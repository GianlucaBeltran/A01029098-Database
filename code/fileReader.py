import csv

with open("TextFiles/greenhouse_gas_inventory_data_data.csv") as csvFile:
    reader = csv.reader(csvFile)

    country_exceptions = ['European Union']
    only_year_wanted = {}
    for row in reader:
        if row[1] == '2010' and row[0] not in country_exceptions:
            if row[0] in only_year_wanted.keys():
                only_year_wanted[row[0]] += float(row[2])
            else:
                only_year_wanted[row[0]] = float(row[2])

    answer = sorted(only_year_wanted.items(), key = lambda item : item[1], reverse = True)


    print(f"Respuesta 1: {answer[:5]}")


with open("TextFiles/populationbycountry19802010millions.csv") as csvFile:
    reader = csv.reader(csvFile)

    list_exceptions = ['NA', '--']
    country_exceptions = ['World', 'Asia & Oceania', 'Country', 'Africa', 'Europe', 'Central & South America', 'North America', 'Eurasia', 'Middle East']
    only_year_wanted = {}
    for row in reader:
        if row[-1] not in list_exceptions and row[0] not in country_exceptions:
            only_year_wanted[row[0]] = float(row[-1])
        
    answer = sorted(only_year_wanted.items(), key = lambda item : item[1], reverse = True)

    print(f"Respuesta 2: {answer[:5]}")


print("Respuesta 3: A simple viste podemos ver que estos datos no tienen ninguna relación, además países como China e India que se encuentran en los top 5 mas populados, no aparecen en nuestra base de datos de gases invernaderos, por lo que no los podemos relacionar. ")