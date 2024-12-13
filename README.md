# Slot Machine Game

## Project Overview
This project implements a simple **Slot Machine Game** using Python. The game allows players to deposit money, place bets on multiple lines, and spin the slot machine to reveal randomized results. Players must manage their balance while making bets and playing responsibly.

---

## Features
- **User Deposits**: Allows players to deposit funds into their account before playing.
- **Line Betting**: Players can choose how many lines (up to a maximum) to bet on.
- **Flexible Betting Amounts**: Players can bet within a specified range per line.
- **Slot Machine Simulation**: Randomized spins based on symbol probabilities.
- **Dynamic Display**: The slot machine results are displayed in a formatted grid.

---

## Rules
1. Players must deposit money before starting the game.
2. Players can bet on up to `MAX_LINES` lines.
3. Betting amounts must be between `MIN_BET` and `MAX_BET`.
4. The total bet cannot exceed the player's available balance.

---

## Symbol Distribution
The symbols have varying probabilities of appearing in a column:
- `A`: Appears 2 times.
- `B`: Appears 4 times.
- `C`: Appears 6 times.
- `D`: Appears 8 times.

The more a symbol appears, the higher the chance it will be selected.

---

## How to Play
1. Run the script.
2. Enter the amount you want to deposit.
3. Choose the number of lines to bet on (1–`MAX_LINES`).
4. Place a bet per line within the allowed range (`MIN_BET`–`MAX_BET`).
5. View the slot machine results and your remaining balance.

---

## File Structure
The game script is self-contained in a single Python file.

### Key Functions
1. `deposit()`: Handles user deposits.
2. `getNumOfLines()`: Asks the user for the number of lines to bet on.
3. `getBet()`: Prompts the user to input a bet amount per line.
4. `getSlotMachineSpin(rows, cols, symbols)`: Simulates a slot machine spin based on symbol distribution.
5. `printSlotMachine(columns)`: Displays the slot machine results in a formatted grid.
6. `main()`: Manages the game flow.

---

## Requirements
- Python 3.x
- No external libraries required (uses the `random` module from Python’s standard library).

---

## Customization
You can adjust the following constants to modify the game:
- `MAX_LINES`: Maximum number of lines a player can bet on.
- `MIN_BET`: Minimum allowed bet per line.
- `MAX_BET`: Maximum allowed bet per line.
- `ROWS` and `COLS`: Dimensions of the slot machine grid.
- `symbolCount`: Adjust the distribution of symbols for different probabilities.

---

## Example Gameplay
1. **Deposit Money**:  
   *Input*: `$50`  
   *Output*: "You have deposited $50."

2. **Choose Lines**:  
   *Input*: `3`  
   *Output*: "You are betting on 3 lines."

3. **Place Bet**:  
   *Input*: `$5`  
   *Output*: "Your total bet is $15. Current balance: $35."

4. **View Results**:  



---

## Future Enhancements
- Add winnings calculation based on matching patterns.
- Implement a balance update after each spin.
- Add more symbols and custom winning rules.
- Allow players to continue playing until their balance reaches zero.

---

Have fun playing the Slot Machine Game responsibly! 🎰
