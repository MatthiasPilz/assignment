Please answer the following questions:

1. What is the difference between a list and a set?
    - A list is an ordered data structure where the elements can be accessed directly through an index
    - A set is unordered (elements cannot be accessed by index) and every element can only appears once

2. What ways of achieving concurrency do you know? What are the limitations of those ways?
    - I have not explicitly implemented concurrency by hand before in python. 
    When using libraries like tensorflow or scipy, I noticed that they are automatically running on multiple
    cores or make use of the GPU (when the device is properly assigned)

3. What is the worst case time complexity of a quick sort?

4. What is an eigenvalue and an eigenvector?

5. For a given linked list containing the first 100 numbers of the sequence: 
0, 1, 1, 2, 3, 5, 8, 13,...,218922995834555200000, provide a solution that returns a linked list in the following order:
218922995834555200000, ..., 13, 8, 5, 3, 2, 1, 1, 0. Please do not rely on standard packages for queues.