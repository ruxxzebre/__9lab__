author = "Chaikovskyi Pavlo"

from random import randint
#import pickle
import numpy as np
import time
from operator import gt, lt, ge, le
# gt - ">" , ge - ">="
# lt - "<" , le - "<="

def time_check(func):
    def wrapper(*args, **kwargs):
        start = time.time ()
        return_value = func (*args, **kwargs)
        end = time.time ()
        print (f"Execution time : {end - start}")
        return return_value
    return wrapper

@time_check
def sort_bubble(a, ascending=True):
    count_comp = 0
    count_switch = 0
    op = lt if ascending else gt
    for i in range(len(a)):
        for j in range (len (a) - i - 1):
            if op(a[j + 1], a[j]):
                a[j], a[j + 1] = a[j + 1], a[j]
                count_switch += 1
            count_comp += 1
    return (count_comp, count_switch)

@time_check
def sort_selection(a, ascending=True):
    count_comp = 0
    count_switch = 0
    op = ge if ascending else le
    for i in range(0, len(a)):
        temp = a[i]
        for j in a[i::]:
            if op(j, temp):
                count_switch += 1
                temp = j
            count_comp += 1
        a.remove(temp)
        a.insert(0, temp)
    return (count_comp, count_switch)

@time_check
def sort_insertion(a, ascending=True):
    count_comp = 0
    count_switch = 0
    op = lt if ascending else gt
    for i in range (1, len (a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and op(temp, a[j]):
            count_comp += 1
            count_switch += 1
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    return (count_comp, count_switch)

if __name__ == '__main__':
    sort_funcs = ['sort_bubble', 'sort_selection', 'sort_insertion']

    while True:
        a = int(input("Bubble, selection, insertion? 0,1,2 : "))
        b = bool(int(input("Ascending/descending order? 1, 0 : ")))
        if a in (0,1,2):
            break


    if input('Generate rand array, or input from keyboard? y/n ') == 'y':
        lenA = int(input("Array's length? : "))
        minA = int(input("Minimum value : "))
        maxA = int(input("Maximum value : "))
        array = np.random.randint(minA, maxA, lenA)

        print('Array\n : ' , array)
        eval(f"{sort_funcs[a]}(array, ascending={b})")
        print ('Sorted array\n : ', array)
    else:
        array = list(map(int, input("Enter some values here :\n").split()))
        np_array = np.asarray(array)
        print ('Array\n : ', array)
        counts = eval (f"{sort_funcs[a]}(array)")
        print ('Sorted array\n : ', array)
        print(f'Comparisons {counts[0]}, swaps {counts[1]}')
