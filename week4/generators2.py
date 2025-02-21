def even_generators(n):
    for i in range(0, n+1, 2):
        yield i

N = int(input())
gen = even_generators(N)


print(", ".join(str(num) for num in even_generators(N)))