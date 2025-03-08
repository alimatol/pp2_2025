numbers = [1, 2, 4, 32, 12, 45]

it = iter(numbers)

result = next(it)

for num in it:
    result *= num

print(result)


