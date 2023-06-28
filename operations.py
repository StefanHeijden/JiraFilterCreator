AND = "AND"
NAND = "AND NOT"
OR = "OR"
NOR = "OR NOT"
labels = "labels"
bouwteams = "Bouwteams"
summary = "summary"
issuetype = "issuetype"


def create_statement(statement, operator=None, many=False):
    if operator is not None:
        return {
            "statement": ("(" if many else "") + statement + (")" if many else ""),
            "operator": operator
        }
    return {
        "statement": ("(" if many else "") + statement + (")" if many else "")
    }


def combine(statements):
    combined_statement = ""
    for statement in statements:
        if "operator" in statement:
            combined_statement = f"{combined_statement} {statement['operator']} {statement['statement']}"
        else:
            combined_statement = statement['statement']
    return combined_statement


def is_in(field, entries, in_value="in"):
    seperator = '", "'
    return f'{field} {in_value} ("{seperator.join(entries)}")'


def subtask_of(statement):
    return f'parent of subtasks({statement})'
