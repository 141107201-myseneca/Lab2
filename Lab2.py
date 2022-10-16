#!usr/bin/python 3
import sys



def sys():
    name= sys.argv[1] 
    age= sys.argv[2]
    print('Variable 1: ' + sys.argv[1])
    print('Variable 2: ' + sys.argv[2])
    print('Script: ' + sys.argv[0])
    print(sys.argv)

if '__name__' == '__main__':
    sys()
