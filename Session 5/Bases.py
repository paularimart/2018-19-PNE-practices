def count_bases(seq):
    """Counting the number of As in the sequence"""
    dict_bases = dict()

    # Counter for the As
    result_A = 0
    result_T = 0
    result_C = 0
    result_G = 0

    for x in seq:
        if x == "A":
            result_A += 1
        elif x == "T":
            result_T += 1
        elif x == "C":
            result_C += 1
        else:
            result_G += 1

    dict_bases["A"] = result_A
    dict_bases["T"] = result_T
    dict_bases["C"] = result_C
    dict_bases["G"] = result_G

    # Return the result
    return dict_bases