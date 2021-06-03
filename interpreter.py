from sys import argv
from readchar import readchar as rchar
import numpy

memory = numpy.zeros(30000,dtype = numpy.uint8)
pointer : int = 0
code : str
quantity : int

def interpreter():
    global pointer, memory, code, quantity
    brackets = 0
    flag = True

    #for factor
    letter = 0
    quantity = len(code) - 1
    visual = code[letter] #for debug

    while flag:
        if code[letter] == '+': memory[pointer] += 1
        elif code[letter] == '-': memory[pointer] -= 1
        elif code[letter] == '>': pointer += 1
        elif code[letter] == '<': pointer -= 1
        elif code[letter] == '.': print(chr(memory[pointer]),end='')
        elif code[letter] == ',': 
            memory[pointer] = ord(input())
        #Loops
        elif code[letter] == '[':
            if not memory[pointer]:
                brackets += 1
                while code[letter] != ']' or brackets != 0:
                    letter += 1
                    if code[letter] == '[': brackets += 1
                    elif code[letter] == ']': brackets -=1
        elif code[letter] == ']':
            if memory[pointer]:
                brackets += 1
                while code[letter] != '[' or brackets != 0:
                    letter -= 1
                    if code[letter] == ']': brackets += 1
                    elif code[letter] == '[': brackets -=1
        
        #Exit Cases
        letter += 1
        if letter > quantity: flag = False
        else: visual = code[letter]

def validates():
    global code
    counting = 0
    for letters in code:
        if letters == '[': counting += 1
        elif letters == ']':
            if not counting: return False
            counting -= 1
    return counting == 0
        
def main(file_name = 'file.b'):
    global pointer, memory, code, quantity
    with open(file_name,'r') as file: code = file.read()
    quantity = len(code)-1
    if validates(): interpreter()
    else: print("There's something wrong with the code. Probably with the ([]) operators.")
    print(f'\nMemory: {memory}')

if __name__ == '__main__':
    if argv[-1].endswith('.b'): main(argv[-1])
    else: main()


