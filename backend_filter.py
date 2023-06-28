from operations import *
import json


file = open("values/backend.json", "r")
backend = json.load(file)
file = open("values/constants.json", "r")
constants = json.load(file)

statements = [
    create_statement(is_in(issuetype, constants[issuetype])),
    create_statement(is_in(labels, backend[labels]), AND)
]

print(combine(statements))
