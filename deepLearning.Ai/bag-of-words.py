# Non transformers models
TextInput = "This is a simple text to learn"

Tokens = TextInput.split(" ")

Vocabulary = [ "This", "simple", "learn", ]

vectorRepresentation = []
for token in Tokens:
    if token in Vocabulary:
        vectorRepresentation.append(1)
    else:
        vectorRepresentation.append(0)
print(vectorRepresentation)