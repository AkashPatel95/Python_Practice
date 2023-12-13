#Python – Replace multiple words with K

original_string="This is a sample sentence with multiple words."
words_to_remove=["is", "a", "with", "words"]

for word in words_to_remove:
    if word in original_string:
        original_string=original_string.replace(word,"K")

print(original_string)