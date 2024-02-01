def unique_characters(string_in):
  unique = True
  string_in = string_in.lower()
  
  if string_in == '':
    return 'Error: Empty string.'

  for i in string_in:
    counter = string_in.count(i)
    if counter > 1:
      unique = False
      break

  return unique

print(unique_characters("apple"))