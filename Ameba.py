'''
The environmental eco club has discovered a new Amoeba that grows in the order of a Fibonacci series every month.
They are exhibiting their amoeba in a national conference. They want to know the size of the amoeba at a particular time instant.
If a particular month’s index is given, write a  program to displays the amoeba’s size……???. 
For Example, The size of the amoeba on month 1, 2, 3, 4, 5, 6, ..will be 0, 1, 1, 2, 3, 5, 8 respectively.
Input format:
The first input containing an integer which denotes the number of the month
Output format:
Print the amoeba size.
Refer the sample output for formatting.
Sample Input:
7
Sample Output:
8
Ans:
'''
n=int(input())
a=0
b=1
for i in range (3,n+1):
	c=a+b
	a=b
	b=c
print (c)
