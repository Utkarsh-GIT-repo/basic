# Write a program to input an integer N from user and print the given number pattern.

# i/p = 4
# o/p :
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

def main():
    pattern_input = int(input())
    tri = 0
    for i in range(1,pattern_input+1):
        for j in range(i):
            tri = tri+1
            print(tri, end= " ")
        print()
    return 0

if __name__ == '__main__':
    main()
