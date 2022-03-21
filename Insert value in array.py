# Write a program to input N numbers array from user and insert an element Y in it at specified position X.
# First line is N which means number of elements.
# Second line contains N space separated integers.
# Third line is X position where Y has to be inserted.
# Fourth line is Y which has to be inserted.

# Input 1:
# 5
# 2 3 1 4 2
# 3
# 5

# Example Output
# Output 1:
# 2 3 5 1 4 2

def main():
    inp = input()  #Input First line as per problem statement
    li = input().split()  #Input second line and create it as a list 
    posi = int(input()) #Input third line as per problem statement
    ins_v = (input()) #Input forth line as per input statement
    posi -= 1 #Decreasing the value of position(Input 3) by 1, to keep the data within list indexes
    li.insert(posi,ins_v) #nsert the data in list at defined position
    print(' '.join(li),end = ' ') #Printing the output in single line.
    return 0

if __name__ == '__main__':
    main()
