# I replace compound numbers by this number and then delete all of this from the list
replacement = .1

def prime_num_check(sqnc, prime_num):
    """
    Check in turn all numbers in the sequence for simple and complex.
    Replace all complex nums by the replacement
    """
    for i in range(len(sqnc)):
        if sqnc[i] != prime_num and sqnc[i] % prime_num == 0:
            sqnc[i] = replacement
    
def clean_up_list(sqnc):
    """
    Clean up the list from all unnecessary numbers
    """
    i = 0
    while i < len(sqnc):
        if sqnc[i] == replacement:
            del sqnc[i]
        else:
            i += 1

def eratosthenes(top_num):
    """
    Find the numbers of Eratosthenes up to a certain number and 
    return formed list with simple nums
    """
    sqnc = [i for i in range(2, top_num)]

    for i in sqnc:
        prime_num_check(sqnc, i)
    
    clean_up_list(sqnc)

    return sqnc

