# Minesweeper for the TI-84 Evo-T

A colour Minesweeper game for the **TI-84 Evo-T** graphing calculator, written in Python.

> **Made with AI:** this game and this README were created with the help of AI (Claude by Anthropic).
> Everything was tested on a real TI-84 Evo-T.

## Features

- 12 × 8 board with 17 mines
- **The first square you open is always safe**
- Empty areas open up by themselves
- Big, clear numbers in the classic colours
- Flags to mark mines
- **Wins and games** stay saved after you quit
- No flicker

## What you need

- A **TI-84 Evo-T** calculator
- A USB cable to connect it to your computer
- **Google Chrome** or **Microsoft Edge** (Safari and Firefox do not work with the TI tool)
- The file [`sweeper.py`](sweeper.py) from this repo

## Setup

1. Download [`sweeper.py`](sweeper.py) to your computer.
2. Connect the calculator to your computer with the USB cable.
   Leave the calculator on the **home screen**.
3. Open **https://connectevo.ti.com** in **Chrome** or **Edge**.
4. Connect to your calculator in the page and allow access when the browser asks.
5. Drag `sweeper.py` onto the page to send it to the calculator.
6. **Choose RAM** to play right away.
   The Python app on the Evo-T only shows files that are in RAM.
   (Want to keep the game safe? See [Don't lose the game](#dont-lose-the-game).)

> **Already sent it to Archive?** On the **home screen** (not in the Python app) press **2nd → mem → Mem Management**,
> find **SWEEPER** and press **enter**. The `*` in front of the name disappears, which means
> it is now in RAM.

## Start the game

1. Open the **Python** app on the calculator.
2. Choose **SWEEPER** and run it.
3. Press **enter** on the start screen.

## Don't lose the game

The Evo-T **deletes RAM** when it stays turned off for a while.
A normal turn-off is fine, but after some time the game is gone.

**Best way:**

1. Keep the game in **Archive**. Archive is never deleted.
2. Go to the **home screen**. If you are in the Python app, leave it with **2nd → quit**
   (quit is above the **mode** key). In the Python app, **2nd → mem** does nothing.
3. Press **2nd → mem** (mem is above the **+** key) and choose **2: Mem Management**.
4. Choose the list with Python programs (or **All**).
5. Find **SWEEPER** and press **enter**. The `*` disappears, which means the game is now in RAM.
6. Open the **Python** app and play.

Programs can't move files between Archive and RAM by themselves, so this step can't be automatic.
The wins list **MINES** is in RAM too, so it can be deleted the same way.

## Keys

| Key | What it does |
|---|---|
| ◀ ▶ ▲ ▼ | Move the yellow frame |
| enter | Open a square |
| 2nd or mode | Put a flag on a square (press again to remove it) |
| clear | Quit |

## Rules

- A **number** tells you how many mines are in the 8 squares around it.
- Open every square **without** a mine to win.
- Open a mine and the game is over.

## Wins

Your wins and games are saved in a calculator list called **MINES**, so they stay after you quit.

- To reset them, delete the list **MINES** in **2nd → mem → Mem Management** (on the home screen).
- A calculator reset (RAM clear) also resets them.

## Good to know

- Keep `sweeper.py` on your computer too, so you can always send it again.
- Made for the TI-84 Evo-T. Other TI-84 models are not tested.
