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

        print("A:",result_A, "T:",result_T, "C:",result_C, "G:",result_G)

    #def perc(base):
