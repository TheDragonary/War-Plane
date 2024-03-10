# War Plane
Very simple 2D scrolling fighter plane game using Pygame

Shoot down enemy planes and try for a high score, but the game gets faster with every 10 points you get!

>This game was part of a school project so don't expect me to continue development on this. I'm not going to add anything new or fix anything. However, if you would like to contribute (I doubt anyone would), please make a pull request with the modified code. I would appreciate it if someone knows how to fix the bugs listed in [Known Bugs](https://github.com/TheDragonary/War-Plane/#known-bugs).

And yes, there are two Python files in the repo.

`main.py` = The main game itself of course

`no-menu.py` = Just the game without any of the menus

## Downloads
Downloads can be found in [Releases](https://github.com/TheDragonary/War-Plane/releases)

### Latest
- [Windows](https://github.com/TheDragonary/War-Plane/releases/latest/download/War-Plane-Windows.zip)
- [Linux](https://github.com/TheDragonary/War-Plane/releases/latest/download/War-Plane-Linux.tar.gz)

### No Menu
- [Windows](https://github.com/TheDragonary/War-Plane/releases/download/v0.1/War-Plane-Windows.zip)
- [Linux](https://github.com/TheDragonary/War-Plane/releases/download/v0.1/War-Plane-Linux.tar.gz)

## Controls

|Action|Key|
|-|-|
|Movement|Arrow keys / WASD|
|Shoot|Space|
|Pause|Esc|

## Screenshots
![](https://github.com/TheDragonary/War-Plane/blob/main/screenshots/1.png)
![](https://github.com/TheDragonary/War-Plane/blob/main/screenshots/2.png)
![](https://github.com/TheDragonary/War-Plane/blob/main/screenshots/3.png)

## Known Bugs
- Continue button in the pause menu does not work
- All enemy planes fire bullets at the exact same time instead of random times for each plane

## Building
Not sure why you would ever want to build this as you can find the latest build in [Releases](https://github.com/TheDragonary/War-Plane/releases) but anyways,

Clone the repo
```
git clone https://github.com/TheDragonary/War-Plane
```
Install requirements needed to run the game
```
pip install -r requirements.txt
```

### Windows
Install cx-freeze
```
pip install cx-freeze
```
Run the setup file
```
python setup.py build
```
Give it a few seconds and you will get a new exe file!

### Linux
Exactly the same as above, but replace one thing.
```
python setup-linux.py build
```
Now this time you get an AppImage, however it doesn't work. To fix that, just copy the folders backgrounds, fonts, sfx and sprites over there. I don't know why the setup script doesn't do that automatically as it does that for Windows, but who knows.

### Building the game without menus
Option 1: Edit the setup script and swap `main.py` for `no-menu.py`

Option 2: Rename `main.py` to something else, rename `no-menu.py` to `main.py`

Whichever option you go with, the build instructions are still the same so just follow the instructions above for your platform.
