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

#9.1 
def check(l):
    result = true
    for i in range(num - 1):
      if l[i] > l[i + 1]:
        result = false
        break
    return result
    
num_of_element = int(input("Enter the number of elements in series: "))
series = list(map(int, input("Enter the numbers, separated by space: ").split()))
num_of_order = int(input("Enter the number of the order: "))
num_required = 0
for i in range(num_of_order):
  if check(series):
    break
  num_required++
  order = tuple(map(int, input("Enter two numbers to switch, separated by space: ").split()))
  a, b = order
  temp = series[a]
  series[a] = series[b]
  series[b] = temp

if check(serise):
  print(num_required)
else:
  print(-1)

#9.2
def max_mod(dev, cards):
  max = 0
  for i in range(num_card):
    if cards[i] % dev == (dev - 1):
      max = dev - 1
      break
    if (cards[i] % dev) > max:
      max = (cards[i] % dev)
  return max
      
num_card, num_question = map(int, input("Enter the number of cards and questions, separated by space: ").split())
list_cards = list(map(int, input("Enter the numbers on card, separated by space: ").split()))
for i in range(1, num_question + 1):
  question = int(input("Enter the number of devider: "))
  print(max_mod(question, list_cards))

#9.3
  
  
    
