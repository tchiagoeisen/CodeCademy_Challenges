def fib_finder(n):
  pointer = 0

  fib_list = []

  while pointer < n:
    if len(fib_list) == 0:
      fib_list.append(pointer)
      fib_list.append(pointer + 1)

    current_num = fib_list[pointer] + fib_list[pointer + 1]
    fib_list.append(current_num)
    pointer += 1
    current_num = 0

  return fib_list[n-1]

print(fib_finder(6))