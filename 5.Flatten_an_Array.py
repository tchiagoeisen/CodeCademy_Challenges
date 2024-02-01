def flatten_array(arr):
  flat_list = []

  for i in range(len(arr)):
    if type(arr[i]) == list:

      for i in arr[i]:
        flat_list.append(i)

    else:
      flat_list.append(arr[i])
      
  return flat_list
  
print(flatten_array([1, 2, [3, 4, 5], 6, [7, 8], 9]))