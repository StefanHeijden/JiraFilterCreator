from operations import *


def generate_has_dod_story():
    has_dod = is_in(summary, "dod")
    return combine([
        [
            "NOT",
            subtask_of(has_dod)
        ],
        "AND",
        backlog_filter()
        ])


print(generate_has_dod_story())