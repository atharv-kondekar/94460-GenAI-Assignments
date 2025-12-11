'''
Q1:
Write a Python program that takes a sentence from the user and prints:
        Number of characters
        Number of words
        Number of vowels
Hint: Use split(), loops, and vowel checking.
'''

sentence = input("Enter  Sentence : ")

num_char = len(sentence)

num_words=len(sentence.split())

vowels = "aeiouAEIOU"
count=0

for ch in sentence:
    if ch in vowels:
        count+=1

print("characters : ",num_char)
print("words = ",num_words)
print("vowels : ",count)