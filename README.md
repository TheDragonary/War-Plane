# War Plane
Simple 2D scrolling fighter plane game with progressive difficulty using Pygame

Shoot down enemy planes and try for a high score, but the game gets more difficult the higher your score!

## Downloads
- [Windows](https://github.com/TheDragonary/War-Plane/releases/latest/download/War-Plane-Windows.zip)
- [Linux](https://github.com/TheDragonary/War-Plane/releases/latest/download/War-Plane-Linux.tar.gz)

## Controls
|Action|Key|
|-|-|
|Movement|Arrow keys / WASD|
|Shoot|Space|

## Features
- Endless progressive difficulty
- Increasing enemy speed and fire rate
- Limited ammo; gain ammo with every kill

## Screenshots
![](https://github.com/TheDragonary/War-Plane/blob/main/screenshots/1.png)
![](https://github.com/TheDragonary/War-Plane/blob/main/screenshots/2.png)
![](https://github.com/TheDragonary/War-Plane/blob/main/screenshots/3.png)

## Building
Not sure why you would ever want to build this as you can find the latest build in [Releases](https://github.com/TheDragonary/War-Plane/releases) but anyways,

Clone the repo
```
git clone https://github.com/TheDragonary/War-Plane.git
```
Install requirements - main packages are `pygame` and `pygame_menu`. Latest Python version (3.12+) should work fine.
```
pip install -r requirements.txt
```
Run the spec file
```
pyinstaller "War Plane.spec"
```
Done! You'll find the executable in the `dist/` folder.
