from operations import *
import json


def get_constants(filename):
    file = open(filename, "r")
    constants = json.load(file)
    file.close()
    return constants


def generate_statement(json_file):
    constants = get_constants(json_file)

    has_backend_labels = is_in(labels, constants["labels"])
    is_story = is_in(issuetype, global_constants[issuetype])
    has_summary = is_in(summary, constants[summary])
    is_issue = is_in(issuetype, "Subtask")

    return combine([
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
    ])
