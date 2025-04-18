#cli.py
#Lauren Caldwell
#04/18/25

#Name: cli.py - command-line interface excercsie
#Synopsis: python3 cli.py pokemon (type and or base stat)
#Description: It will either show you the pokemons type the you specified or its total base stat
#depending on what arguments you specified, can also show you both at the same time.
import argparse

def get_parsed_arguments():
    parser = argparse.ArgumentParser(description='Reports the Pokemon type or total base stats')
    parser.add_argument('pokemon', metavar='pokemon', nargs='+', help='one or more Pokemon that you want to know the type of')
    parser.add_argument('--type', '-t', action= 'store_true', help='the pokemon type')
    parser.add_argument( '--stat','-s', action = 'store_true', help = 'the pokemons total base stats')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def get_pokemon_type(pokemon_name):
    data = open('pokemon.csv')
    for line in data:
        line = line.strip().split(',')
        if line[1] == pokemon_name:
            if line[3] == '':
                types = [line[2]]
            else:
                types = [line[2],line[3]]
            return types
        else:
            types= []
    return types

def get_total_stat(pokemon_name):
    data = open('pokemon.csv')
    for line in data:
        line = line.strip().split(',')
        if line[1] == pokemon_name:
            stat = [line[4]]
            return stat
        else:
            stat = []
    return stat

        
def main():
    argument = get_parsed_arguments()
    print_statement = False
    
    for pokemon in argument.pokemon:
        if argument.type:
            pokemon_type = get_pokemon_type(pokemon)
            if len(pokemon_type) == 2:
                print(f'{pokemon} first type is: {pokemon_type[0]}')
                print(f'{pokemon} second type is: {pokemon_type[1]}')
            elif len(pokemon_type) == 1:
                print(f'{pokemon} type is: {pokemon_type[0]}')
            elif print_statement == False:
                print('pokemon not in list')
                print_statement = True
        
        if argument.stat:
            stat_value = get_total_stat(pokemon)
            if len(stat_value) == 1:
                print(f"{pokemon} total base stats is {stat_value[0]}")
            elif print_statement == False:
                print('pokemon not in list')
                print_statement = True

if __name__ == '__main__':
    main()