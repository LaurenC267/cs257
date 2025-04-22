#api.py
#Lauren Caldwell
#04/21/25

#Name: api.py
#Synopsis: python3 api.py pokemon (type and or base stat)
#Description: It will either show you the pokemons type the you specified or its total base stat
#depending on what arguments you specified.
import argparse
import Flask 
import json

app = flask.Flask(__name__)

@app.route('/pokemon_type/<pokemon_name>')
def get_pokemon_type(pokemon_name):
    data = open('pokemon.csv')
    for line in data:
        line = line.strip().split(',')
        if line[1] == pokemon_name:
            if line[3] == '':
                types = [line[2]]
            else:
                types = [line[2],line[3]]
        else:
            types= []
        
        type1 = types[0]
        type2= types[1]

        return jsonify({
                    'pokemon': pokemon_name,
                    'Type 1' : type1,
                    'Type 2: ': type2})


@app.route('/pokemon_stat/<pokemon_name>')
def get_total_stat(pokemon_name):
    data = open('pokemon.csv')
    for line in data:
        line = line.strip().split(',')
        if line[1] == pokemon_name:
            stat = [line[4]]
        else:
            stat = []
    return jsonify({
                    'pokemon': pokemon_name,
                    'total_stat': stat})
    
@app.route('/help')
def get_help():
    return flask.render_template('help.html')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParse('Flask application for getting a pokemon type or stat')
    parser.add_argument('host', help= 'the host that the application is running on')
    parser.addargument('port', type=int, help = 'the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug = True)
