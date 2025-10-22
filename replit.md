# Jeu de Gestion de Boulangerie

## Overview
A French bakery management simulation game built in Python. Players manage a bakery over 7 days, making bread, selling products, buying ingredients, and dealing with random daily events. The game is text-based and runs in the console.

## Project Information
- **Language**: Python 3.11
- **Type**: Console/Terminal-based game
- **Main File**: main.py

## Game Mechanics
- **Duration**: 7 game days
- **Daily Actions**: 5 actions per day
- **Starting Resources**: 1000€, 50kg flour, 10kg yeast, 5kg salt, 50L water
- **Daily Customer Limit**: 50-100 customers per day (random, resets daily)
- **Bread Aging System**: 
  - Day 0 (fresh): Best price (4-6€)
  - Day 1: Medium price (3-4€)
  - Day 2: Reduced price (2€)
  - Day 3+: Automatically discarded

## Random Events
The game includes various random events each day, both positive (rich customers, food critic, free delivery, village festival) and negative (pigeon attack, robbery, oven breakdown, strike, health inspector).

## Recent Changes
- **2025-10-22**: Enhanced score tracking and display
  - Scores now include date and time of completion
  - Top 10 leaderboard displayed at end of each game
  - Backward compatible with old score format
  - All scores are preserved in scores.txt (append mode)
- **2025-10-22**: Added daily customer limit system
  - Customers per day now vary between 50-100 (random each day)
  - Players can only sell up to the daily customer limit
  - Status displays now show customer count (sold/max)
  - Clear feedback when customer limit is reached
- **2025-10-21**: Initial setup in Replit environment
  - Installed Python 3.11
  - Created project documentation

## Project Structure
```
.
├── main.py              # Main game code
├── scores.txt           # Score save file (auto-generated)
├── README.md            # Game documentation (French)
├── InfoBoulangerie.md   # Bread production calculation info
├── LICENSE              # MIT License
├── replit.md            # This file
└── git_commit.ps1       # PowerShell script (not used in Replit)
```

## Running the Game
The game runs via: `python main.py`

## Dependencies
- Standard Python library only (random, time)
- No external packages required
