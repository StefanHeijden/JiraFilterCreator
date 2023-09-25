from operations import *


def test_is_in(result, field, entries, in_value= "in"):
    print(is_in(field, entries, in_value) == result)


test_is_in("field = test", "field", "test")
test_is_in("field = test", "field", ["test"])
test_is_in("summary ~ test", "summary", ["test"])
test_is_in('field in ("test1", "test2")', "field", ["test1", "test2"])

