#You are given a Bank account having N amount and you are asked to perfrom ADD(credit) and SUBTRACT(debit) operations.
#After each operation print the amount left in the Bank account. 
#If the debit amount is greater than current balance print "Insufficient Funds"(without quotes) and the operation is skipped.

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    bank_bal = int(input())
    num_of_operations = int(input())
    for i in range(num_of_operations):
        op_type, amt = input().split(' ')
        if int(op_type) == 1:
            bank_bal = bank_bal + int(amt)
            print(bank_bal)
        else:
            
            if bank_bal - int(amt) < 0 :
                print("Insufficient Funds")
            else:
                bank_bal = bank_bal - int(amt)
                print(bank_bal)
    return 0

if __name__ == '__main__':
    main()
