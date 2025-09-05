number = int(input())
number_list = [3]
ans = []

if len(number_list) < 2:
   print('Список не имеет минимальное количество чисел')
else:
  for i in range(len(number_list)):
    for j in range(1, len(number_list)):
      if number_list[i] + number_list[j] == number:
        x = sorted([i, j])
      if x not in ans: ans.append(x)
      if len(ans) == 0: print('Подходящих чисел не найдено')
      else: print(ans)
