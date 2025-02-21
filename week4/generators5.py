def generator(n):
    for i in range(n, 0, -1):
        yield i

N = int(input())
gen = generator(N)

for num in gen:
    print(num)
