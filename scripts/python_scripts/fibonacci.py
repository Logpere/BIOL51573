#!/usr/bin/env python3

import argparse


###------ function to parse the command-line arguments
def get_args():
    ###------------- accept and parse command line arguments
    # create an argument parser object
    parser = argparse.ArgumentParser(description="This script calculates the number at a given position \
                                     in the Fibonacci sequence")

    # add a positional argument, in this case, the position in the Fibonacci sequence
    parser.add_argument("position", help="Position in the Fibonacci sequence", type=int)

    # an optional argument for verbose output or not
    # if 'store_true', this means assign 'True' if the optional argument is specified
    # on the command line, so the default for 'store_true' is actually false
    parser.add_argument("-v", "--verbose", help="Print verbose output", action='store_true')

    # parse the arguments and return in two steps
    args = parser.parse_args()
    return args

    # or, parse the arguments and return in one step
    # return parser.parse_args()



###------ function to calculate the Fibonacci number
def fib():
    # initialize two integers
    a,b = 0,1

    for i in range(int(beyonce.position)):
        a,b = b,a+b

    fibonacci_number = a
    return fibonacci_number


###------ function to print the output
def print_output(output):
    if beyonce.verbose:
        print(f"The Fibonacci number for {beyonce.position} is {output}.")
    else:
        print(fibnum)


###------ define the main() function
def main():
    fibnum = fib()
    print_output(fibnum)
    # this print statement will not print variables that are local to fib()
    # print(a, b, fibonacci_number)

###------ calling get_args() happens out here on its own
beyonce = get_args()


# set the environment for this script
# is this main (i.e., a standalone Python script), or
# is this a Python module being called by another script
if __name__ == '__main__':
    main()



















