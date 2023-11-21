import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        print(f"{_} column - {column}")
        current_symbols = all_symbols[:]
        print(f"{_} current_symbols - {current_symbols}")
        print(f"{_} all_symbols - {all_symbols}")
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            print(f"{_} current_symbols - {current_symbols}")
            column.append(value)
            print(f"{_} column - {column}")
    
        columns.append(column)
    print(columns)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        print(f"{line} - {symbol}")
        for column in columns:
            symbol_to_check = column[line]
            print(f"{column} - {symbol_to_check}")
            if symbol != symbol_to_check:
                print(f"{symbol} != {symbol_to_check}")
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    print(winnings)
    print(winning_lines)
    return winnings, winning_lines

# get_slot_machine_spin(ROWS, COLS, symbol_count)
columns = [['C', 'D', 'B'], ['B', 'A', 'D'], ['D', 'C', 'A']]
lines = 3
bet = 10
# print_slot_machine(columns)

check_winnings(columns, lines, bet, symbol_value)