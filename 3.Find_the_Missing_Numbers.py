def missing_nos(arr, k):
  
  missing_num = []
  pointer = 0
  counter = 0

  while pointer < len(arr) - 1:

    if arr[pointer] + 1 != arr[pointer + 1]:
      missing_num.append(arr[pointer] + 1 )
      counter += 1
    pointer += 1
    
    if counter == k:
      break

  return missing_num


print(missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2))