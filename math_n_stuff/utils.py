def filter_list(lst: list):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def all_elements_same(lst):
    return len(set(lst)) == 1 if lst else True


if __name__ == "__main__":
    pass
