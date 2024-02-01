def score_sorter(array, top_score):
  sort_score = []
  while array:
    max_value = max(array)
    sort_score.append(max_value)
    array.remove(max_value)
  return sort_score

print(score_sorter([1, 2, 3, 9999, 13], 10000))