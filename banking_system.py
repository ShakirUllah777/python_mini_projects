accounts = []        # list of account ids (integers)
names = []           # list of account holder names
balances = []        # list of balances (floats)
pins = []            # list of numeric PINs (integers)
next_id = 1

def find_index_by_id(acc_id):
    i = 0
    while i < len(accounts):
        if accounts[i] == acc_id:
            return i
        i += 1
    return -1

def authenticate(acc_id, pin):
    idx = find_index_by_id(acc_id)
    if idx == -1:
        return -1
    if pins[idx] == pin:
        return idx
    return -1

while True:
    print('\nMenu:')
    print('1. Create account')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transfer')
    print('5. Check balance')
    print('6. List accounts')
    print('7. Exit')
    choice = input('Choose an option (1-7): ')

    if choice == '1':
        name = input('Name: ')
        pin_input = input('Choose a 4-digit PIN (numbers only): ')
        try:
            pin = int(pin_input)
        except:
            print('Invalid PIN. Use numbers only.')
            continue
        init_input = input('Initial deposit (or 0): ')
        try:
            init = float(init_input)
        except:
            print('Invalid amount.')
            continue
        accounts.append(next_id)
        names.append(name)
        balances.append(init)
        pins.append(pin)
        print('Account created. Your account id is', next_id)
        next_id += 1

    elif choice == '2':
        try:
            acc = int(input('Account id: '))
            pin = int(input('PIN: '))
        except:
            print('Invalid input.')
            continue
        idx = authenticate(acc, pin)
        if idx == -1:
            print('Authentication failed.')
            continue
        try:
            amt = float(input('Amount to deposit: '))
        except:
            print('Invalid amount.')
            continue
        if amt <= 0:
            print('Enter a positive amount.')
            continue
        balances[idx] = balances[idx] + amt
        print('Deposit successful. New balance:', balances[idx])

    elif choice == '3':
        try:
            acc = int(input('Account id: '))
            pin = int(input('PIN: '))
        except:
            print('Invalid input.')
            continue
        idx = authenticate(acc, pin)
        if idx == -1:
            print('Authentication failed.')
            continue
        try:
            amt = float(input('Amount to withdraw: '))
        except:
            print('Invalid amount.')
            continue
        if amt <= 0:
            print('Enter a positive amount.')
            continue
        if amt > balances[idx]:
            print('Insufficient funds.')
            continue
        balances[idx] = balances[idx] - amt
        print('Withdrawal successful. New balance:', balances[idx])

    elif choice == '4':
        try:
            from_acc = int(input('Your account id: '))
            pin = int(input('Your PIN: '))
            to_acc = int(input('Recipient account id: '))
        except:
            print('Invalid input.')
            continue
        idx_from = authenticate(from_acc, pin)
        if idx_from == -1:
            print('Authentication failed.')
            continue
        idx_to = find_index_by_id(to_acc)
        if idx_to == -1:
            print('Recipient account not found.')
            continue
        try:
            amt = float(input('Amount to transfer: '))
        except:
            print('Invalid amount.')
            continue
        if amt <= 0:
            print('Enter a positive amount.')
            continue
        if amt > balances[idx_from]:
            print('Insufficient funds.')
            continue
        balances[idx_from] = balances[idx_from] - amt
        balances[idx_to] = balances[idx_to] + amt
        print('Transfer successful.')

    elif choice == '5':
        try:
            acc = int(input('Account id: '))
            pin = int(input('PIN: '))
        except:
            print('Invalid input.')
            continue
        idx = authenticate(acc, pin)
        if idx == -1:
            print('Authentication failed.')
            continue
        print('Account:', accounts[idx])
        print('Name:', names[idx])
        print('Balance:', balances[idx])

    elif choice == '6':
        print('All accounts:')
        i = 0
        while i < len(accounts):
            print('ID:', accounts[i], 'Name:', names[i], 'Balance:', balances[i])
            i += 1

    elif choice == '7':
        print('Goodbye.')
        break

    else:
        print('Invalid choice. Enter 1-7.')
