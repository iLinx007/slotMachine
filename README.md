# 🎰 Slot Machine Game

## 🌟 Project Overview
This project implements a simple **Slot Machine Game** using Python. The game allows players to:
- 💰 Deposit money.
- 🎲 Place bets on multiple lines.
- 🎡 Spin the slot machine to reveal randomized results.

Players must manage their balance while making bets and playing responsibly.

---

## ✨ Features
- 💵 **User Deposits**: Allows players to add funds to their account.
- 🔢 **Line Betting**: Choose up to `MAX_LINES` lines to bet on.
- 🎯 **Flexible Betting Amounts**: Bet within a specified range (`MIN_BET`–`MAX_BET`).
- 🔄 **Slot Machine Simulation**: Randomized spins based on symbol probabilities.
- 🖥️ **Dynamic Display**: Slot machine results displayed in a clean grid format.

---

## 📜 Rules
1. Players must deposit money before starting the game.
2. Bets can be placed on up to `MAX_LINES` lines.
3. Each bet must be between `MIN_BET` and `MAX_BET`.
4. Total bets cannot exceed the player's current balance.

---

## 🎲 Symbol Distribution
The symbols have varying probabilities:
- 🅰️ `A`: Appears 2 times.
- 🅱️ `B`: Appears 4 times.
- 🅾️ `C`: Appears 6 times.
- 🅾️ `D`: Appears 8 times.

The more a symbol appears, the higher its chance of selection.

---

## 🎮 How to Play
1. 🏦 **Deposit funds** to start the game.
2. 🔢 **Choose the number of lines** to bet on (1–`MAX_LINES`).
3. 💸 **Place your bet** per line within the allowed range.
4. 🎡 **Spin the slot machine** and view the results.

---

## 🛠️ File Structure
The game script is contained in a single Python file.

### 🧩 Key Functions
1. `deposit()`: 💵 Handles user deposits.
2. `getNumOfLines()`: 🎯 Prompts the player to choose the number of lines to bet on.
3. `getBet()`: 💸 Asks for the bet amount per line.
4. `getSlotMachineSpin(rows, cols, symbols)`: 🎰 Simulates a spin based on symbol probabilities.
5. `printSlotMachine(columns)`: 🖥️ Displays the slot machine's results in a grid.
6. `main()`: 🚀 Manages the game flow.

---

## 🖥️ Requirements
- 🐍 **Python 3.x**
- 📦 No external libraries (uses the `random` module from Python’s standard library).

---

## ⚙️ Customization
You can modify the following constants to tweak the game:
- 🔢 `MAX_LINES`: Maximum number of lines to bet on.
- 💰 `MIN_BET`: Minimum bet per line.
- 💸 `MAX_BET`: Maximum bet per line.
- 🟦 `ROWS` and `COLS`: Slot machine grid dimensions.
- 🔠 `symbolCount`: Adjust the frequency of each symbol.

---

## 💡 Example Gameplay
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

## 🚀 Future Enhancements
- 🎉 Add winnings calculation based on matching patterns.
- 💹 Update the balance dynamically after each spin.
- 🔤 Add more symbols and winning combinations.
- 🔄 Allow players to play continuously until their balance is depleted.

---

🎉 Have fun playing the Slot Machine Game responsibly! 🤑
