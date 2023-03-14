import matplotlib.pyplot as plt

# Presento esta forma de acceder archivo csv, luego de probar todas las posibilidades
# solo me aseguré de eliminar las comas dentro de las celdas
# y luego de comprender que es un generador

def read_data(filepath = './app/data.csv'):
    with open(filepath, 'r', encoding='cp1252') as f:
        header = list(next(f).strip().split(','))   # sobre el método readline del objeto file
    
        DATA = []
        for line in f.readlines():  # método readlines del objeto file
            DATA.append(dict(zip(header, line.strip().split(','))))

        return DATA



def world_population_by_continent(DATA, continents):
    percentage = []
    for w in range(len(continents)):
        percentage_by_country = sum([float(data["World Population Percentage"]) for data in DATA if data['Continent'] == continents[w]])
        percentage.append(percentage_by_country)

    return continents, percentage    
        


def continental_population_by_country(DATA, continent):
    percentage_by_country = {data['Country/Territory']: float(data["World Population Percentage"]) for data in DATA if data['Continent'] == continent}

    labels = list(percentage_by_country.keys())
    values = list(percentage_by_country.values())

    return labels, values

        

def country_population_growth(DATA, country):
    country_dictionary = {data['Country/Territory']: data for data in DATA if data['Country/Territory'] == country}
    contry_tuples_list = list(country_dictionary[country].items())

    labels = [label[0] for label in contry_tuples_list[-5:-13:-1]]
    labels = [w.replace('Population', '').strip() for w in labels]
    values = [value[1] for value in contry_tuples_list[-5:-13:-1]]

    return labels, values

    

def chart_pie(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    
    return plt.show()


 
def chart_bar(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    
    return plt.show()



def chart_barh(labels,values,continent):
    plt.barh(labels, values, height = 0.4)
    plt.xlabel('Porcentage')
    plt.title('Población de ' + continent + ' ' + str(sum(values)) + ' % del total del mundo' )
    return plt.show()



def chart_line(x, y, x1,y1):
    plt.plot(x,y, 'b')
    plt.plot(x1,y1, 'r')
        
    return plt.show()
           
