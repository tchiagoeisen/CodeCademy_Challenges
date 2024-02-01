def word_reverser(phrase):
  words = []
  word = ''

  for i in range(0,len(phrase)):

    if phrase[i] == ' ':
      words.insert(0,word.strip())
      word = ''

    elif i == len(phrase)-1:
      word += phrase[i]
      words.insert(0,word.strip())
      word = ''

    else:
      word += phrase[i]
    
  return ' '.join(words)

print(word_reverser('Codecademy rules'))
print(word_reverser("May the Fourth be with you"))

