print("This program calculates the total length of a DNA sequence and the number of bases that compound it")
DNA_seq = "AGCATTTTATGCTACGATCGTACGTCTACGATGCTCGTCGTACGTACATGCTACGTACGATGTGGCATATTTATACGTACTACGTACAACCCGTAGCTACGTACG"

print("Total length:", len(DNA_seq))

counter_A = 0
counter_T = 0
counter_G = 0
counter_C = 0

for x in DNA_seq:
    if x == "A":
        counter_A += 1
    elif x == "T":
        counter_T += 1
    elif x == "G":
        counter_G += 1
    else:
        counter_C += 1

print("A:", counter_A)
print("T:", counter_T)
print("G:", counter_G)
print("C:", counter_C)
