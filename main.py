import random

MAX_LINES = 5
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbolCount = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            column.append(value)
            currentSymbols.remove(value)
        columns.append(column)

    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")
    print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def getNumOfLines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1 - " + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    
    return lines

def getBet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return amount

def main():
    balance = deposit()
    lines = getNumOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on ${lines} lines.\nYour current balance is ${balance} and your total bet is ${totalBet}")

    slots = getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)


main()



