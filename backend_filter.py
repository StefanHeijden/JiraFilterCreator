from operations import *
import json


def print_statement(filename):
    file = open(filename, "r")
    backend = json.load(file)
    file = open("values/constants.json", "r")
    constants = json.load(file)

    has_backend_labels = is_in(labels, backend["labels"])
    is_story = is_in(issuetype, constants[issuetype])
    has_summary = is_in(summary, backend[summary])
    is_issue = is_in(issuetype, "Subtask")

    print(combine([
        [
           is_story,
           "AND",
           [
               has_backend_labels,
               "OR",
               parent_of(has_summary)
           ]
        ],
        "OR",
        [
            is_issue,
            "AND",
            [
               has_summary,
               "OR",
               subtask_of(has_backend_labels)
            ]
        ]
    ]))


print_statement("values/backend.json")
print_statement("values/frontend.json")
print_statement("values/ops.json")
print_statement("values/testers.json")
