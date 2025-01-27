# BeatDown: A countdown timer with Music

BeatDown is a TUI timer written in python that also plays music.
## Features
- Display a countdown timer in ASCII art format.
- Plays your favorite music in background using `mpv`.
## Installation
To use BeatDown, you need to have python and python-pip installed. Follow these steps:
1. Clone this repository:

```bash
git clone https://github.com/ashraddhansh/BeatDown.git
```

2. Install Dependencies

```bash
pip install -r requirement.txt
```

3. Make sure you have mpv installed, it is required to play music from the terminal. You can install it using following commands.

- On Ubuntu/Debian:

```bash
sudo apt install mpv
```

- On Fedora:

```bash
sudo dnf install mpv
```

- On Arch Linux:

```bash
sudo pacman -S mpv
```

- On MacOS(via homebrew):

```bash
brew install mpv
```

## Usage
```bash
python main.py <minutes> <seconds>
```
### Parameters
- **minutes:** No of minutes you want to play the timer.
- **seconds:** No of seconds you want to play the timer.
### Example
```bash
python main.py 10 43
```

This will set the timer for 10 minutes and 43 seconds.

## Changing the Music
As BeatDown is powered by mpv so you can play any kind of music from youtube or stored in your computer.
To change to music you need to edit the `main.py`, just paste the youtube link in `mpv_process` line or the absolute path of the music stored on your computer.
### Example

```python
mpv_process = subprocess.Popen(['mpv', '--no-video', '--no-terminal', 'https://www.youtube.com/watch?v=OgU_UDYd9lY&t=913s'])
```

or like this

```python
mpv_process = subprocess.Popen(['mpv', '--no-video', '--no-terminal', '/home/tomato/Music/LinkinPark/from-Zero.flac'])
```
