import random
count_m = 0

for i in range(1,10000):
    temp = []
    list = [0, 0, 0, 0, 0, 0]
    for a in range(1, 10):
        x = random.randint(0, 5)
        if x not in temp:
            temp.append(x)
        else:
            continue
        if len(temp) == 4:
            for b in temp:
                list[b] = 1
            break

    if list[0] == 0:
            count_m = count_m + 1
    else:
            for a in range(len(list) - 1):
                if list[a] == 0 and list[a+1] == 0:
                    count_m = count_m + 1
                    False



print(count_m)







