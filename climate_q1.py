import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

years = []
co2 = []
temp = []

cursor.execute("SELECT Year, C02, Temperature FROM ClimateData")
result = cursor.fetchall()

for row in result:
    year.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

connection.close()


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

plt.savefig("co2_temp_1.png") 
