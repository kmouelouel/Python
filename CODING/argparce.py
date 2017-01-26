import argparse
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b= b,a+b
    return a

def Main():
    parser= argparse.ArgumentParser(description='Process fib function')
    parser.add_argument('num', help="The Fibonacci Number you wish to calculate.",type=int)
    args=parser.parse_args()

    result = fib(args.num)
    print("the "+str(args.num)+ "the fib number is "+ str(result))
Main()
    
