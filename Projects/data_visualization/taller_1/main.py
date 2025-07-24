import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

# First we import the data:
bike_d_df = pd.read_csv('bike+sharing+dataset/day.csv')
bike_h_df = pd.read_csv('bike+sharing+dataset/hour.csv')

# 1. What time of year should I make sure I have the most bikes available?
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

# 2. What are the times of day and days of the week when I will have the highest demand by user type?
# We select the usefully fields for the answer:
# -> hr         ( Categorical variable )   : Represents hour of the day.
# -> weekday    ( Categorical variable ) : Represents day of the week.
# -> cnt        ( Numerical variable )   : Represents count of total rental bikes including both casual and registered.

# Change numbers for day names to improve readability (day of the week):
weekly_map = {
    0: 'Lunes',
    1: 'Martes',
    2: 'Miércoles',
    3: 'Jueves',
    4: 'Viernes',
    5: 'Sábado',
    6: 'Domingo'}
bike_h_df['weekday'] = bike_h_df['weekday'].map(weekly_map)

# For each hour and day of the week, we will calculate the average number of bikes rented for each user type:
hourly = (
    bike_h_df
    .groupby('hr')[['casual','registered']]
    .mean()
    .reset_index()
    .melt(id_vars='hr', var_name='user_type', value_name='avg_count')
)

# Map user types to more readable names:
hourly['user_type'] = hourly['user_type'].map({
    'casual': 'Casual',
    'registered': 'Registrado'
})

# Plotting the average number of rentals by hour and user type:
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(
    data=hourly,
    x='hr',
    y='avg_count',
    hue='user_type',
    marker='o',
    ax=ax
)
ax.set_xticks(range(0, 24))
ax.set_title('Promedio de alquileres por hora y tipo de usuario')
ax.set_xlabel('Hora del día')
ax.set_ylabel('Promedio de alquileres por hora')
ax.grid(True)
fig.tight_layout()
plt.show()

# Save the image:
fig.savefig('plot_results/hourly_bike_rentals.png', dpi=300, bbox_inches='tight')

# For the weekdays (same process):
weekday = (
    bike_h_df
    .groupby('weekday')[['casual', 'registered']]
    .mean()
    .reindex(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    .reset_index()
    .melt(id_vars='weekday', var_name='user_type', value_name='avg_count')
)
weekday['user_type'] = weekday['user_type'].map({'casual': 'Casual', 'registered': 'Registrado'})

# Ensure the order of weekdays is correct:
weekday['weekday'] = pd.Categorical(
    weekday['weekday'],
    categories=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
    ordered=True
)

# Plotting the average number of rentals by weekday and user type:
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(
    data=weekday,
    x='weekday', y='avg_count',
    hue='user_type',
    marker='o',
    ax=ax
)
plt.xticks(rotation=45)
ax.set_title('Promedio de alquileres por día de la semana y tipo de usuario')
ax.set_xlabel('Día de la semana')
ax.set_ylabel('Promedio de alquileres')
ax.legend(title='Tipo de usuario')
ax.grid(True)
fig.tight_layout()
plt.show()

# Save the image:
fig.savefig('plot_results/weekday_bike_rentals.png', dpi=300, bbox_inches='tight')

# 3. How do weather conditions affect bike rentals?
# We select the usefully fields for the answer:
# -> weathersit ( Categorical variable ) : Represents weather conditions.
# -> cnt        ( Numerical variable )   : Represents count of total rental bikes including both casual and registered.

# Map weather codes to descriptive labels
weather_map = {
    1: "Despejado / Parcialmente nublado",
    2: "Neblina / Nublado",
    3: "Lluvia ligera / Nieve ligera",
    4: "Lluvia fuerte / Nieve / Niebla"
}
bike_d_df['weather'] = bike_d_df['weathersit'].map(weather_map)

# Compute average rentals by weather condition
weather_avg = (
    bike_d_df
    .groupby('weather')['cnt']
    .mean()
    .reset_index()
    .rename(columns={'cnt': 'avg_rentals'})
)

# Sort descending by average rentals
weather_avg = weather_avg.sort_values(by='avg_rentals', ascending=False).reset_index(drop=True)

# Prepare red→green color palette
cmap = plt.colormaps['RdYlGn']
vals = weather_avg['avg_rentals'].values
norm = mcolors.Normalize(vmin=vals.min(), vmax=vals.max())
colors = [cmap(norm(v)) for v in vals]

# Weather condition bar plot
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(weather_avg['weather'], vals, color=colors)
ax.bar_label(bars, fmt='%.0f')
ax.set_ylim(0, vals.max() * 1.15)
ax.set_title('Promedio de alquileres diarios por condición climática')
ax.set_xlabel('Condición climática')
ax.set_ylabel('Promedio de alquileres diarios')
plt.xticks(rotation=45)
fig.tight_layout()
plt.show()

# Save the image:
fig.savefig('plot_results/weather_bike_rentals.png', dpi=300, bbox_inches='tight')
