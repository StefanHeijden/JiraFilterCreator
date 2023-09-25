from operations import *


def generate_has_dod_story():
    has_dod = is_in(summary, "dod")
    return combine([
        [
            "NOT",
            parent_of(has_dod)
        ],
        "AND",
        backlog_filter(),
        "AND",
        is_story()
        ])


print(generate_has_dod_story())