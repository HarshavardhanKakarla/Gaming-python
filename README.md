Interactive desktop games developed using **Python** and the **Pygame** library.

##  Overview

This repository showcases classic arcade-style games built in Python, featuring graphical interfaces, keyboard interaction, scoring systems, and responsive menus.

### Included Games:
-  **Snake Game**
-  **Lane Car Racing Game**
 
<p float="center">
  <img src="https://github.com/HarshavardhanKakarla/Gaming-python/blob/88e31dc6adfa86e2f5e4653b172000e31e7808ee/Screenshot%202025-07-22%20193257.png" width="45%" />
  <img src="https://github.com/HarshavardhanKakarla/Gaming-python/blob/88e31dc6adfa86e2f5e4653b172000e31e7808ee/Screenshot%202025-07-22%20193419.png" width="45%" /> 
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

### Common Functionality
- Main menu interface for game selection  
- Difficulty selection screen  
- Game-over logic with restart option  
- Custom fonts & responsive UI layout  

##  Technologies Used
- Python 3  
- Pygame (for rendering, event handling, and game logic)  
- Custom image assets:
  - `player_car.png`
  - `enemy_car.png`

##  Repository Structure

```
Gaming-python/
├── app.py             # Main game launcher with menu
├── player_car.png     # Asset for player car
├── enemy_car.png      # Asset for enemy cars
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
Ensure the following files are in the same directory as `app.py`:
- `player_car.png`
- `enemy_car.png`

### 4. Run the Application
```bash
python app.py
```

### 5. Play the Games!
Use the menu to select your game and preferred difficulty.

##  Controls

| Action                     | Snake Game             | Lane Car Racing Game     |
|----------------------------|------------------------|---------------------------|
| Navigate Menu              | Number keys (1, 2...)  | Number keys (1, 2...)     |
| Quit                       | Q                      | Q                         |
| Restart                    | R                      | R                         |
| Movement                   | Arrow keys             | Arrow keys                |

##  License

This project is **open source** and intended for educational use.

## Credits

Developed by **Harshavardhan Kakarla**

For feature requests, issues, or contributions, feel free to open an issue on the [GitHub repository](https://github.com/HarshavardhanKakarla/Gaming-python).
