
# Pong Game in Python using Pygame

## Overview
This is a simple implementation of the classic Pong game using Python and the Pygame library. The game features two paddles and a bouncing ball. The objective is to prevent the ball from passing your paddle. Each time a player misses the ball, the opponent gets a point.

This game was created 95% automatically using MetaGPT y ChatGPT Code Interpreter. 
Read more about this here (español): https://open.substack.com/pub/viernes/p/metagpt-una-ia-que-transforma-conceptos
MetaGPT running on Google Colab notebook: https://colab.research.google.com/drive/12XF5HNp3hWLRLxf-rb6KXRKwoTXnmem0
Code Interpreter conversation: https://chat.openai.com/share/f2e9328b-f090-424a-96a0-e681390f78f3

## How it was made
The game is structured around four main files:
- `paddle.py`: Defines the Paddle class responsible for drawing the paddles and their movements.
- `ball.py`: Defines the Ball class responsible for drawing the ball and its movement logic.
- `game.py`: Implements the main game logic, including scoring, game state transitions, and interactions between the ball and the paddles.
- `main.py`: The entry point of the application. It initializes and runs the game.

## Installation
1. Ensure you have Python 3.x installed on your machine.
2. Install the required dependencies using pip:
```bash
pip install pygame==2.0.1
```
3. Clone the repository or download the game files.

## Running the Game
Navigate to the directory containing the game files and run the following command:
```bash
python main.py
```

The game window should open, and you can start playing!

## Controls
- Player 1 (Left paddle): `W` (Move Up), `S` (Move Down)
- Player 2 (Right paddle): Arrow Up (Move Up), Arrow Down (Move Down)
