def commonElements(set1, set2):
    elements = set1.intersection(set2)
    return elements

set_a = {1, 2, 3, 4, 5,6,9,88}
set_b = {4, 5, 6, 7,88}

result = commonElements(set_a, set_b)
print("Common Elements:", result)