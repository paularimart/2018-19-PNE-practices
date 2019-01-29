file = open("dna.txt", "r")
seq = file.read()

print("Total length:", len(seq))

counter_A = 0
counter_T = 0
counter_G = 0
counter_C = 0

for x in seq:
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
