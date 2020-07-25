Please answer the following questions:

1. What is the difference between a list and a set?
    - A list is an ordered data structure where the elements can be accessed directly through an index
    - A set is unordered (elements cannot be accessed by index) and every element can only appears once

2. What ways of achieving concurrency do you know? What are the limitations of those ways?
    - I have not explicitly implemented concurrency by hand before in python. 
    When using libraries like tensorflow or scipy, I noticed that they are automatically running on multiple
    cores or make use of the GPU (when the device is properly assigned)
    - In order to still answer your question I checked online and found an interesting article on 
    https://towardsdatascience.com/concurrency-in-python-e770c878ab53
    - After going through the article, I implemented the computation of an integral to test the ideas (I chose an
    integral because I can easily adjust the computational load by changing the number of intervals, and I can verify
    the result of the computation)
    - To guarantee that there is no uncontrolled concurrent access to mutable data, there is the Global Interpreter Lock
    (GIL) in python. This allows only one thread to run at any time. 
    - When using the multiprocessing library, we can create several processes which will be executed on the different 
    cores of the given CPU. Currently I am using a laptop with 8 cores, so I would expect a speedup of this CPU heavy
    computation to be roughly eightfold.
    - I will add the results directly in the respective files in [this folder](./concurrency)

3. What is the worst case time complexity of a quick sort?
    - For quick sort the input is split into two parts based on a 'randomly' selected pivot point.
    If this pivot is either the smallest or largest element (for all choices), we end up doing this (n-1) times.
    Eventually this means the worst case time complexity is O(n²)

4. What is an eigenvalue and an eigenvector?
    - Given a linear transformation, an eigenvector is a vector that remains essentially unchanged by the 
    transformation, i.e. up to a scalar factor. This factor is the eigenvalue. With the linear transformation A,
    the eigenvector v, and the eigenvalue $\lambda$, we have: $Av = \lambda v$.

5. For a given linked list containing the first 100 numbers of the sequence: 
0, 1, 1, 2, 3, 5, 8, 13,...,218922995834555200000, provide a solution that returns a linked list in the following order:
218922995834555200000, ..., 13, 8, 5, 3, 2, 1, 1, 0. Please do not rely on standard packages for queues.
    - Given the first eight elements I assumed the question is referring to the Fibonacci sequence, but during testing
    I realised that the final value does not match. As it is fairly close to the 100th number in my list this might be
    due to a rounding error / casting between different data types, so I continued with the Fibonacci sequence.
    - I implemented the linked list [here](./linkedList.py)