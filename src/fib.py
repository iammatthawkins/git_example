def fibonacci(n_iterations):
    """This function takes an integer and returns a list of that length of the fibonacci sequence"""

    if isinstance(n_iterations, (int)) == False:
        print('Please supply an integer')
        return []
    elif n_iterations < 1:
        print('Please supply a positive integer')
        return []

    fib_seq = [1, 1]

    if n_iterations == 1:
        return [1]
    elif n_iterations > 2:
        for i in range(2, n_iterations):
            a, b = fib_seq[i - 2], fib_seq[i - 1]
            c = a + b
            fib_seq.append(c)
        
    print(fib_seq)
    return fib_seq

fibonacci(10)