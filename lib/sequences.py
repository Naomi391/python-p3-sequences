def print_fibonacci(length):
    fibonacci = []  # Initialize an empty sequence

    # Check if length is greater than 0
    if length > 0:
        fibonacci.append(0)  # Add the first Fibonacci number to the sequence
    if length > 1:
        fibonacci.append(1)  # Add the second Fibonacci number to the sequence

    # Generate subsequent Fibonacci numbers until desired length is reached
    while len(fibonacci) < length:
        next_number = fibonacci[-1] + fibonacci[-2]  # Generate the next Fibonacci number
        fibonacci.append(next_number)  # Add the next Fibonacci number to the sequence

    # Print the generated Fibonacci sequence
    print(fibonacci)


