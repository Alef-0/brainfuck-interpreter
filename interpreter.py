from sys import argv
from os import path
import numpy

memory = numpy.zeros(30000, dtype = numpy.uint8)
numpy.set_printoptions(edgeitems = 10)
pointer : int = 0
code : str = ""
quantity : int = 0

def interpreter():
    global pointer, memory, code, quantity
    brackets = 0
    flag = quantity > 0

    #for factor
    letter = 0
    visual = code[letter] # debug

    while flag:
        if   code[letter] == '+': memory[pointer] += 1
        elif code[letter] == '-': memory[pointer] -= 1
        elif code[letter] == '>': pointer += 1
        elif code[letter] == '<': pointer -= 1
        elif code[letter] == '.': print(chr(memory[pointer]), end='')
        elif code[letter] == ',':
            text = input()
            if not len(text): memory[pointer] = ord('\n')
            else:             memory[pointer] = ord(text)
        #Loops
        elif code[letter] == '[':
            if not memory[pointer]:
                brackets += 1
                while code[letter] != ']' or brackets:
                    letter += 1
                    if   code[letter] == '[': brackets += 1
                    elif code[letter] == ']': brackets -= 1
        elif code[letter] == ']':
            if memory[pointer]:
                brackets += 1
                while code[letter] != '[' or brackets:
                    letter -= 1
                    if   code[letter] == ']': brackets += 1
                    elif code[letter] == '[': brackets -= 1
        
        #Exit Cases
        letter += 1
        if (flag := (letter < quantity)): visual = code[letter]

def validates():
    global code
    counting = 0
    for letters in code:
        if   letters == '[': counting += 1
        elif letters == ']':
            if not counting: return False
            counting -= 1
    return counting == 0
        
def main(file_name = 'brainfuck.b'):
    global pointer, memory, code, quantity
    no_problem = True
    file_name = path.join(path.dirname(__file__),file_name)
    # File check
    if path.isfile(file_name):
        with open(file_name,'r') as file: code = file.read().strip()
    else: 
        print("Can't find the file")
        no_problem = False
    if ((quantity := len(code)) < 1): 
        print("There's nothing to execute")
        no_problem = False
    # End of file check
    if no_problem: 
        if validates(): interpreter()
        else: print("There's something wrong with the code. Probably with the ([]) operators.")
    print(f'\nMemory: {memory}') #Can be useful for quick checks

if __name__ == '__main__':
    if argv[-1].endswith('.b'): main(argv[-1])
    else: main()