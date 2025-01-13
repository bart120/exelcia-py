import requests
import pandas
import numpy

url = "https://api.open-meteo.com/v1/forecast"
params_value ={
    "latitude": 16.2333,
    "longitude":-61.5167,
    "hourly": "temperature_2m",
    "timezone": "Europe/Paris"
}

reponse = requests.get(url, params=params_value)
if reponse.status_code == 200:
    donnees = reponse.json()
    
else:
    print("Erreur dans la récupération de données.")
    exit()

heures = donnees['hourly']['time']
temperatures = donnees['hourly']['temperature_2m']
#print(len(heures))
df = pandas.DataFrame({
    "Heure": heures,
    "Temp": temperatures
})
print("aperçu")
print(df, "\n")

df_25 = df[df["Temp"]< 25 ]
df_aprem = df[(df["Heure"].dt is not None)&(df["Heure"].dt.hour) >= 12 & (df['Heure'].dt.hour <= 23) ]
tab_temperatures = numpy.array(df_25['Temp'])

#print(tab_temperatures)
if len(tab_temperatures) > 0:  
    min_temp = numpy.min(tab_temperatures)
    max_temp = numpy.max(tab_temperatures)
    moy_temp = numpy.mean(tab_temperatures)

    print(min_temp)
    print(max_temp)
    print(moy_temp)
