def product_of_the_others(array):
  pointer = 0
  product_of_the_others = []
  product_of_array = 1

  
  while pointer < len(array):
    product_of_array = array[pointer]
    product_of_array = 1

    for i in range(0, len(array)):
      if pointer == i:
        continue
      
      else: 
        product_of_array *= array[i]
        
    product_of_the_others.append(product_of_array)
    pointer += 1
  
  return product_of_the_others
 
print(product_of_the_others([1,2,3,4,5]))