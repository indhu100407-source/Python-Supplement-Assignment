# Problem 42: Convert list to string
# Find and fix the error

words = ["Hello", "World", "Python"]
sentence = "".join(words)
for word in words:
    sentence += word + " "
print(f"Sentence: {sentence}")
