times_table = []
for x in range(1, 5):
  horizontal_num = []
  for y in range(1, 5):
    horizontal_num.append(x * y)
  times_table.append(horizontal_num)
for horizontal_num in times_table:
  print(horizontal_num)
