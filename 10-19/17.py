"""
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

def bank():
    balance = 0
    while True:
        user_input = input("Please provide an event (D/W) and amount, B for Balance or Q to QUIT: ").split()
        if user_input[0].upper() == 'Q':
            print(f'Quitting...')
            break

        elif user_input[0].upper() == 'B':
            print(f'Your BALANCE is {balance}')

        elif user_input[0].upper() == 'D':
            amount = int(user_input[1])
            balance += amount
            print(f'You Depositted {amount} and current balance {balance}')


        elif user_input[0].upper() == 'W':
            amount = int(user_input[1])
            if balance - amount >= 0:
                balance -= amount
                print(f'You Withdrawed {amount} and current balance {balance}')

            else:
                print('Insufficient funds')
        
        else:
            print("I didn't understand")
    

bank()