# War Plane
Very simple 2D scrolling fighter plane game using Pygame

Shoot down enemy planes and try for a high score, but the game gets faster with every 10 points you get!

>This game was part of a school project so don't expect me to continue development on this. I'm not going to add anything new or fix anything. However, if you would like to contribute (I doubt anyone would), please make a pull request with the modified code. I would appreciate it if someone knows how to fix the bugs listed in [Known Bugs](https://github.com/TheDragonary/War-Plane/#known-bugs). And if you like reading, you can read some of the thoughts I had [here](https://github.com/TheDragonary/War-Plane/#random-facts).

And yes, there are two Python files in the repo, that is no mistake.

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
### Windows
Run the setup file
```
python setup.py build
```
Give it a few seconds and you'll find yourself with a new exe file!

### Linux
Exact same process as above, but replace one thing. I'm sure you can figure that out, but for your convenience, I have given it to you below.
```
python setup-linux.py build
```
Now this time you get an AppImage, but wait, it doesn't work! To fix that, just copy the folders backgrounds, fonts, sfx and sprites over there. I don't know why the setup script doesn't do that automatically as it does that for Windows, but who knows.

### Building the game without menus
Option 1: Edit the setup script and swap `main.py` for `no-menu.py`

Option 2: Rename `main.py` to something else, rename `no-menu.py` to `main.py`

Whichever option you go with, the build instructions are still the same so just follow the instructions above for your platform.

## Random Thoughts
- At one point I was going to implement bosses. They would appear every 20 points and they would basically just be a very big version of the enemy plane but they take about 10 or so bullets before disappearing, then the game continues as normal. Also, you would get 5 points for destroying them. The reason why they aren't here is because they basically broke the game. Your bullets would just go through and the boss would be stuck on the screen forever, impossible to get rid of. So I simply just scrapped the whole idea.
- Items! I just didn't know how to even get started with them. Couldn't get them to appear at all. And I realised that it would be a LOT of work to add them in. There would've been all sorts of items like: extra life, faster speed, more ammo, more damage, etc. But since this was a school project, I simply did not have enough time.
- I also wanted to add upgrades. You could earn coins by playing, then spend them on your plane to increase health, damage, speed, etc. I could even add in more planes that you could buy, all with different stats. This would probably make the game closer to one of those mobile games. However, same reason, no time! And Pygame isn't really the best for complicated things, I would have to make drastic changes to the entire game in order to make all of that possible.
- I am not going to add these features by the way, I'm done! :sob: I had some pretty big ambitions with the game early on, but since this was a school project, I had time constraints. I don't exactly think Pygame is a great game engine, and if I ever wanted to make a new game, I'd go with Godot, or maybe Gamemaker. Pygame is probably only good for basic games. Feel free to prove me wrong though.
- Why am I putting this onto Github just now? It's a piece of my history I guess. It's the first game that I ever made so I guess I could say I'm pretty proud of it, even if it isn't all that great. Other reason is that it is somewhat proof that I actually know some Python. And lastly, just in case something happens to my computer and I lose everything, I'll have it safely kept here.
- And no, I will not be working on the game anymore. I accept contributions though, all I really need help with are the bugs I've listed above, you don't have to try and implement some of the features discussed here.
