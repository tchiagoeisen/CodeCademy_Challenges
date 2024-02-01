def prime_finder(n):
  
  list_num = []

  for i in range(n, 1, -1):
    list_num.append(i)

  list_prime = list_num.copy()
  
  while list_num:
    cur_num = list_num.pop()

    for i in list_prime:
      if i % cur_num == 0 and i != cur_num:
        list_prime.remove(i)

   
  return list_prime[::-1]
 
print(prime_finder(11))