"""
Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter/chars of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.

"""
sentence = input("Please enter your sentence")
freq = []
for i in sentence :
  freq.append(sentence.count(i))
letter_count =zip(sentence, freq)
set(letter_count)