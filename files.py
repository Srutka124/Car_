import time


count = 0

start = (time.time())
with open('text.txt', 'r') as file:
    for line in file:
        for char in line:
            if char == '1':
                count +=1

print(time.time() - start)


with open('text.txt', 'r') as file:
    lines = file.readlines()
    res = lines[13].split(' ')
    print(res[7])

print(time.time() - start)

count1 = 0
with open('text.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split(' ')
        for number in numbers:
            count1 = count1 + int(number)

print(count1)

cr = 0
cr1 = 0
cr2 = 0
cr3 = 0
with open('text.txt', 'r') as file:
    lines = file.readlines()
    res = lines[3].split(' ')
    res1 = lines[6].split(' ')
    res2 = lines[9].split(' ')
    res3 = lines[12].split(' ')
    for r in res:
        numbers  = res
        for n in numbers:
            cr = cr + int(n)
    for r1 in res:
        numbers  = res1
        for n in numbers:
            cr1 = cr1 + int(n)
    for r2 in res:
        numbers  = res2
        for n in numbers:
            cr2 = cr2 + int(n)

    for r3 in res:
        numbers  = res3
        for n in numbers:
            cr3 = cr3 + int(n)

print(cr, cr1, cr2, cr3, (cr+cr1+cr2+cr3))