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

