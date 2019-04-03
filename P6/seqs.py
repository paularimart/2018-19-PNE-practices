class Seq:
    def __init__(self, strbases):

        self.strbases = strbases

        def check(self):
            bases = ["A", "C", "G", "T"]
            for x in self.strbases:
                if x != bases:
                    result = "NO"
            return result

        def len(self):
            return len(self.strbases)

        def count_A(self):
            result_A = 0
            for x in self.strbases:
                if x == "A":
                    result_A += 1
            x = result_A
            return x

        def count_T(self):
            result_T = 0
            for x in self.strbases:
                if x == "T":
                    result_T += 1
            x = result_T
            return x

        def count_C(self):
            result_C = 0
            for x in self.strbases:
                if x == "C":
                    result_C += 1
            x = result_C
            return x

        def count_G(self):
            result_G = 0
            for x in self.strbases:
                if x == "G":
                    result_G += 1
            x = result_G
            return x

        def perc_A(self):
            seq_len = len(self.strbases)
            result_A = 0
            for x in self.strbases:
                if x == "A":
                    result_A += 1
            if seq_len > 0:
                per_A = round(100.0 * result_A / seq_len, 1)
            else:
                per_A = 0
            return per_A

        def perc_T(self):
            seq_len = len(self.strbases)
            result_T = 0
            for x in self.strbases:
                if x == "T":
                    result_T += 1
            if seq_len > 0:
                per_T = round(100.0 * result_T / seq_len, 1)
            else:
                per_T = 0
            return per_T

        def perc_C(self):
            seq_len = len(self.strbases)
            result_C = 0
            for x in self.strbases:
                if x == "C":
                    result_C += 1
            if seq_len > 0:
                per_C = round(100.0 * result_C / seq_len, 1)
            else:
                per_C = 0
            return per_C

        def perc_G(self):
            seq_len = len(self.strbases)
            result_G = 0
            for x in self.strbases:
                if x == "G":
                    result_G += 1
            if seq_len > 0:
                per_G = round(100.0 * result_G / seq_len, 1)
            else:
                per_G = 0
            return per_G

