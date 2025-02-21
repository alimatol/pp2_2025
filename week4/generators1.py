def square_generator(n):
    for i in range(n+1):
        yield i**2

N = int(input())
gen = square_generator(N)
for square in gen:
    print(square)