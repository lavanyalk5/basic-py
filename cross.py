def print_cross_mark(n):
    # Check if the input number is odd
    if n % 2 == 0:
        print("Please enter an odd number.")
        return
    
    for i in range(n):
        for j in range(n):
            # Condition to print '*' for cross mark
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Input from the user
n = int(input("Enter an odd number for the size of the cross mark: "))
print_cross_mark(n)