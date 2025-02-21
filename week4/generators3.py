def divisble_generator(n):
    for i in range(0, n):
        if(i%3 == 0 and i%4 ==0):
            yield i

N = int(input())
gen = divisble_generator(N)

print(", ".join(str(it) for it in divisble_generator(N)))