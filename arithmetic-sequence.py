# Generating an arithmetic sequence
start = 5
difference = 3
terms = 8

sequence = [start + i * difference for i in range(terms)]
print("Arithmetic Sequence:", sequence)
