zxc=[3, 10, 100, 7, 5]
#если вы умный человек то можете найти с помощью sort, это очень сложно я знаю
for i in range(len(zxc)):
    for j in range(i + 1, len(zxc)):

        if zxc[i] > zxc[j]:
            zxc[i], zxc[j] = zxc[j], zxc[i]

print(zxc)
