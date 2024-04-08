def merge_dictionaries(*dicts):
    result = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            result[key] = result.get(key, 0) + value
    return result


# Użycie:
print(merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4}))  # wypisze: {"a": 1, "b": 5, "c": 4}
