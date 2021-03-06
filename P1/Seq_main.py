from Seq import Seq

seq_1 = Seq(input("Enter the sequence 1: "))
seq_2 = Seq(input("Enter the sequence 2: "))
seq_3 = Seq(seq_1.complement())
seq_4 = Seq(seq_3.reverse())

str1 = seq_1.strbases
str2 = seq_2.strbases
str3 = seq_3.strbases
str4 = seq_4.strbases

len_1 = seq_1.len()
len_2 = seq_2.len()
len_3 = seq_3.len()
len_4 = seq_4.len()

count_1 = seq_1.count()
count_2 = seq_2.count()
count_3 = seq_3.count()
count_4 = seq_4.count()

per_1 = seq_1.perc()
per_2 = seq_2.perc()
per_3 = seq_3.perc()
per_4 = seq_4.perc()

print("Sequence 1: ", str1)
print(" Length: ", len_1)
print(" Bases count: ", count_1)
print(" Bases percentage: ", per_1)
print("")
print("Sequence 2: ", str2)
print(" Length: ", len_2)
print(" Bases count: ", count_2)
print(" Bases percentage: ", per_2)
print("")
print("Sequence 3: ", str3)
print(" Length: ", len_3)
print(" Bases count: ", count_3)
print(" Bases percentage: ", per_3)
print("")
print("Sequence 4: ", str4)
print(" Length: ", len_4)
print(" Bases count: ", count_4)
print(" Bases percentage: ", per_4)
