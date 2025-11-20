import pandas as pd
import matplotlib.pyplot as plt

# Read the data files
wordle_df = pd.read_csv('wordle_stats.csv')
# tic.csv uses tab delimiter
tic_df = pd.read_csv('tic.csv', sep='\t')

# Process Wordle data
wordle_df['date'] = pd.to_datetime(wordle_df['date'])
wordle_df['moves'] = wordle_df.apply(
    lambda row: row['attempts'] if row['result'] == 'WON' else 0, 
    axis=1
)

# Process Tic-Tac-Toe data
tic_df['Date'] = pd.to_datetime(tic_df['Date'])
tic_df['moves'] = tic_df.apply(
    lambda row: row['Number of Moves'] if 'Won' in row['Result'] else 0,
    axis=1
)

# Create the plot
plt.figure(figsize=(12, 6))

plt.plot(wordle_df['date'], wordle_df['moves'], 
         label='Wordle', marker='o', linewidth=2, markersize=6)
plt.plot(tic_df['Date'], tic_df['moves'], 
         label='Tic-Tac-Toe', marker='x', linewidth=2, markersize=8)

# Formatting
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Moves/Attempts (0 = Loss)', fontsize=12)
plt.title('Game Performance: Moves to Win (Losses = 0)', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

plt.show()
