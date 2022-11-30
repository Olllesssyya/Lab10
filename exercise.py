x = 'example.txt'
f = open(x, "rt")
b = f.read()
print(b)
y = 'result.txt'
f2 = open(y, "w")
c = f.read()
with open('example.txt', 'rt') as file:
    text = file.read()
for i in "0123456789":
    f2.writelines('Цифр:' f"{i} {text.count(i)}" + '\n')
print("Запис виконано")
f.close()
f2.close()