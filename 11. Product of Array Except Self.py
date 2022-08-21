import sys

num_list = list(map(int,sys.stdin.readline().split()))

answer = []

for i in range(len(num_list)):
  
  temp = num_list[:]
  del temp[i]
  num = 1
  
  for t in temp:
    num *= t
  answer.append(num)

print(answer)
