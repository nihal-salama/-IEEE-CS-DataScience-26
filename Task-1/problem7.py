sentence = input("Write a sentente: ")
words = sentence.split()
max = words[0]
for i in range(len(words)):
    if len(words[i]) > len(max):
        max = words[i]

print(f"The longest word is: {max}")
print(words)
