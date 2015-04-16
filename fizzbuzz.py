""" 
Usage: 
	fizzbuzz.py --number=NUMBER
"""

from docopt import docopt

author__ = 'lewiso'

def fizzbuzz(number):
    for i in range(number):
        if(i%3 == 0 and i%5==0):
            print "fizzbuzz"
        elif(i%3 == 0):
            print "fizz"
        elif(i%5 == 0):
            print "buzz"
        else:
            print i


if __name__ == '__main__':
	argv =	docopt(__doc__)
    	fizzbuzz(int(argv['--number']))
