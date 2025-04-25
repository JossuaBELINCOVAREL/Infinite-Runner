# Infinite Runner Game 🏃‍♂️

A simple 2D infinite runner built with **Pygame**. Control a player that can jump over obstacles while the game gets faster and harder. Avoid collisions, beat your high score, and restart anytime!

---

## 🎮 Features

- Smooth player movement (left, right, jump)
- Gravity-based jumping mechanics
- Obstacle generation with increasing difficulty
- Score system with live display
- Game Over and Restart screen
- Background image rendering

---

## 📁 Project Structure

```
project-root/
│
├── assets/
│   ├── background.jpg       # Background image
│   └── player.jpg           # Player character image
│
├── style.py                 # Styling and UI helper functions
├── main.py                  # Main game logic
└── README.md                # This documentation
```

---

## 🔧 Requirements

Make sure Python is installed, then install **pygame**:

```bash
pip install pygame
```

---

## 🚀 How to Run

Run the game from your terminal or IDE:

```bash
python main.py
```

The game will launch in a window. Use the following controls to play:

---

## 🕹 Controls

| Key            | Action              |
|----------------|---------------------|
| **← / →**       | Move Left / Right   |
| **Spacebar**   | Jump                |
| **R**          | Restart after death |
| **ESC / Quit** | Exit game           |

---

## 🔁 Gameplay Loop

1. The player starts near the ground and can move horizontally.
2. Press **space** to jump over incoming obstacles.
3. If you hit an obstacle, you’ll see the "Game Over" screen.
4. Press **R** to restart the game and try again.

---

## 🎨 Customization

You can easily:
- Replace `player.jpg` with your own character sprite.
- Update `background.jpg` to change the scenery.
- Modify values like jump height, gravity, or obstacle speed in `main.py`.

---

## 🛠 Todo (Optional Improvements)

- Add background scrolling effect (parallax)
- Introduce sounds/music
- Add more obstacle types
- Track high scores
- Add animated character sprite

---

## 📄 License

This project is provided for educational and non-commercial purposes. Feel free to modify and improve it!

---

## 🧠 Author

Made with ❤️ using [Pygame](https://www.pygame.org/)

