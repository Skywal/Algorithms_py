# My implementation of the sieve of eratosthenes
from simple_num import *
from lcd_lcm import *
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--first", required=True, help="First integer")
ap.add_argument("-b", "--second", required=True, help="Second integer")
#ap.add_argument("-c", "--third", required=True, help="Third integer")
args = vars(ap.parse_args())

if __name__ == "__main__":
    print("""
    Find the largest common divisor and least common multiple
    for three numbers {}, {} 
    and numbers of Eratosthenes for them.
    """.format(args['first'], args['second']))

    list_for_first = list(eratosthenes(int(args['first'])))
    list_for_second = list(eratosthenes(int(args['second'])))
    #list_for_third = list(eratosthenes(int(args['third'])))

    print(f"For number {args['first']} all simple nums are \n{list_for_first}\n")
    print(f"For number {args['second']} all simple nums are \n{list_for_second}\n")
    #print(f"For number {args['third']} all simple nums are \n{list_for_third}\n")

    print(f"For numbers {args['first']} and {args['second']}")
    print(f"the largest common divisor is {larg_com_div(int(args['first']), list_for_first, int(args['second']), list_for_second)}")
    print(f"the least common multiple is {lea_com_mult(int(args['first']), list_for_first, int(args['second']), list_for_second)}")
