# Given an integer N, print the corresponding Numeric Inverted Half Pyramid pattern for N.

# For example if N = 4 then pattern will be like:

# 1 2 3 4
# 1 2 3
# 1 2
# 1

# NOTE: There should be no extra spaces after last integer and before first integer in any row and all integers in any row in the pattern are space separated.

def main():
    inv_tri = int(input())  #User input
    for s in range(inv_tri): #Initialize a loop for vertical pattern
        for i in range(1,inv_tri+1): #Initializez a loop from 1 to current val of User Input variable
            print(i, end = '') #Printing the pattern
            if i != inv_tri: #As per note, the space should only be between the numbers, no extra space in the end
                print(" ",end = '') 
        print()
        inv_tri = inv_tri -1  #Decresing the value of User Input variable by 1
    return 0

if __name__ == '__main__':
    main()
