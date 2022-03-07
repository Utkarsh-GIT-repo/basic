# Given an integer N, print the corresponding stair pattern for N.

# For example if N = 4 then stair pattern will be like:

# *
# **
# ***
# ****

def main():
    star_pattern_input = int(input())
    for i in range(1,star_pattern_input+1):
        for j in range(i):
            print("*", end='')
        print()
    return 0

if __name__ == '__main__':
    main()
