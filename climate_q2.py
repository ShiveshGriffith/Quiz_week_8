import matplotlib.pyplot as plt
import pandas as pd

load = pd.read_csv('climate.csv')

years = load['Year']
co2 = load['CO2']
temp = load['Temperature']



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.show()

plt.savefig("co2_temp_2.png") 

