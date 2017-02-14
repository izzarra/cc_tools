from test_data import *
import sys
import json


# Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):

    # Initialize a new GameLibrary
    game_library = GameLibrary()

    for gameData in json_data['game']:
        platform = Platform(gameData['platform']['name'], gameData['platform']['launch_year'])
        game = Game(gameData['title'], platform, gameData['Year'])
        game_library.add_game(game)

    # Return the completed game_library
    return game_library

# loading in JSON stuff:
json_data = open('test_data.json')
d = json.load(json_data)
game_library = make_game_library_from_json(d)
print_game_library(game_library)

# Handling command line arguments
#  Note: sys.argv is a list of strings that contains each command line argument
#        The first element in the list is always the name of the python file being run
# Command line format: <input json filename>

default_input_json_file = "data/test_data.json"

if len(sys.argv) == 2:
    input_json_file = sys.argv[1]
    print("Using command line args:", input_json_file)
else:
    print("Unknown command line options. Using default values:", default_input_json_file)
    input_json_file = default_input_json_file

# Load the json data from the input file
# Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
# Print out the resulting GameLibrary data using print_game_library(game_library_data) in test_data.py
