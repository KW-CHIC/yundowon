import sys

num_list = list(map(int,sys.stdin.readline().split()))

min = min(num_list)

index = num_list.index(min)

new_list = num_list[index:]

max = max(new_list)

print(max - min)
