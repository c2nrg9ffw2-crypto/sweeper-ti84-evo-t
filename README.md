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
6. **Choose RAM, not Archive.**
   The Python app on the Evo-T does not show files that are in Archive.

> **Already sent it to Archive?** On the calculator press **2nd → mem → Mem Management**,
> find **SWEEPER** and press **enter**. The `*` in front of the name disappears, which means
> it is now in RAM.

## Start the game

1. Open the **Python** app on the calculator.
2. Choose **SWEEPER** and run it.
3. Press **enter** on the start screen.

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

- To reset them, delete the list **MINES** in **2nd → mem → Mem Management**.
- A calculator reset (RAM clear) also resets them.

## Good to know

- Files in RAM are deleted when the calculator resets. Keep `sweeper.py` on your computer
  so you can send it again.
- Made for the TI-84 Evo-T. Other TI-84 models are not tested.
