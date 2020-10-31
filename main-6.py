#Name: Nafisa Chowdhury
#PSID: 1591144

input_words = input()
words = input_words.split()

for word in words:
    frequency = words.count(word)
    print(word, frequency)
