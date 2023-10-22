def linear_search_product(products, target):
    indices = []
    for i in range(len(products)):
        if products[i] == target:
            indices.append(i)
    return indices
products = ["apple", "banana", "orange", "apple", "grape"]
target_product = "apple"
result = linear_search_product(products, target_product)
print(result) 