def flatten(sublist):
  flat_list = [item for l in sublist for item in l]
  return flat_list
print(flatten([[1, 2, 3], [4, 5, 6], [7], [8, 9]]))
print("welcome")
