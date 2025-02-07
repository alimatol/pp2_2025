def filter_list(numbers):
    unique= []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

print(filter_list([1,1,2,6,4,3,76,23,42,1,3]))
        

    


