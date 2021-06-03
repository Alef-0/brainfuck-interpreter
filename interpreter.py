from sys import argv
from readchar import readchar as rchar
import numpy

tape = numpy.zeros(30000,dtype = numpy.uint8)
pointer : int = 0
program : str
quantity : int

def interpreter():
    global pointer, tape, program, quantity
    brackets = 0
    flag = True

    #for factor
    letter = 0
    quantity = len(program)

    while flag:
        if program[letter] == '+': tape[pointer] += 1
        elif program[letter] == '-': tape[pointer] -= 1
        elif program[letter] == '>': pointer += 1
        elif program[letter] == '<': pointer -= 1
        elif program[letter] == '.': print(chr(tape[pointer]),end='')
        elif program[letter] == ',': tape[pointer] = ord(input())
        #Loops
        elif program[letter] == '[':
            if not tape[pointer]:
                brackets += 1
                while program[letter] != ']' or brackets != 0:
                    letter += 1
                    if program[letter] == '[': brackets += 1
                    elif program[letter] == ']': brackets -=1
        elif program[letter] == ']':
            if tape[pointer]:
                brackets += 1
                while program[letter] != '[' or brackets != 0:
                    letter -= 1
                    if program[letter] == ']': brackets += 1
                    elif program[letter] == '[': brackets -=1
        
        #Exit Cases
        letter += 1
        if letter > quantity: flag = False

def validates():
    global program
    counting = 0
    for letters in program:
        if letters == '[': counting += 1
        elif letters == ']':
            if not counting: return False
            counting -= 1
    return counting == 0
        
def main(file_name = 'file.b'):
    global pointer, tape, program, quantity
    with open(file_name,'r') as file: program = file.read()
    quantity = len(program)-1
    if validates(): interpreter()
    else: print("There's something wrong with the code. Probably with the ([]) operators.")
    print(f'\nMemory: {tape}')

if __name__ == '__main__':
    if argv[-1].endswith('.b'): main(argv[-1])
    else: main()


