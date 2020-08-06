def max_by_key(elements,key):
    if not elements:
        return None
    m = elements[0]
    for element in elements:
        if m[key] < element[key]:
            m = element
    return m

def filter_by_key(elements,key,treshold):
    filtered_elements = []
    for element in elements:
        if element[key] > treshold:
            filtered_elements.append(element)
    return filtered_elements 
    