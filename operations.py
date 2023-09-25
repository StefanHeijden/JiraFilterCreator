AND = "AND"
NAND = "AND NOT"
OR = "OR"
NOR = "OR NOT"
labels = "labels"
bouwteams = "Bouwteams"
summary = "summary"
issuetype = "issuetype"


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
    return f'{field} {in_value} {entries}'


def subtask_of(statement):
    return f"issueFunction in subtasksOf('{statement}')"


def parent_of(statement):
    return f"issueFunction in parentsOf('{statement}')"
