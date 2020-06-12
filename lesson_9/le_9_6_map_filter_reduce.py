from functools import reduce

values = [2, -1, 5, 8, 3, -2, ]
for square in map(lambda x: x * x, values):
    # print(square)
    pass

squares = list(map(lambda x: x ** 2, values))
print(squares)

# 2_filter
positive = list(filter(lambda x: x > 0, values))
print(positive)


# 3_reduce
product = reduce(lambda x, y: x + y, values)
print(product)
