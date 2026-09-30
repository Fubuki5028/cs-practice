print('Ввод')
temp = int(input())
n = int(input())
count = 0
count_error = 0
for _ in range(n):
    res = input()
    print(res)
    count += 1
    if res == 'error':
        count_error +=1
print('Вывод:',count,count_error)
    
