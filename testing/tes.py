lists = [2, 3, 4, 5]
counter = 0
arr = [1, 9]
for value in range(len(lists)):
    if counter == 0:
        lists += arr
    counter += 1
print(lists)
