def find_volume(radius):
    volume = 4/3 * 3.14 * radius**3
    return volume

r = float(input())
print(find_volume(r))