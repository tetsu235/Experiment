count = 0
def update(t, l):
  global count
  a, b = t
  if compare(a, b):
    print(-1)
  else:
    count += 1

def compare(t, l):
  a, b = t
  for i in range(0, c - 2):
    if A[i] > A[i + 1]:
      return false
  return true


N = int(input())
A = []
for i in range(0, N):
  temp = int(input())
  A += temp
Q = int(input())
B = []
for i in range(0, Q):
  temp = tuple(input())
  B += temp
for i in range(0, Q):
  update(B[i], A)

if count == Q:
  print(-1)


  

