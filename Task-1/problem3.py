# (a, e, i, o, u)
# Data Science
word = input("Enter any word: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for ch in word:
    for vowel in vowels:
        if ch == vowel:
            count+=1

print(f"The number of vowels is: {count}")