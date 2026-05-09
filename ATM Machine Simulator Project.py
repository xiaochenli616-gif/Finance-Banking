initial_amount = 5000
print('Welcome to the ATM!')
print('What would you like to do?')


while True:
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    question = int(input('Enter your choice:'))
    if question not in [1,2,3,4]:
        print('Please enter a valid option!')
        continue
    if question == 1:
        print(f'Your current balance is ${initial_amount:,.2f} ')
    elif question == 2:
        deposit_amount = int(input('Enter deposit amount: $'))
        if deposit_amount < 0:
            print('That is for withdrawn')
            continue
        current_amount = initial_amount + deposit_amount
        print(f'Successfully deposited ${deposit_amount:,.2f}! Your new balance is ${current_amount:,.2f}')
        initial_amount = current_amount
    elif question == 3:
        withdraw_amount = int(input('Enter withdraw amount: $'))
        if withdraw_amount < 0:
            print('Withdraw amount cannot be negative')
            continue
        elif withdraw_amount > initial_amount:
            print('Balance not enough for withdrawn!')
            continue
        current_amount = initial_amount - withdraw_amount
        print(f'Successfully withdrew ${withdraw_amount:,.2f}! Your new balance is ${current_amount:,.2f}')
        initial_amount = current_amount
    elif question == 4:
        break

print('Thank you for using our ATM. Goodbye!')