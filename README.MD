# 🏦 Python Mini Banking System

A simple, menu-driven banking application developed using **Python and Object-Oriented Programming (OOP)**. This project allows users to perform basic banking operations such as depositing money, withdrawing money, checking account balances, and viewing transaction history.

## ✨ Features

- **Account Creation:** Creates a bank account with an account holder's name.
- **Account Details:** Displays the account holder's name, account number, and available balance.
- **Deposit Money:** Allows users to deposit money with a minimum deposit requirement of ₹500.
- **Withdraw Money:** Allows users to withdraw money while checking their available balance.
- **Balance Inquiry:** Displays the current account balance.
- **Transaction History:** Records and displays deposit and withdrawal transactions.
- **Input Validation:** Prevents deposits and withdrawals of non-positive amounts and prevents withdrawals exceeding the available balance.
- **Interactive Menu:** Provides a menu-driven interface for selecting banking operations.
- **Exit Message:** Displays a thank-you message when the user exits the application.

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Instance and Class Variables
- Methods
- Lists and Dictionaries
- Conditional Statements (`if-elif-else`)
- Loops (`while` and `for`)
- User Input and Output

## 📂 Project Structure

```text
Python-Mini-Banking-System/
│
├── bms.py
└── README.md
```

## ⚙️ How to Run the Project

### Prerequisites

- Python 3 installed on your computer.

### Steps

1. Clone or download this repository.
2. Open the project folder in VS Code or a terminal.
3. Open the terminal in the project directory.
4. Run the following command:

```bash
python bms.py
```

On Windows, you can also use:

```bash
py bms.py
```

## 📋 Available Banking Operations

When you run the program, the following menu appears:

```text
========== MINI BANKING SYSTEM ==========

1. Show Account Details
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Transaction History
6. Exit

=========================================
```

Select an option from 1 to 6 to perform the desired operation.

## 📚 Learning Objectives

This project was developed to practise Python programming and understand how Object-Oriented Programming can be used to organize a real-world application.

Key concepts practised include:

- Creating classes and objects.
- Initializing objects using constructors.
- Managing account balances through instance variables.
- Defining methods for different banking operations.
- Storing transactions using lists and dictionaries.
- Applying conditional statements for validation.
- Using loops to create an interactive menu.

## 🚀 Future Improvements

- Save account details and transaction history using JSON.
- Support multiple bank accounts and account selection.
- Add PIN-based authentication.
- Implement money transfers between accounts.
- Handle invalid inputs using `try-except`.
- Improve transaction history and account management.
- Add automated tests for banking operations.

## ⚠️ Current Limitations

- Account and transaction data are stored in memory and are not saved after the program exits.
- The application currently creates one account when the program starts.
- This is an educational project and is not intended for real banking transactions.

## 👨‍💻 Author

**Amit Pal**

GitHub: [AmitStack98](https://github.com/AmitStack98)

## 📄 License

No license has been added to this repository yet.
