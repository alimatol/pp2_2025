def solve(numheads, numlegs):
    for chikens in range(0,numheads+1):
        rabits = numheads - chikens
        if(chikens*2 + rabits*4) == numlegs:
            return chikens , rabits
x = int(input())
y = int(input())

print(solve(x, y))