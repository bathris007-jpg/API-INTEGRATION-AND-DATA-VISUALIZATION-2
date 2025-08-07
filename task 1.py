import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

API_key = '501ada00a3ed1b1bba06627376fb6b58'
city_name = 'Bangalore'
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}"

response = requests.get(url)
data = response.json()
dates = []
temps = []
humidities = []
pressures = []
print(data)
if 'list' in data:
    for item in data.get('list',[]):
        print(item)
    else:
        print("Error: 'list' key not found in the response.")
    from datetime import datetime
    sunrise_ts=1752020293
    dt = datetime.fromtimestamp(sunrise_ts)
    print(dt)
for item in data['list']:
    dt= datetime.fromtimestamp(item['dt'])
    temp = item['main']['temp']
    humidity = item['main']['humidity']
    pressure = item['main']['pressure']

    dates.append(dt)
    temps.append(temp)
    humidities.append(humidity)
    pressures.append(pressure)

sns.set(style = "whitegrid")
fig,axs = plt.subplots(3,1,figsize=(14,10), sharex=True)


sns.lineplot(ax=axs[0],x=dates,y=temps,color="red",marker="o")
axs[0].set_title(f"Temperature Forecast for {city_name}")
axs[0].set_ylabel("Temperature (°C)")

sns.lineplot(ax=axs[1],x=dates,y=humidities,color="blue",marker="s")
axs[1].set_title("Humidity Forecast")
axs[1].set_ylabel("Humidity (%)")

sns.lineplot(ax=axs[2],x=dates,y=pressures,color="green",marker="^")
axs[2].set_title("Pressure Forecast")
axs[2].set_ylabel("Pressure (hPa)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.suptitle(f"Weather Dashboard: 5-Day Forecast for {city_name}",fontsize=18,y=1.03)
plt.show()
