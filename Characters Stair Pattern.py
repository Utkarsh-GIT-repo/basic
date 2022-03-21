# Given an integer N, print the corresponding pattern for N.

# For example if N = 4 then pattern will be like:

# A
# B B
# C C C
# D D D D

# Output the pattern corresponding to the given N.

# NOTE: There should be no extra spaces after last character or before first character in any row and all characters in any row in the pattern are space separated.

def main():
    x = int(input())  #Read the Depth of pyramid
    av = 64   #Ascii value of capital letters starts from 64
    for i in range(1, x+1): #Initiate vertival loop
        for j in range(1,i+1): #Initiate horizontal loop
            print(chr(av+i),end = '' ) #Print the ASCII Value of the loop variable
            if i!=j: #To make sure there is no extra space after the last character(as mentioned in the notes)
                print(" ", end = '')
        print() #Move the controller to the next line
    return 0

if __name__ == '__main__':
    main()
