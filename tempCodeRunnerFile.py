counter = 0

while counter < 9:
    counter += 1
    print(counter)
    if counter < 6:
        continue
    print(f'Contando hasta {counter}')