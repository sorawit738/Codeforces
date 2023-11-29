def f1(l, x):
  # l: is list of integer, list (contain at least 1 data).
  # x: is a single integer.
  # returns a string showing 2 numbers in the list that gives minimum value and
  # maximum value when multiplied by x.
  maxIndex = 0
  minIndex = 0
  j = 0
  while (j != len(l)):
    if l[j]*x < l[minIndex]*x:
      minIndex = j
    if l[j]*x > l[maxIndex]*x:
      maxIndex = j
    j += 1
  return str(l[minIndex]) + ' ' + str(l[maxIndex])

exec(input().strip())