"""

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

"""

from decimal import *

def x_from_y(y):
    x = (1 + (2*y) + Decimal(1 + (8*pow(y,2))).sqrt())/2
    return x
    
def check_prob(x, y):
    p = (x/(x+y)) * ((x-1)/(x+y-1))
    return p
    
def main_func():
    getcontext().prec = 30
    ratio = round(2414213567470 / 1000000002111 , 6) 
    print(ratio)
    start_num = 1e12 / (ratio + 1) 

    #for y in range(int(start_num), int(start_num + 1e6)):
    #start_num = 1
    for y in range(int(start_num), int(start_num + 1e7)):
        try:
            x = x_from_y(y)
            
        except ValueError:
            continue
        if x == int(x):
            p = check_prob(int(x), y)
            print('y: {}, x: {}, total: {}, prob: {}'.format(y, x, x+y, p))
           
    return 0

if __name__ == "__main__":
    main_func()
