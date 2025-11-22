# List of very common English words
COMMON_WORDS = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
    "for", "not", "on", "with", "he", "as", "you", "do", "at", "this",
    "but", "his", "by", "from", "they", "we", "say", "her", "she", "or",
    "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know",
    "take", "people", "into", "year", "your", "good", "some", "could",
    "them", "see", "other", "than", "then", "now", "look", "only", "come",
    "its", "over", "think", "also", "back", "after", "use", "two", "how",
    "our", "work", "first", "well", "way", "even", "new", "want", "because"
}

# Common bigrams in English (for burst typing)
COMMON_BIGRAMS = {
    "th", "he", "in", "er", "an", "re", "on", "at", "en", "nd", "ti", "es", "or", "te", "of", "ed", "is", "it", "al", "ar", "st", "to", "nt", "ng", "se", "ha", "as", "ou", "io", "le", "ve", "co", "me", "de", "hi", "ri", "ro", "ic", "ne", "ea", "ra", "ce"
}

def get_word_difficulty(word):
    word_lower = word.lower().strip(".,!?;:")
    if word_lower in COMMON_WORDS:
        return "common"
    is_long = len(word_lower) > 8
    has_complex_chars = any(c in "zxqj" for c in word_lower)
    if is_long or has_complex_chars:
        return "complex"
    return "normal"

def is_common_bigram(char1, char2):
    bigram = (char1 + char2).lower()
    return bigram in COMMON_BIGRAMS
