temp_threshold = int(input())
n = int(input())
print('Ввод',temp_threshold)
print(n)
count = 0
count_error = 0
count_exceed = 0
temp_max = float('-inf')
temp_sum = 0

for _ in range(n):
    temp = input()
    print(temp)
    count += 1
    if temp == 'error':
        count_error +=1
        continue
    temp_sum += float(temp)
    if float(temp) > temp_threshold:
        count_exceed +=1
    if float(temp) > temp_max:
        temp_max = float(temp)

print('Вывод:',count,count_error,count_exceed,temp_max,f"{temp_sum/(n-count_error):.1f}", sep = '\n')
