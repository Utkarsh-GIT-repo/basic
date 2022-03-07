# Write a program to input an integer T and then T lines each containing two integers A & B from user and print T lines conatining HCF of two given 2 numbers A and B.

#Input format
# First line is T which means number of test cases.
# Each next T lines contain two integers A &B.

# Output Format
# T lines each containing an integer representing HCF of A & B.

# Input 1:
# 2
# 15 105 
# 24 36

# Output 1:
# 15
# 12

def main():
    ip = int(input())
    for i in range(ip):
        first,second = input().split()
        first = int(first)
        second = int(second)
        li = []
        for j in range(1,min(first,second)+1):
            if first % j == 0 and second % j == 0:
                li.append(j)
        print(max(li) )
    return 0

if __name__ == '__main__':
    main()
