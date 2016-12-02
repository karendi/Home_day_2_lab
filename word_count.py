def words(statement):
  results = {}
  S = statement.split()
  for word in S:
    if word not in results:
      results[word] = 1
    else:
      results[word] += 1
  return results
