import numpy as np
from .typer import MarkovTyper
import time
import sys

def run_monte_carlo(target_text, wpm, n_simulations=100):
    """
    Runs n_simulations to estimate typing time distribution.
    """
    times = []
    print(f"Running {n_simulations} simulations for text: '{target_text}' (Target WPM: {wpm})")
    
    start_global = time.time()
    
    for i in range(n_simulations):
        typer = MarkovTyper(target_text, target_wpm=wpm)
        total_time, _ = typer.run()
        times.append(total_time)
        
    end_global = time.time()
    
    times = np.array(times)
    mean_time = np.mean(times)
    std_time = np.std(times)
    min_time = np.min(times)
    max_time = np.max(times)
    
    print(f"\n--- Monte Carlo Results ---")
    print(f"Estimated Mean Time : {mean_time:.4f} s")
    print(f"Standard Deviation  : {std_time:.4f} s")
    print(f"Min / Max           : {min_time:.4f} s / {max_time:.4f} s")
    print(f"Computation Time    : {end_global - start_global:.4f} s")
    
    return times

def demo_single_run(target_text, wpm):
    """
    Displays a detailed real-time simulation.
    """
    has_newlines = True if target_text.count("\n") > 0 else False
    if has_newlines:
        print(f"\n--- Real-Time Simulation Demo:\n{target_text}\n(Target WPM: {wpm}) ---")
    else:
        print(f"\n--- Real-Time Simulation Demo: '{target_text}' (Target WPM: {wpm}) ---")
    print("Preparing simulation...\n")
    
    # 1. Calculate trajectory instantly
    typer = MarkovTyper(target_text, target_wpm=wpm)
    total_time, history = typer.run()
    
    # 2. Replay history
    print("START TYPING:")
    print("-" * 40)
    
    last_time = 0.0
    current_output = ""
    
    for t, action, text in history:
        # Calculate delay
        delay = t - last_time
        if delay > 0:
            time.sleep(delay)
        last_time = t
        
        # Differential update logic
        if text.startswith(current_output):
            # We added characters (Normal typing or swap)
            new_part = text[len(current_output):]
            sys.stdout.write(new_part)
        elif current_output.startswith(text):
            # We removed characters (Backspacing)
            removed_part = current_output[len(text):]
            for char in reversed(removed_part):
                if char == '\n':
                    # Move cursor up one line
                    sys.stdout.write('\033[A')
                    # Find the length of the line we are moving up to
                    lines = text.split('\n')
                    last_line_len = len(lines[-1]) if lines else 0
                    # Move cursor to the end of that line
                    # \033[G moves to absolute column. Using a large number or exact len
                    sys.stdout.write(f'\033[{last_line_len + 1}G')
                else:
                    # Generic backspace/clear
                    sys.stdout.write('\b \b')
        else:
            # Divergence (e.g. middle-string correction if implemented in future)
            # Fallback: Clear block and redraw (rare)
            prev_lines = current_output.count('\n')
            if prev_lines > 0:
                sys.stdout.write(f'\033[{prev_lines}A')
            sys.stdout.write('\r\033[J')
            sys.stdout.write(text)
            
        sys.stdout.flush()
        current_output = text
        
    print("\n" + "-" * 40)
    print(f"Total Simulated Time: {total_time:.4f}s")
    
    # Show errors
    errors = [h for h in history if "ERROR" in h[1]]
    if errors:
        print(f"Errors made and corrected: {len(errors)}")
