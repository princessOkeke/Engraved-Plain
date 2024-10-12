# Engraved Plain

## Overview
**Engraved Plain** is a strategic twist on tic-tac-toe, played on a 5x5 grid. Two players take turns marking spaces with X or O, but each player has three restricted spaces they cannot use. The objective is to align four consecutive marks (X or O) horizontally, vertically, or diagonally.

<img width="333" alt="game2" src="https://github.com/user-attachments/assets/f23cfff4-4019-4f76-afda-bf66fa8d71ba">

<img width="333" alt="game6" src="https://github.com/user-attachments/assets/435d0ee9-60ce-4295-85da-b08f4bf3be33">

<img width="333" alt="game5" src="https://github.com/user-attachments/assets/d4ef71a1-084f-46bb-a4b5-324865b9a114">

## Game Play Demo
https://github.com/user-attachments/assets/67f60e09-eb25-4a5e-9bba-58c91fe029a1



## Game Features

- **Grid Size**: A larger 5x5 grid allows for more complex strategies compared to traditional tic-tac-toe.

- **Unique Restrictions**: Each player has three randomly generated spaces where they cannot play, introducing variability each time the game is reset.

- **Winning Conditions**: Players win by forming four consecutive marks in a row, column, or diagonally.

## Modes of Play

- **Single Player Mode**: Compete against an AI powered by the minimax algorithm, which calculates optimal moves.

- **Double Player Mode**: Play against another human.





## Technology Implemented

1. **Tkinter**  
   Tkinter is Python’s standard GUI library, used for building the game window and managing player interactions. It allows for easy button creation and responsive event handling.

2. **Minimax Algorithm**  
   The minimax algorithm, enhanced with alpha-beta pruning, optimizes the AI's decision-making by evaluating possible moves and predicting outcomes. An evaluation function assesses the board state, considering potential wins and threats.

## Gameplay Mechanics

- Players alternate turns, with the game checking for valid moves based on restrictions.
- The game continuously evaluates the state after each turn to detect wins or draws.
- A reset option allows players to start fresh, re-randomizing restricted spaces.

### How to Clone and Play Engraved Plain

- **Prerequisites:**
  - Install **Python 3.x**: [Download here](https://www.python.org/downloads/).
  - Install **NumPy**:
    ```bash
    pip install numpy
    ```

- **Clone the Repository:**
  - Open your terminal.
  - Navigate to your desired directory.
  - Run:
    ```bash
    git clone https://github.com/princessOkeke/Engraved-Plain.git
    ```

- **Run the Game:**
  - Change into the cloned directory:
    ```bash
    cd Engraved-Plain
    ```
  - Execute the game:
    ```bash
    python GamePlay.py
    ```

- **Notes:**
  - Ensure Tkinter is included with your Python installation.
  - Follow the on-screen instructions to start playing!


## Conclusion
**Engraved Plain** redefines the classic tic-tac-toe experience with its larger grid and added complexity. The combination of a user-friendly interface and a robust AI challenge provides engaging gameplay for all skill levels.
