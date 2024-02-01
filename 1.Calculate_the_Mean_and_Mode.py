def stats_finder(array):
  result = []
  averange_sum = 0

  for i in array:
    averange_sum += i
  averange = averange_sum / len(array)
  
  result.append(averange)
 
  mode = 0
  array_copy = array[:]
  max_counter = 0

  while array_copy:
    value = array_copy.pop()
    if value in array:
      counter = array.count(value)

      if mode == 0 and counter > 1 :
        mode = value
        max_counter = counter

      if max_counter < counter:
        mode = value
        max_counter = counter
        
      elif max_counter == counter:
        if mode > value:
          mode=value
        
  result.append(mode)
  
  return result
    
print(stats_finder([500, 400, 400, 400, 300, 375, 300, 350, 325, 300]))