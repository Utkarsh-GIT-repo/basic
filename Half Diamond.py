# Given an integer N, print the corresponding Half Diamond pattern with 2*N - 1 rows.

# For example if N = 5 then pattern will be like:

# * 
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# NOTE: There should be no spaces after any * .

def main():
    inp = int(input())  #User input to capture the depth of pyramid
    for i in range(1, inp+1): #As the loop is initialized from 1, so inp+1 is the higher limit of the range.
        print(i*'*') #Print the top halp of the pyramid
    for j in range(inp-1, 1,-1): #Initiate a reverse loop, starting from max width -1 to 0
        print(j*'*') #Print the bottom half of the pyramid
    print('*') #Print the last row
    return 0

if __name__ == '__main__':
    main()
