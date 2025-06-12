# Tic-Tac-Toe (with Bots)

<br/>

## Features
- Bot plays 'Optimally' using 'minimax' algorithm on all legal moves to find the best move to play
- Board state for current position of board
- Pygame implementation for (Human vs Human) AND (Human vs Bot)
- Remove Moves using Key Press - 'B' -> For Bot games removes until last user move
- Text Pop Up for Wins/Draws

## Prerequisites
 **Python3** 
 **pygame** `pip install pygame`

<br/>

## How To Run

```bash
# 1. Clone the repository
git clone https://github.com/RiazulRahat/tic-tac-toe.git
cd tic-tac-toe

# 2. [Optional] Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install pygame

# Go To Directory
cd /src/tictactoe

# 4. a. Play (Human vs Human)
python game.py

# OR

# 4. b. Play as O (Human vs Bot)
python game_ai_x.py # bot plays X

# OR

# 4. c. Play as X (Human vs Bot)
python game_ai_o.py # bot plays O


# Alternatively: can run by running specific files in VSCode - Run Python File


# NOTE: Bot should play moves Automatically, Just press on an empty square to play your move.

# Enjoy!