import re
import sys
from ast import literal_eval


def main(param):
    try:
        param = validate(param)
    except ValueError as ve:
        print(f"Cannot parse input: {ve}", file=sys.stderr)
        sys.exit(1)


def validate(param):
    if type(param) == str:
        param = literal_eval(param)  # throws a ValueError if un-eval-able
    if type(param) != dict or "data" not in param.keys():
        raise ValueError("Expected keyword 'data' not found")
    if type(param["data"]) != dict or "attributes" not in param["data"].keys():
        raise ValueError("Expected keyword 'attributes' not found")
    if type(param["data"]["attributes"]) != dict or "list" not in param["data"]["attributes"].keys():
        raise ValueError("Expected keyword 'list' not found")

    paramlist = param["data"]["attributes"]["list"]
    if type(paramlist) != list or len(paramlist) < 1:
        raise ValueError("Empty data.attribute.list, needs at least one element")
    for query in paramlist:
        if type(query) != dict or \
                "date" not in query.keys() or \
                ("power" not in query.keys() and "value" not in query.keys()) or \
                len(query.keys()) != 2 or \
                not re.match(r"\d{4}-\d{2}-\d{2}", query["date"]) or \
                not re.match(r"\d+", query.get("value") or query.get("power")):
            # I assume that the query can either be 'power' or 'value'
            raise ValueError(f"Malformed query: {query}")
    return param


if __name__ == '__main__':
    main(sys.argv)
