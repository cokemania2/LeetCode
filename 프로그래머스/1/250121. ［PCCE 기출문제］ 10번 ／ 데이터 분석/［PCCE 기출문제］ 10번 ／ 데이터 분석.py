def find_column(ext):
    if ext == "code":
        return 0
    elif ext == "date":
        return 1
    elif ext == "maximum":
        return 2
    return 3


def solution(data, ext, val_ext, sort_by):
    filtered_data = list(filter(lambda x: x[find_column(ext)] < val_ext, data))
    sorted_data = sorted(filtered_data, key = lambda x: x[find_column(sort_by)])
    return sorted_data