#!/usr/bin/python3
import sys 
arg_count = len(sys.argv)

arg_list = list(sys.argv)

for arg in range(1, arg_count):
#    if arg != 0:
     print(f"Args @ index {arg} is: {arg_list[arg]}")

#print(arg_count)
