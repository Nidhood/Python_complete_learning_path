import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


# First we import the data:
bike_d_df = pd.read_csv('bike+sharing+dataset/day.csv')
bike_h_df = pd.read_csv('bike+sharing+dataset/hour.csv')

# What time of year should I make sure I have the most bikes available?
# We select the usefully fields for the answer:
# -> season ( Categorical variable ) : Represents seasons.
# -> cnt    ( Numerical variable )   : Represents count of total rental bikes including both casual and registered.

# Change numbers for season names to improve readability (1:springer, 2:summer, 3:fall, 4:winter):
season_map = {
    1: 'Primavera',
    2: 'Verano',
    3: 'Otoño',
    4: 'Invierno'}
bike_d_df['season'] = bike_d_df['season'].map(season_map)

# For each season, we will calculate the total number of bikes rented:
seasonal = (
    bike_d_df.groupby('season')['cnt']
    .agg(['sum', 'mean', 'count'])
    .reset_index()
)

# Sort descending by mean rentals:
seasonal = seasonal.sort_values(by='mean', ascending=False).reset_index(drop=True)

#  Coloring scheme for the plot:
cmap = plt.colormaps['RdYlGn']  # red - yellow - green

# Seasonal plot
vals = seasonal['mean'].values
norm = mcolors.Normalize(vmin=vals.min(), vmax=vals.max())
colors = [cmap(norm(v)) for v in vals]
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(seasonal['season'], vals, color=colors)
ax.bar_label(bars, fmt='%.0f')
ax.set_title('Promedio de alquileres diarios por estación')
ax.set_xlabel('Estación')
ax.set_ylabel('Promedio de alquileres diarios')
fig.tight_layout()
plt.show()


# Save the image:
fig.savefig('plot_results/seasonal_bike_rentals.png', dpi=300, bbox_inches='tight')
