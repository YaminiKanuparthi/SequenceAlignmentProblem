import sys
import time
import psutil

mismatch_costs = {
    'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94},
    'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
    'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
    'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}
}

gap_cost = 30

class SequenceAlignment:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_input(self):
        with open(self.input_file, 'r') as infile:
            input_data = infile.read().split('\n')
        return input_data

    def write_output(self, output_data):
        with open(self.output_file, "w") as outfile:
            outfile.write('\n'.join(output_data))

    def process_input(self, input_data):
        strings = []
        insertion_points = [[], []]

        for item in input_data:
            if item.isalpha():
                strings.append(item)
            elif item.isnumeric():
                if len(strings) == 1:
                    insertion_points[0].append(int(item))
                else:
                    insertion_points[1].append(int(item))

        return strings, insertion_points

    def generate_strings(self, input_strings, insertion_points):
        string1 = input_strings[0]
        string2 = input_strings[1]
        insertion_points1 = insertion_points[0]
        insertion_points2 = insertion_points[1]

        for i in insertion_points1:
            string1 = string1[:i + 1] + string1 + string1[i + 1:]

        for j in insertion_points2:
            string2 = string2[:j + 1] + string2 + string2[j + 1:]

        return string1, string2

    def dynamic_programming_alignment(self, string1, string2):
        length1 = len(string1)
        length2 = len(string2)
        dp = [[0] * (length1 + 1) for _ in range(length2 + 1)]

        for j in range(length1 + 1):
            dp[0][j] = gap_cost * j

        for i in range(length2 + 1):
            dp[i][0] = gap_cost * i

        for i in range(1, length2 + 1):
            for j in range(1, length1 + 1):
                dp[i][j] = min(dp[i - 1][j] + gap_cost,
                               dp[i][j - 1] + gap_cost,
                               dp[i - 1][j - 1] + mismatch_costs[string1[j - 1]][string2[i - 1]])

        aligned1, aligned2 = '', ''
        p1, p2 = length1, length2

        while p1 > 0 and p2 > 0:
            if dp[p2][p1] == dp[p2 - 1][p1 - 1] + mismatch_costs[string1[p1 - 1]][string2[p2 - 1]]:
                aligned1 = string1[p1 - 1] + aligned1
                aligned2 = string2[p2 - 1] + aligned2
                p1 -= 1
                p2 -= 1
            elif dp[p2][p1] == dp[p2][p1 - 1] + gap_cost:
                aligned1 = string1[p1 - 1] + aligned1
                aligned2 = '_' + aligned2
                p1 -= 1
            else:
                aligned1 = '_' + aligned1
                aligned2 = string2[p2 - 1] + aligned2
                p2 -= 1

        while p1 > 0:
            aligned1 = string1[p1 - 1] + aligned1
            aligned2 = '_' + aligned2
            p1 -= 1

        while p2 > 0:
            aligned1 = '_' + aligned1
            aligned2 = string2[p2 - 1] + aligned2
            p2 -= 1

        return dp, aligned1, aligned2

    def find_alignment(self, string1, string2):
        length1, length2 = len(string1), len(string2)
        dp = [[0] * (length1 + 1) for _ in range(2)]

        for j in range(length1 + 1):
            dp[0][j] = gap_cost * j

        for i in range(1, length2 + 1):
            dp[1][0] = gap_cost * i
            for j in range(1, length1 + 1):
                dp[1][j] = min(dp[0][j] + gap_cost,
                               dp[1][j - 1] + gap_cost,
                               dp[0][j - 1] + mismatch_costs[string1[j - 1]][string2[i - 1]])

            dp[0] = dp[1][:]

        return dp[-1]

    def divide_and_conquer_alignment(self, string1, string2):
        length1, length2 = len(string1), len(string2)

        if length1 <= 2 or length2 <= 2:
            return self.dynamic_programming_alignment(string1, string2)[1:]

        left_mid = length2 // 2
        right_mid = length1 // 2

        left_align = self.find_alignment(string1, string2[:left_mid])
        right_align = self.find_alignment(string1[::-1], string2[left_mid:][::-1])[::-1]

        min_sum = float('inf')
        split_point = 0

        for i in range(len(right_align)):
            sum_score = left_align[i] + right_align[i]
            if sum_score <= min_sum:
                min_sum = sum_score
                split_point = i

        left_part = string1[:right_mid - split_point]
        right_part = string1[right_mid - split_point:]

        left_result = self.divide_and_conquer_alignment(left_part, string2[:left_mid])
        right_result = self.divide_and_conquer_alignment(right_part, string2[left_mid:])

        return left_result[0] + right_result[0], left_result[1] + right_result[1]

    def run_alignment(self):
        input_data = self.read_input()
        strings, insertion_points = self.process_input(input_data)
        s1, s2 = self.generate_strings(strings, insertion_points)

        start_time = time.time()
        process = psutil.Process()

        alignment_results = self.divide_and_conquer_alignment(s1, s2)

        end_time = time.time()
        time_taken = (end_time - start_time) * 1000
        memory_info = process.memory_info()
        memory_consumed = int(memory_info.rss / 1024)

        output_data = [
            str(self.find_alignment(s1, s2)[-1]),
            alignment_results[0],
            alignment_results[1],
            str(time_taken),
            str(memory_consumed)
        ]

        self.write_output(output_data)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    alignment = SequenceAlignment(input_file, output_file)
    alignment.run_alignment()

if __name__ == "__main__":
    main()
