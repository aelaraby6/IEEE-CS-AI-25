sentence = input('Write the sentence: ')
words = sentence.split()

reversedWords = [word[::-1] for word in words]
reversedSentence = " ".join(reversedWords)

print(reversedSentence)
