# Given an integer N, print the corresponding Full Numeric Pyramid pattern for N.

# For example if N = 5 then pattern will be like:

# 0 0 0 0 1 0 0 0 0 
# 0 0 0 2 3 2 0 0 0 
# 0 0 3 4 5 4 3 0 0
# 0 4 5 6 7 6 5 4 0
# 5 6 7 8 9 8 7 6 5 

# NOTE: There should be exactly one extra space after each number for each row.

def main():
    fnp = int(input())   #Capture the input from user, which will be the depth of the pyramid
    for i in range(1, fnp+1): #Initialize the vertical depth of the pyramid
        zer = (fnp - i) #Inialize the Zeros to be printed
        print(zer*'0 ',end = '' ) #As the number of '0' will be identical on the LHS and RHS, printing the zeros on LHS
        for j in range(i, (2*i)):  #The max (center of the pyramid) number goes till 2N-1
            print(j, end = ' ')     #Printing the LHS of the FNP(Full Numeric Pyramid)
        for z in range(j,i,-1):  #Decending loop for the right side of the pyramid
            print(z-1, end = ' ') #Printing the RHS of the pyramid
        print(zer*'0 ',end = '' ) #As the number of '0' will be identical on the LHS and RHS, printing the zeros on RHS
        print() #Setting the cursor to a New line
    return 0

if __name__ == '__main__':
    main()
