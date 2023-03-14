import app.utils

def country_population_growth():
    country = input('País:  ')
    DATA = app.utils.read_data(filepath = './app/data.csv')
    labels, values = app.utils.country_population_growth(DATA, country)
    return app.utils.chart_bar(labels, values)
    


def continental_population_by_country():
    continent = input('Continente:  ')
    DATA = app.utils.read_data(filepath = './app/data.csv')
    labels, values = app.utils.continental_population_by_country(DATA, continent)
    return app.utils.chart_barh(labels, values, continent)



def world_population_by_continent():
    continents = ['Europe', 'Asia', 'Africa', 'Oceania', 'North America', 'South America']
    DATA = app.utils.read_data(filepath = './app/data.csv')
    labels, values = app.utils.world_population_by_continent(DATA, continents)
    return app.utils.chart_pie(labels, values)



def population_growth_comparison():
    country = input('País:  ')
    DATA = app.utils.read_data(filepath = './app/data.csv')
    x, y = app.utils.country_population_growth(DATA, country)
    return x, y



def run():
    print('''[P]oblación por pais
[E]l porcentage de países por continente
[T]otal de la Población mundial por continente
[C]omparación entre dos países''')
    letter = input('tecleé la letra: ')

    if letter == 'P':
        country_population_growth()


    if letter == 'E':
        continental_population_by_country()


    if letter == 'T':
        world_population_by_continent()
                                

    if letter == 'C':
        x, y = population_growth_comparison()
        x1, y1 = population_growth_comparison()  
        app.utils.chart_line(x, y, x1,y1)

    
     
if __name__ == '__main__':
    run()
    
    

    
    
    
    


