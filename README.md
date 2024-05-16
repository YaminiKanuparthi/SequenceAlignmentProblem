# SequenceAlignmentProblem

![image](https://github.com/YaminiKanuparthi/SequenceAlignmentProblem/assets/83491239/9dfc6bae-0aa0-4e11-93bf-39f5d829da5f)

Graph1 – Memory vs Problem Size (M+N)
![image](https://github.com/YaminiKanuparthi/SequenceAlignmentProblem/assets/83491239/b58d4b52-ebc8-4db4-9ec2-d00841e0a8ec)

Nature of the Graph (Logarithmic/ Linear/ Polynomial/ Exponential)

Basic: Exponential

Efficient: Linear 

Explanation:  

Basic Algorithm Memory Usage: The memory usage by the basic algorithm grows exponentially as the input size increases. This suggests that the algorithm's space complexity increases significantly with larger inputs, possibly due to recursive operations or extensive memory allocation that doubles at each step.

Efficient Algorithm Memory Usage: The efficient algorithm shows a near linear increase in memory usage as the input size grows. This indicates that the algorithm manages its memory in a way that is proportional to the input size, perhaps using iterative processes or efficient data structures that scale linearly.
The graph depicting memory usage indicates that as the problem size increases, the memory consumed by the basic algorithm (orange line) increases exponentially, while the memory consumed by the efficient algorithm (blue line) increases linearly.

The basic algorithm's exponential increase in memory usage suggests a naive implementation that scales poorly with input size. This is often seen in implementations that do not reuse memory efficiently or manage intermediate results suboptimally.

Conversely, the efficient algorithm's linear increase in memory usage implies that it effectively manages memory, possibly through in-place updates or by using more sophisticated data structures that grow proportionally with the input size. This efficient use of memory makes the algorithm more scalable and suitable for larger datasets, as it avoids the steep increase in resource demands that characterizes the basic algorithm.

Therefore, memory consumption in the efficient algorithm is significantly less compared to the basic algorithm.

Graph2 – Time vs Problem Size (M+N)

![image](https://github.com/YaminiKanuparthi/SequenceAlignmentProblem/assets/83491239/a7edbe7c-6c4e-4f29-b0f1-6b22f84e1892)

Nature of the Graph (Logarithmic/ Linear/ Polynomial/ Exponential)

Basic: Polynomial

Efficient: Linear

Explanation:

Basic Algorithm Time Consumed: The time consumed by the basic algorithm appears to increase polynomially as the input size increases. This polynomial growth could be indicative of nested loops which typically result in higher computation times as the input size expands.

Efficient Algorithm Time Consumed: The efficient algorithm demonstrates what appears to be constant time consumption across different input sizes. This remarkably stable performance suggests that the efficient algorithm’s execution time does not depend significantly on the input size, possibly due to optimizations or the use of advanced data structures that handle data more efficiently regardless of size.

In the graph, the x-axis represents the problem size (m + n), where m and n are the lengths of two strings being aligned. The y-axis shows the time consumed by the programs in milliseconds. The blue line depicts the time taken by the efficient algorithm, and the orange line represents the time taken by the basic algorithm.

Observing the graph, the time taken by the basic algorithm shows a polynomial growth as the problem size increases, which aligns with the
O(m×n) complexity expected from a traditional dynamic programming approach used in sequence alignment. This polynomial increase is due to the need to fill a matrix of size m by n, where each cell computation depends on the values of its neighboring cells.

On the other hand, the efficient algorithm, represented by the blue line, exhibits a nearly constant time across various input sizes. This indicates that the algorithm is leveraging advanced optimization techniques, in our case- DP with Divide and Conquer

