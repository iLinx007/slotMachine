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

symbolValues = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def checkWinninigs(columns, lines, bet, values):
    winnings = 0
    winnningLines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symb_to_check = column[line]
            if symbol != symb_to_check:
                break
        else:         
            winnings += values[symbol]*bet
            winnningLines.append(line+1)
    
    return winnings, winnningLines


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
        lines = input("Enter the number of lines you want to bet on (1 - " + str(min(MAX_LINES, ROWS)) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= min(MAX_LINES, ROWS):
                break
            else:
                print(f"Enter a valid number of lines (1 - {min(MAX_LINES, ROWS)}).")
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
    
def game(balance):
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
    winnings, winningLines = checkWinninigs(slots, lines, bet, symbolValues)
    print(f"You won ${winnings}.")
    print(f"You won on lines", *winningLines)

    return winnings - totalBet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        response = input("Press enter to play (q to quit).")
        if response == 'q':
            break
        balance += game(balance)

    print(f"You left with ${balance}.")

main()



