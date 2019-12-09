# My smplementation of the sieve of eratosthenes
replacement = .1

def prime_num_check(sqnc, prime_num):
    
    for i in range(len(sqnc)):
        if sqnc[i] != prime_num and sqnc[i] % prime_num == 0:
            sqnc[i] = replacement
    
def clean_up_list(sqnc):
    i = 0

    while i < len(sqnc):
        if sqnc[i] == replacement:
            del sqnc[i]
        else:
            i += 1

def eratosthenes(top_num):
    sqnc = [i for i in range(2, top_num)]

    for i in sqnc:
        prime_num_check(sqnc, i)
    
    clean_up_list(sqnc)

    print(f"{sqnc}")


if __name__ == "__main__":
    
    eratosthenes(1000)

    #print(" algorithm ", prime_num_check(sqnc, 2 ))
    #N = 100
    #prime = [i for i in range(2, N)]
    #print(f"prime is {prime}")
