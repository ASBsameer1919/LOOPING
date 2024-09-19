'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''
# Input
n = int(input())

# Initialize variables
factorial = 1
i = 1

# Check if n is a factorial number
while factorial < n:
    i += 1
    factorial *= i

# Output
if factorial == n:
    print("Yes")
else:
    print("No")
