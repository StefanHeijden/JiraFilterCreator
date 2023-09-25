import json

AND = "AND"
NAND = "AND NOT"
OR = "OR"
NOR = "OR NOT"
labels = "labels"
bouwteams = "bouwteams"
sprint = "sprint"
summary = "summary"
issuetype = "issuetype"
file = open("values/constants.json", "r")
global_constants = json.load(file)
file.close()


def combine(statements):
    combined_statement = []
    for statement in statements:
        if type(statement) is list:
            combined_statement.append(f"({combine(statement)})")
        else:
            combined_statement.append(statement)

    return " ".join(combined_statement)


def is_in(field, entries, in_value="in"):
    if type(entries) is list and len(entries) > 1:
        updated_entries = []
        for entry in entries:
            if " " in entry:
                updated_entries.append(f'"{entry}"')
            else:
                updated_entries.append(entry)
        return f'{field} {in_value} ({", ".join(updated_entries)})'
    if type(entries) is list:
        entries = entries[0]
    if field == "summary":
        in_value = "~"
    else:
        in_value = "="
    if " " in entries:
        entries = '"' + entries + '"'
    return f'{field} {in_value} {entries}'


def subtask_of(statement):
    return f"issueFunction in subtasksOf('{statement}')"


def parent_of(statement):
    return f"issueFunction in parentsOf('{statement}')"


def backlog_filter():
    is_in_bouwteam = is_in("Bouwteams", global_constants[bouwteams])
    is_in_sprint = is_in("Sprint", global_constants[sprint])
    return combine([
        is_in_bouwteam,
        "AND",
        is_in_sprint
        ])


def is_story():
    return is_in(issuetype, global_constants[issuetype])

def is_issue():
    is_in(issuetype, "Subtask")