
def get_neighbors(arr: list, quantity: int):
    arr.sort()
    return arr[:quantity]


def get_classification(neighbors: list, quantity: int):
    nearest = get_neighbors(neighbors, quantity)
    nearest = [classification for i, classification in nearest]
    dict_classification = {key: nearest.count(key) for key in nearest}
    value = max(dict_classification, key=dict_classification.get)

    values = list(dict_classification.values())

    if values.count(dict_classification[value]) > 1:
        return False

    return value
