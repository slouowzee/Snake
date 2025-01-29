# README.md content

# Snake Game

This is a simple Snake game implemented using Pygame. The objective of the game is to control the snake to eat food and grow in length while avoiding collisions with the walls and itself.

## Project Structure

```
snake-game
├── src
│   ├── game
│   │   ├── __init__.py
│   │   ├── snake.py
│   │   ├── food.py
│   │   └── constants.py
│   └── main.py
├── tests
│   ├── __init__.py
│   └── test_game.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd snake-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, run the following command:
```
python src/main.py
```

## Controls

- Use the arrow keys to control the direction of the snake.
- Eat the food to grow the snake.
- Avoid colliding with the walls or the snake's own body.

## Testing

To run the tests, execute:
```
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License.