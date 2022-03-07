# Write a program to input an integer N from user and print hollow inverted right triangle star pattern of N lines using '*'.

# Input Format
# First line is an integer N

# Output Format
# N lines conatining only char '*' as per the question.

# Input :
# 7

# Output :
# *******
# *    *
# *   *
# *  *
# * *
# **
# *

def main():
    ht = int(input())
    print('*'*ht , end = '')   #print first line
    print()
    for i in range (ht-1,0,-1): #Reverse Loop
        j = i-2   #Number of spaces will always be loop -2
        if j == 0:    #Check for second last instance, as it will always be **
            print('**')    
        elif j > 0:
            print('*'+" "*j+'*')  #Print pattern with required space
    print('*')     #print last line
    return 0

if __name__ == '__main__':
    main()
