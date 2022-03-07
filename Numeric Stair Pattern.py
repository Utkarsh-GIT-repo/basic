# Given an integer N, print the corresponding pattern for N.

# For example if N = 4 then pattern will be like:

# 1
# 1 2
# 1 2 3
# 1 2 3 4

def main():
    input_num = int(input())
    for i in range(1,input_num+1):
        for j in range(1, i+1):
            print(j, end='')
            if i != j:
                print(" ", end='')
        print()
    return 0

if __name__ == '__main__':
    main()
