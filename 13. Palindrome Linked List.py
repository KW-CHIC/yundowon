import sys

num_list = list(map(int,sys.stdin.readline().split()))

fPoint = 0

LPoint = len(num_list) - 1


for _ in range((LPoint + 1 )// 2 ):
    if num_list[fPoint] != num_list[LPoint]:
        print("false")
        exit(0)
    fPoint += 1
    LPoint -= 1

print("true")
