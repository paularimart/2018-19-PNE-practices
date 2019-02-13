class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New sequence created!")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        #dict_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
        comp_seq = ""
        for x in self.strbases:
            if x == "A":
                comp_seq += "T"
            elif x == "T":
                comp_seq += "A"
            elif x == "C":
                comp_seq += "G"
            elif x == "G":
                comp_seq += "C"
        return comp_seq

    def reverse(self):
        rev_seq = self.strbases[::-1]
        return rev_seq

    def count(self):

        result_A = 0
        result_T = 0
        result_C = 0
        result_G = 0

        for x in self.strbases:
            if x == "A":
                result_A += 1
            elif x == "T":
                result_T += 1
            elif x == "C":
                result_C += 1
            else:
                result_G += 1

        x = ["A:",result_A, "T:",result_T, "C:",result_C, "G:",result_G]
        return x

    def perc(base):
        if seq_len > 0:
            per_A = round(100.0 * num_A / seq_len, 1)
        else:
            per_A = 0

        print("Base T")
        num_T = dict_bases['T']
        print(" The number of Ts is:", num_T)
        if seq_len > 0:
            per_T = round(100.0 * num_T / seq_len, 1)
        else:
            per_T = 0

        print("Base C")
        num_C = dict_bases['C']
        print(" The number of Ts is:", num_C)
        if seq_len > 0:
            per_C = round(100.0 * num_C / seq_len, 1)
        else:
            per_C = 0

        print("Base G")
        num_G = dict_bases['G']
        print(" The number of Gs is:", num_G)
        if seq_len > 0:
            per_G = round(100.0 * num_G / seq_len, 1)
        else:
            per_G = 0

        print("A: ", per_A, "T: ", per_T, "C: ", per_C, "G: ", per_G)
