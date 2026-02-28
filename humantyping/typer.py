import numpy as np
from dataclasses import dataclass, field
from typing import List
from .config import *
from .keyboard import KeyboardLayout
from .language import get_word_difficulty, is_common_bigram

@dataclass
class TypingState:
    current_text: str = ""
    target_text: str = ""
    total_time: float = 0.0
    history: List[tuple] = field(default_factory=list)
    last_char_typed: str = None 
    fatigue_multiplier: float = 1.0
    mental_cursor_pos: int = 0 

class MarkovTyper:
    def __init__(self, target_text, target_wpm=DEFAULT_WPM, layout="qwerty"):
        self.target_text = target_text
        self.keyboard = KeyboardLayout(layout)
        self.state = TypingState(target_text=target_text)
        
        self.session_wpm = np.random.normal(target_wpm, WPM_STD)
        self.session_wpm = max(10, self.session_wpm)
        self.base_keystroke_time = 60 / (self.session_wpm * AVG_WORD_LENGTH)
        
        self.state.history.append((0.0, f"INIT (WPM: {self.session_wpm:.1f})", ""))

    def _get_current_word_context(self):
        idx = self.state.mental_cursor_pos
        if idx >= len(self.target_text):
            return None
        start = idx
        while start > 0 and self.target_text[start-1] != ' ':
            start -= 1
        end = idx
        while end < len(self.target_text) and self.target_text[end] != ' ':
            end += 1
        return self.target_text[start:end]

    def _calculate_keystroke_time(self, char_to_type):
        time = self.base_keystroke_time * self.state.fatigue_multiplier
        
        current_word = self._get_current_word_context()
        if current_word:
            difficulty = get_word_difficulty(current_word)
            if difficulty == "common":
                time *= SPEED_BOOST_COMMON_WORD
            elif difficulty == "complex":
                time *= SPEED_PENALTY_COMPLEX_WORD
        
        if self.state.last_char_typed:
            if is_common_bigram(self.state.last_char_typed, char_to_type):
                time *= SPEED_BOOST_BIGRAM 
            else:
                dist = self.keyboard.get_distance(self.state.last_char_typed, char_to_type)
                if dist < 2.0 and dist > 0:
                    time *= SPEED_BOOST_CLOSE_KEYS
                elif dist > 4.0:
                    time *= 1.2

        if char_to_type == ' ':
            time += np.random.normal(TIME_SPACE_PAUSE_MEAN, TIME_SPACE_PAUSE_STD)
        elif self.keyboard.is_composed_accent(char_to_type):
            time += TIME_COMPOSED_ACCENT_PENALTY
        elif self.keyboard.is_direct_accent(char_to_type):
            time += TIME_DIRECT_ACCENT_PENALTY
        elif char_to_type.isupper():
            time += TIME_UPPERCASE_PENALTY
                
        dt = np.random.normal(time, TIME_KEYSTROKE_STD)
        return max(0.02, dt)

    def step(self):
        # 1. Check for completion
        if self.state.current_text == self.target_text:
            return None

        # --- MONITORING & CORRECTION PHASE ---
        
        # Calculate divergence point
        first_error_pos = len(self.target_text)
        min_len = min(len(self.state.current_text), len(self.target_text))
        for i in range(min_len):
            if self.state.current_text[i] != self.target_text[i]:
                first_error_pos = i
                break
        
        # Also consider over-typing as an error
        if len(self.state.current_text) > len(self.target_text) and first_error_pos == len(self.target_text):
            first_error_pos = len(self.target_text)

        # Do we have an error?
        if first_error_pos < len(self.state.current_text):
            should_correct = False
            
            last_action = self.state.history[-1][1] if self.state.history else ""
            
            # Case 0: CONTINUED BACKSPACING (Critical)
            if "BACKSPACE" in last_action:
                should_correct = True # Lock into backspacing until fixed

            # Case A: End of text (Always correct)
            elif self.state.mental_cursor_pos >= len(self.target_text):
                should_correct = True
                
            # Case B: End of Word / Context Check
            elif len(self.state.current_text) > 0:
                last_char = self.state.current_text[-1]
                distance = len(self.state.current_text) - first_error_pos
                
                # Check at word boundaries (Strict)
                # Correction is mandatory at any separator to prevent error accumulation
                if last_char in ' \n\t.,;!?:()[]{}<>"\'':
                    should_correct = True
                
                # Drift Check (Don't let errors linger)
                elif distance >= 2:
                    # High probability to notice error as we type further away
                    rand_value = np.random.random()
                    if rand_value < 0.8:
                        should_correct = True
                    
                # Immediate reaction (1 char past error)
                elif distance == 1:
                    rand_value = np.random.random()
                    if rand_value < PROB_NOTICE_ERROR:
                        should_correct = True

            if should_correct:
                # Reaction time check (only if we weren't already backspacing)
                if "BACKSPACE" not in last_action:
                     dt = np.random.normal(TIME_REACTION_MEAN, TIME_REACTION_STD)
                     self.state.total_time += max(0.1, dt)
                
                # Perform Backspace
                dt = np.random.normal(TIME_BACKSPACE_MEAN, TIME_BACKSPACE_STD)
                self.state.total_time += dt
                self.state.current_text = self.state.current_text[:-1]
                
                step = (self.state.total_time, "BACKSPACE", self.state.current_text)
                self.state.history.append(step)
                
                # Sync mental cursor immediately
                self.state.mental_cursor_pos = len(self.state.current_text)
                return step

        # --- TYPING PHASE ---

        # Sync mental cursor if we backspaced (redundant safety)
        if self.state.mental_cursor_pos > len(self.state.current_text):
             self.state.mental_cursor_pos = len(self.state.current_text)
        
        # If we are done typing but text is correct (caught by top check), or waiting for consistency
        if self.state.mental_cursor_pos >= len(self.target_text):
             # This happens if we just corrected an 'overtype' error and now we are 'at the end'
             # The next loop will catch completion.
             return None

        char_intended = self.target_text[self.state.mental_cursor_pos]
        self.state.fatigue_multiplier *= FATIGUE_FACTOR

        # Swap Error (Anticipation)
        # Using the next char after the supposed typed char
        # Example: "the" -> "hte". Typing 'h' instead of 't'.
        if len(self.target_text) > self.state.mental_cursor_pos + 1:
            char_after = self.target_text[self.state.mental_cursor_pos + 1]
            if char_after != ' ' and char_after != char_intended:
                if np.random.random() < PROB_SWAP_ERROR:
                    dt = self._calculate_keystroke_time(char_after)
                    self.state.total_time += dt
                    self.state.current_text += char_after
                    self.state.last_char_typed = char_after
                    step = (self.state.total_time, f"TYPED_SWAP '{char_after}'", self.state.current_text)
                    self.state.history.append(step)
                    self.state.mental_cursor_pos += 1
                    return step

        # Normal Typing (Success or Error)
        current_prob_error = PROB_ERROR
        word_diff = get_word_difficulty(self._get_current_word_context() or "")
        if word_diff == "complex": 
            current_prob_error *= 1.5
        elif word_diff == "common": 
            current_prob_error *= 0.5
        if self.keyboard.is_composed_accent(char_intended): 
            current_prob_error *= 2.0

        if np.random.random() < current_prob_error:
            # Generate Error
            wrong_char = self.keyboard.get_random_neighbor(char_intended)
            dt = self._calculate_keystroke_time(wrong_char)
            self.state.total_time += dt
            self.state.current_text += wrong_char
            self.state.last_char_typed = wrong_char
            step = (self.state.total_time, f"TYPED_ERROR '{wrong_char}'", self.state.current_text)
            self.state.history.append(step)
            self.state.mental_cursor_pos += 1
        else:
            # Success
            dt = self._calculate_keystroke_time(char_intended)
            self.state.total_time += dt
            self.state.current_text += char_intended
            self.state.last_char_typed = char_intended
            step = (self.state.total_time, f"TYPED '{char_intended}'", self.state.current_text)
            self.state.history.append(step)
            self.state.mental_cursor_pos += 1
            
        return step

    def run(self):
        steps = 0
        max_steps = len(self.target_text) * 10
        while self.step() is not None:
            steps += 1
            if steps > max_steps:
                break
        return self.state.total_time, self.state.history