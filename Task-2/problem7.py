file = open("simple_text.txt")
content = file.read()
words = content.split()
count = 0
for word in words:
    if len(word) > 5 :
        count += 1

print(count)
