T = int(input())
for i in range(T):
  num = int(input())
  m = 0
  for n in range(2,num):
    if num % n == 0 :
      m += 1
      continue
    else:
      continue
  if m == 0:
    print(f"{num} eh primo")
  else:
    print(f'{num} nao eh primo')