texts = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary

text_counts = {}
for text in texts:
    if text in text_counts:
        text_counts[text]+= 1
    else:
        text_counts[text] = 1

print(text_counts)