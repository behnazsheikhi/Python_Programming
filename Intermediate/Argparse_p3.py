# we want to use argparse to parse arguments through command line
import argparse
import sys
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,help='what is the first number?')
    parser.add_argument('--y', type=float, default=2.0, help='what is the second number?')
    parser.add_argument('--operation', type=str, default='add', help='which operation do you choose?')
    args=parser.parse_args()
    sys.stdout.write(str(calculator(args)))

def calculator(args):
    if args.operation=='add':
        result=args.x+args.y
    elif args.operation =='sub' :
        result=args.x-args.y
    elif args.operation =='mul':
        result =args.x*args.y
    elif args.operation =='div':
        result =args.x/args.y
    else:
        result='Invalid Input'
    return result
# output=calculator(2,5,'sub')
# print(output)
if __name__=='__main__':
    main()
