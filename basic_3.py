#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import time
import psutil
import numpy as np

gap_cost = 30

mismatch_costs = np.array([[0, 110, 48, 94],[110, 0, 118, 48],[48, 118, 0, 110],[94, 48, 110, 0]])

def encode(n):
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return mapping.get(n, -1)

def string_input(strings, idx_list):
    s1 = strings[0]
    s2 = strings[1]
    ia = idx_list[0]
    ib = idx_list[1]

    for i in range(len(ia)):
        s1 = s1[:ia[i] + 1] + s1 + s1[ia[i] + 1:]

    for j in range(len(ib)):
        s2 = s2[:ib[j] + 1] + s2 + s2[ib[j] + 1:]

    return s1, s2

def align(s1, s2):
    lx, ly = len(s1), len(s2)
    opt = np.zeros((ly + 1, lx + 1), dtype=int)

    for j in range(lx + 1):
        opt[0][j] = gap_cost * j
    for i in range(ly + 1):
        opt[i][0] = gap_cost * i

    for i in range(1, ly + 1):
        for j in range(1, lx + 1):
            opt[i][j] = min(opt[i - 1][j] + gap_cost,
                            opt[i][j - 1] + gap_cost,
                            opt[i - 1][j - 1] + mismatch_costs[encode(s1[j - 1]), encode(s2[i - 1])])

    s1_point = lx
    s2_point = ly
    aligned_X = ''
    aligned_Y = ''

    while (s1_point > 0 and s2_point > 0):
        if (opt[s2_point - 1, s1_point - 1] + mismatch_costs[encode(s1[s1_point - 1]), encode(s2[s2_point - 1])] == opt[s2_point][s1_point]):
            aligned_X = s1[s1_point - 1] + aligned_X
            aligned_Y = s2[s2_point - 1] + aligned_Y
            s1_point -= 1
            s2_point -= 1
        elif (opt[s2_point - 1][s1_point] + gap_cost == opt[s2_point][s1_point]):
            aligned_X = '_' + aligned_X
            aligned_Y = s2[s2_point - 1] + aligned_Y
            s2_point -= 1
        else:
            aligned_Y = '_' + aligned_Y
            aligned_X = s1[s1_point - 1] + aligned_X
            s1_point -= 1

    while s1_point > 0:
        aligned_X = s1[s1_point - 1] + aligned_X
        aligned_Y = '_' + aligned_Y
        s1_point -= 1

    while s2_point > 0:
        aligned_X = '_' + aligned_X
        aligned_Y = s2[s2_point - 1] + aligned_Y
        s2_point -= 1

    return opt, aligned_X, aligned_Y

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as infile:
        input_data = infile.read().split('\n')

    strings = []
    numbers = [[], []]

    for item in input_data:
        if item.isalpha():
            strings.append(item)
        elif item.isnumeric():
            if len(strings) == 1:
                numbers[0].append(int(item))
            else:
                numbers[1].append(int(item))

    s1, s2 = string_input(strings, numbers)

    start_time = time.time()
    process = psutil.Process()
    
    opt, aligned_X, aligned_Y = align(s1, s2)

    end_time = time.time()
    time_taken = (end_time - start_time) * 1000
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)

    with open(output_file, "w") as outfile:
        outfile.write(str(opt[-1, -1]) + '\n')
        outfile.write(aligned_X + '\n')
        outfile.write(aligned_Y + '\n')
        outfile.write(str(time_taken) + '\n')
        outfile.write(str(memory_consumed))

if __name__ == "__main__":
    main()

