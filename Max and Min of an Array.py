# Write a program to print maximum and minimum elements of the input array A of size N where you have to take integer N and other N elements as input from the user.

# A single line representing N (number of integers) followed by N integers of the array A

# Input 1:
# 5 1 2 3 4 5

# Output 1:
# 5 1

def main():
    inp = list(map(int, (input().split()))) #Read input as integer and store it in list
    inp.pop(0) #Remove teh first element which represents the number of elements in the list
    mx = max(inp) #Max value of the list
    mi = min(inp) #Min value of the list
    
    print(mx, mi, sep = ' ') #Print output in a single line
    return 0

if __name__ == '__main__':
    main()
