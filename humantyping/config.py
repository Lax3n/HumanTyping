# Typing model configuration

# Default average typing speed (words per minute)
DEFAULT_WPM = 60
WPM_STD = 10  # WPM standard deviation

# Average word length (standard)
AVG_WORD_LENGTH = 5

# Probabilities
PROB_ERROR = 0.04  
PROB_SWAP_ERROR = 0.015 
PROB_NOTICE_ERROR = 0.85 # Lowered slightly to let some mistakes pass and be corrected later
PROB_NOTICE_ERROR_LATE = 0.99 # Probability of noticing mistakes during final review

# Speed factors
SPEED_BOOST_COMMON_WORD = 0.6    
SPEED_PENALTY_COMPLEX_WORD = 1.3 
SPEED_BOOST_CLOSE_KEYS = 0.5     
SPEED_BOOST_BIGRAM = 0.4         

# Time (in seconds)
TIME_KEYSTROKE_STD = 0.03        
TIME_BACKSPACE_MEAN = 0.12
TIME_BACKSPACE_STD = 0.02
TIME_ARROW_MEAN = 0.15 # Time to move cursor (arrows)
TIME_ARROW_STD = 0.03
TIME_REACTION_MEAN = 0.35        
TIME_REACTION_STD = 0.1

# Specific penalties
TIME_DIRECT_ACCENT_PENALTY = 0.15 
TIME_COMPOSED_ACCENT_PENALTY = 0.4 
TIME_UPPERCASE_PENALTY = 0.2
TIME_SPACE_PAUSE_MEAN = 0.25
TIME_SPACE_PAUSE_STD = 0.05

# Fatigue
FATIGUE_FACTOR = 1.0005 
