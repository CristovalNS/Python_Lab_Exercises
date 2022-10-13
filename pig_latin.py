# Pig latin translator

user_input = input('Enter an english sentence: ').casefold()
words = user_input.split()

yay = "yay"
ay = "ay"
vowel = ["a", "i", "u", "e", "o"]

for a, word in enumerate(words):
    if word[0] in vowel:
        words[a] = words[a] + yay
        # print(word)
    else:
        has_vowel = False

        for b, letter in enumerate(word):
            if letter in vowel:
                words[a] = word[b:] + word[:b] + ay
                has_vowel = True
                break
        if has_vowel is False:
            words[a] = words[a] + ay

translation = ' '.join(words)
print("Pig Latin: ", translation)

