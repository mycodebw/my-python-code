#!/usr/bin/env python
# encoding: utf-8

"""
The minigame 2048 in python
"""

import random

def init():
    """
    initialize a 2048 matrix. return a matrix list
    """
    matrix = [ 0 for i in range(16) ]
    random_lst = random.sample( range(16), 2 ) # generate 2 different number
    matrix[random_lst[0]] = matrix[random_lst[1]] = 2
    return matrix

def move(matrix, direction):
    """
    moving the matrix. return a matrix list
    """
    merged_list = [] #initial the merged index
    if direction == 'u':
        for i in range(16):
            j = i
            while j - 4 >= 0:
                if matrix[j-4] == 0:
                    matrix[j-4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j-4] == matrix[j] and j - 4 not in merged_list and j not in merged_list:
                    matrix[j-4] *=2
                    matrix[j] = 0
                    merged_list.append(j-4)
                    merged_list.append(j)  #prevent the number to be merged twice
                j -= 4
    elif direction == 'd':
        for i in range(15,-1,-1):
            j = i
            while j + 4 < 16:
                if matrix[j+4] == 0:
                    matrix[j+4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j+4] == matrix[j] and j + 4 not in merged_list and j not in merged_list:
                    matrix[j+4] *=2
                    matrix[j] = 0
                    merged_list.append(j)
                    merged_list.append(j+4)
                j += 4
    elif direction == 'l':
        for i in range(16):
            j = i
            while j % 4 != 0:
                if matrix[j-1] == 0:
                    matrix[j-1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j-1] == matrix[j] and j - 1 not in merged_list and j not in merged_list:
                    matrix[j-1] *=2
                    matrix[j] = 0
                    merged_list.append(j-1)
                    merged_list.append(j)
                j -= 1
    else:
        for i in range(15,-1,-1):
            j = i
            while j % 4 != 3:
                if matrix[j+1] == 0:
                    matrix[j+1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j+1] == matrix[j] and j + 1 not in merged_list and j not in merged_list:
                    matrix[j+1] *=2
                    matrix[j] = 0
                    merged_list.append(j)
                    merged_list.append(j+1)
                j += 1
    return matrix
 
def insert(matrix):
    """insert one 2 or 4 into the matrix. return the matrix list
    """
    get_zero_index = []
    for i in range(16):
        if matrix[i] == 0:
            get_zero_index.append(i)
    random_zero_index = random.choice(get_zero_index)
    matrix[random_zero_index] = random.choice([2, 4])
    return matrix
 
def output(matrix):
    """
    print the matrix. return the matrix list
    """
    max_num_width = len(str(max(matrix)))
    demarcation = ( '+' + '-'*(max_num_width+2) ) * 4 + '+' #generate demarcation line like '+---+---+---+'
    print demarcation
    for i in range(len(matrix)):
        if matrix[i] == 0:
            printchar = ' '
        else:
            printchar = str(matrix[i])
        print '|', 
        print '{0:>{1}}'.format(printchar,max_num_width),
        if (i + 1) % 4 == 0:
            print '|'
            print demarcation
    print

def is_over(matrix):
    """is game over? return bool
    """
    if 0 in matrix:
        return False
    else:
        for i in range(16):
            if i % 4 != 3:
                if matrix[i] == matrix[i+1]:
                    return False
            if i < 12:
                if matrix[i] == matrix [i+4]:
                    return False
    return True
 
def play():
    matrix = init()
    matrix_stack = []
    matrix_stack.append(list(matrix))
 
    while True:
        output(matrix)
        if is_over(matrix) == False:
            if max(matrix) == 2048:
                input = raw_input('The max number is 2048, win the goal! q for quit, others for continue. ')
                if input == 'q':
                    exit()
            #while True:
            input = raw_input("which direction? u(p)/d(own)/l(eft)/r(ight), q for quit, b for back: ")
            if input in [ 'u', 'd', 'l', 'r' ]:
                matrix = move(matrix, input)
                insert(matrix)
                matrix_stack.append(list(matrix))
                #break
            elif input == 'b':
                if len(matrix_stack) == 1:
                    print 'Cannot back anymore...'
                    continue
                matrix_stack.pop()
                matrix = list(matrix_stack[-1])
                #break
            elif input == 'q':
                print 'Byebye!'
                exit()
            else:
                print 'Input error! Try again.'
        else:
            print 'Cannot move anyway. Game Over...'
            exit()

if __name__ == '__main__':
#    matrix = init()
#    output(matrix)
    play()