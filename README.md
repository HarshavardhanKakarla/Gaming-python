Interactive desktop games developed using **Python** and the **Pygame** library.

##  Overview

This repository showcases classic arcade-style games built in Python, featuring graphical interfaces, keyboard interaction, scoring systems, and responsive menus.

### Included Games:
-  **Snake Game**
-  **Lane Car Racing Game**
-  **Brick Breaker**
-  **Word Unscrambler**
 
<p float="center">
  <img src="https://github.com/HarshavardhanKakarla/Gaming-python/blob/88e31dc6adfa86e2f5e4653b172000e31e7808ee/Screenshot%202025-07-22%20193257.png"  width="45%" />
  <img src="https://github.com/HarshavardhanKakarla/Gaming-python/blob/88e31dc6adfa86e2f5e4653b172000e31e7808ee/Screenshot%202025-07-22%20193419.png" width="45%" /> 
</p>  

<p float="center">
  <img src="https://github.com/HarshavardhanKakarla/Gaming-python/blob/f356903a838f878ca2a8563e327200ef998faaf3/images/Screenshot%202025-08-04%20162923.png" width="45%" />
  <img src="https://github.com/HarshavardhanKakarla/Gaming-python/blob/f356903a838f878ca2a8563e327200ef998faaf3/images/Screenshot%202025-08-04%20163153.png" width="45%" /> 
</p>

##  Features

### Snake Game
- Classic grid-based snake mechanics  
- Arrow-key navigation  
- Randomized food generation  
- Real-time scoring & game-over triggers  

### Lane Car Racing Game
- Fast-paced lane dodging gameplay  
- Player & enemy car sprites  
- Progressive difficulty scaling  
- Collision-based game over detection  
- Animated lanes with responsive switching
  
###  Brick Breaker
Break all the bricks using a bouncing ball and paddle:
- Paddle movement with arrow keys
- Ball physics and wall rebounds
- Brick collision and score tracking
- Game-over and reset functionality

###  Word Unscrambler
Test your vocabulary and reflexes:
- Randomly scrambled word challenges
- Text input detection and validation
- Score and attempt counter
- Dictionary-based word generation

### Common Functionality
- Main menu interface for game selection  
- Difficulty selection screen  
- Game-over logic with restart option  
- Custom fonts & responsive UI layout  

##  Technologies Used
- Python 3  
- Pygame (for rendering, event handling, and game logic)  
- Custom image assets:


##  Repository Structure

```
Gaming-python/
├── Snake & Lane Car Race
     ├── app.py
├── BrickBreaker
     ├── app.py
├── WordUnscrambler
     ├── app.py
├── assets/           # Images, fonts, or sounds (if included)
└── README.md

```

##  Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/HarshavardhanKakarla/Gaming-python.git
cd Gaming-python
```

### 2. Install Requirements
Make sure you have **Python 3.x** installed.  
Install pygame:
```bash
pip install pygame
```

### 3. Confirm Assets
Ensure the  files are in the  folder `images` to run the code  
To add background music make sure to make chages accordingly

### 4. Run the Application
```bash
python app.py
```

### 5. Play the Games!
Use the menu to select your game and preferred difficulty.

##  Controls

| Action                     |  Games                 |
|----------------------------|------------------------|
| Navigate Menu              | Number keys (1, 2...)  |
| Quit                       | Q                      |
| Restart                    | R                      |
| Movement                   | Arrow keys             |

##  License

This project is **open source** and intended for educational use.

## Credits

Developed by **Harshavardhan Kakarla**

For feature requests, issues, or contributions, feel free to open an issue on the [GitHub repository](https://github.com/HarshavardhanKakarla/Gaming-python).
