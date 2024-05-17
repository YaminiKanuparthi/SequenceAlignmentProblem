import matplotlib.pyplot as plt
import os
import re

def read_file(file):
    total_length = 0
    memory = 0
    time_taken = 0

    lines = file.readlines()
    for line_index, line in enumerate(lines):
        line = line.strip()  # Remove trailing newline characters
        if line_index > 0 and line_index < 3:
            total_length += len(line.replace('_', ''))
        elif line_index == 3:
            time_taken = float(line)
        elif line_index == 4:
            memory = float(line)

    return total_length, memory, time_taken

basic_memory = []
basic_time = []
efficient_memory = []
efficient_time = []
length = []

basic_output_file = open("C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/basic_output.csv", 'w')
efficient_output_file = open("C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/efficient_output.csv", 'w')

# Processing basic algorithm output files
basic_files = os.listdir("C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/Basic/")
basic_files.sort(key=lambda f: int(re.sub('\D', '', f)))
for file in basic_files:
    print("Processing file:", file)
    with open("C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/Basic/" + file, 'r') as f:
        total_length, bt, bm = read_file(f)
        basic_memory.append(bm)
        basic_time.append(bt)
        length.append(total_length)
        print("Basic algorithm output:", total_length, bt, bm)
        basic_output_file.write(str(total_length) + "," + str(bm) + "," + str(bt) + '\n')

# Processing efficient algorithm output files
efficient_files = os.listdir("C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/NE/")
efficient_files.sort(key=lambda f: int(re.sub('\D', '', f)))
for file in efficient_files:
    print("Processing file:", file)
    with open("C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/NE/" + file, 'r') as f:
        total_length, et, em = read_file(f)
        efficient_memory.append(em)
        efficient_time.append(et)
        print("Efficient algorithm output:", total_length, et, em)
        efficient_output_file.write(str(total_length) + "," + str(em) + "," + str(et) + '\n')

print("Length:", len(length))
print("Efficient Time:", len(efficient_time))

if len(length) != len(efficient_time):
    print("Error: Lengths of 'length' and 'efficientTime' lists do not match.")

# Plotting time consumed vs. input size
fig1 = plt.figure(figsize=(10,6))
plt.plot(length, efficient_time)
plt.plot(length, basic_time)
plt.legend(['Efficient algorithm time consumed', 'Basic algorithm time consumed'])
plt.xlabel('Total length of string (m+n)')
plt.ylabel('Time consumed (ms)')
plt.title('Input Size vs Time Consumed')
plt.grid()
plt.savefig('C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/time_comparison.png')

# Plotting memory usage vs. input size
fig2 = plt.figure(figsize=(10,6))
plt.plot(length, efficient_memory)
plt.plot(length, basic_memory)
plt.legend(['Efficient algorithm memory usage', 'Basic algorithm memory usage'])
plt.xlabel('Total length of string (m+n)')
plt.ylabel('Memory usage (KB)')
plt.title('Input Size vs Memory Consumed')
plt.grid()
plt.savefig('C:/Users/tanay/Desktop/Algos/Project/Project/DP_output/memory_comparison.png')
