from Bases import count_bases

s1 = input("Enter the sequence 1: ")
s2 = input("Enter the sequence 2: ")

list_seqs = [s1, s2]
seq_num = 0

for s in list_seqs:
# Calculate the total sequence length
    print("")
    seq_num += 1
    seq_len = len(s)
    print("Sequence", seq_num, "is", seq_len, "bases in length")

    dict_bases = count_bases(s)

    print("Base A")
    num_A = dict_bases['A']
    print(" The number of As is:", num_A)
    if seq_len > 0:
        per_A = round(100.0 * num_A / seq_len, 1)
    else:
        per_A = 0
    print(" The percentage of As is: {}%".format(per_A))

    print("Base T")
    num_T = dict_bases['T']
    print(" The number of Ts is:", num_T)
    if seq_len > 0:
        per_T = round(100.0 * num_T / seq_len, 1)
    else:
        per_T = 0
    print(" The percentage of Ts is: {}%".format(per_T))

    print("Base C")
    num_C = dict_bases['C']
    print(" The number of Ts is:", num_C)
    if seq_len > 0:
        per_C = round(100.0 * num_C / seq_len, 1)
    else:
        per_C = 0
    print(" The percentage of Cs is: {}%".format(per_C))

    print("Base G")
    num_G = dict_bases['G']
    print(" The number of Gs is:", num_G)
    if seq_len > 0:
        per_G = round(100.0 * num_G / seq_len, 1)
    else:
        per_G = 0
    print(" The percentage of Gs is: {}%".format(per_G))