x = [1,2,3,4,5,6,7,8,9,10]

def size():
  count = 0
  for i in x:
    count+=1
  return count

def sum():
  sum_ = 0
  for elem in x:
    sum_ += elem
  return sum_

def max(x):
  max = 0
  for elem in x:
    if max < elem:
      max = elem
  return max