def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score



n = int(input("Enter the number of words: "))
words = input("Enter the words separated by spaces: ").split()
print(score_words(words))

# Debugging Process:
# Verified that the is_vowel function correctly identifies vowels.
# Checked the loop in score_words to ensure:
    # Correct counting of vowels in each word.
    # Proper addition to the score based on even or odd vowel counts.
# Ensured the program handles edge cases like:
    # No words (n = 0).
    # Words with no vowels.