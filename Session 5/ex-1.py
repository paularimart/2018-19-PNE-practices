def count_A(seq):
    """Counting the number of As in the sequence"""
    # Counter for the As
    result = 0

    for x in seq:
        if x == "A":
            result += 1

    # Return the result
    return result

# Main program

s = "AGTCGTAGCTGCCCTAGAACGTAGCTTTGACGCAAGCT"

num_A = count_A(s)
print("The number of As is:", num_A)

# Calculate the total sequence length
seq_len = len(s)

# Calculate the percentage of As in the sequence
per = round(100.0 * num_A / seq_len, 1)

print("The total length is:", seq_len)
print("The percentage of As is: {}%".format(per))

