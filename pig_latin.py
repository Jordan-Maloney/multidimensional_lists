##
# pig_latin.py
# Jordan Maloney
# 13/4/21


def sentence_to_list(sentence):
    """
    Takes the sentence and turns it into a list
    """
    words = sentence.split(" ")
    return words


def vowel_converter(word):
    """
    Takes a word that starts with a vowel and converts it
    to Pig Latin form
    """
    ADDER = "way"
    new_word = word + ADDER
    return new_word


def consonant_converter(VOWELS, word):
    """
    Takes a word that starts with a consonant and converts it
    to Pig Latin form
    """
    ADDER = "ay"
    # Find the index of the first vowel
    vowel_idx = 0
    first_vowel = True
    for letter in word:
        if letter in VOWELS and first_vowel:
            vowel_idx = word.index(letter)
            first_vowel = False
    # Take a slice of everything before the vowel

    
# Main routine
while __name__ == "__main__":
    sentence = input("Please type a sentence. ").lower()
    # Convert sentence to list
    words = sentence_to_list(sentence)
    VOWELS = ["a", "e", "i", "o", "u"]
    for word in words:
        # Convert words which start with vowels
        if word[0] in VOWELS:
            word = vowel_converter(word)
        # Convert words which start with consonants
        elif (word[0] >= ord[97]
              and word[0] <= ord[122]
              and word[0] not in VOWELS):
            word = consonant_converter(VOWELS, word)
