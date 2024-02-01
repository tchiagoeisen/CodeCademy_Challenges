def fizzbuzz(limit):
  # Write your code here
  fizzbuzz_list = []

  for i in range(1,limit+1):

    if i % 3 == 0 and i % 5 == 0:
      fizzbuzz_list.append('FizzBuzz')

    elif i % 3 == 0:
      fizzbuzz_list.append('Fizz')

    elif i % 5 == 0:
      fizzbuzz_list.append('Buzz')

    else:
      fizzbuzz_list.append(i)

  return fizzbuzz_list

print(fizzbuzz(16))
