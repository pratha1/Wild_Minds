# Wild Minds 🧠

A web-based cognitive health monitoring platform that detects early dementia patterns through gameplay analytics.

## 🎯 Project Overview

Wild Minds uses interactive games to track cognitive abilities related to mental health. By analyzing gameplay patterns and performance metrics, the platform helps identify potential early signs of cognitive decline, particularly dementia patterns.

**Live Website:** [wildmind27.wixsite.com](https://durga2005.wixsite.com/wildmind27)

## 🎮 Features

### Interactive Games
- **Wordle**: Word puzzle game tracking vocabulary recall and problem-solving abilities
- **Tic-Tac-Toe**: Strategy game monitoring decision-making and spatial reasoning

### Analytics & Tracking
- Real-time performance tracking
- Game statistics visualization
- CSV export for detailed analysis
- Cognitive ability trend monitoring

### Performance Visualization
- Combined gameplay performance graphs
- Win/loss tracking with move counts
- Temporal pattern analysis
- Comparative metrics between different game types

## 📊 How It Works

1. **Play Games**: Users engage with Wordle and Tic-Tac-Toe
2. **Track Performance**: Each game logs attempts, moves, and outcomes
3. **Export Data**: Download gameplay statistics as CSV files
4. **Analyze Patterns**: Visualize cognitive performance over time using Python analytics

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Data Analysis**: Python (pandas, matplotlib)
- **Deployment**: Wix platform
- **Development**: Agile team collaboration

## 📁 Project Structure

```
wild minds/
├── tic.html              # Tic-Tac-Toe game interface
├── wordle.py             # Wordle game logic
├── reports.py            # Data visualization script
├── tic.csv               # Tic-Tac-Toe game logs
├── wordle_stats.csv      # Wordle performance data
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Playing the Games

1. Visit [wildmind27.wixsite.com](https://durga2005.wixsite.com/wildmind27)
2. Choose a game (Wordle or Tic-Tac-Toe)
3. Play and track your performance
4. Download your gameplay statistics

### Running Local Analysis

#### Prerequisites
```bash
pip install pandas matplotlib
```

#### Generate Performance Reports
```python
python reports.py
```

This will create a combined graph showing:
- Wordle attempts per game (0 for losses)
- Tic-Tac-Toe moves per game (0 for losses)
- Performance trends over time

## 📈 Data Format

### Wordle Statistics (`wordle_stats.csv`)
```csv
date,word,attempts,result
2025-11-19,DANCER,7,WON
2025-11-17,ISLAND,5,WON
```

### Tic-Tac-Toe Logs (`tic.csv`)
```csv
Date	Time	Number of Moves	Result
11/19/2025	17:52:43	9	Player X Won
11/15/2025	17:52:43	9	Player X Won
```

## 🧪 Cognitive Metrics Tracked

- **Success Rate**: Win/loss patterns
- **Attempts Required**: Problem-solving efficiency
- **Move Count**: Strategic planning ability
- **Temporal Patterns**: Performance consistency over time


## 🔮 Future Enhancements

- Additional cognitive games (memory, pattern recognition)
- Machine learning-based pattern detection
- Personalized cognitive health reports
- Mobile app development
- Healthcare provider integration

