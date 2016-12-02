def word_count(statement):
  results = {}
  S = statement.split()
  for word in S:
    if word not in results:
      results[word] = 1
    else:
      results[word] += 1
  return results

print(word_count("olly olly in come free"))    
