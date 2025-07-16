grid = [
    [3, 7, 2, 9],
    [1, 5, 12, 8],
    [4, 0, 6, 2]
]
largest = grid[0][0]
for row in grid:
    for number in row:
        if number > largest:
            largest = number
print("The largest number is:", largest)

