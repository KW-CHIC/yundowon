# 배열 파티션 I

# 입력
# 1 4 3 2
# 출력
# 4

# 처음 풀이

import sys

num_list = list(map(int,sys.stdin.readline().split()))

num_list.sort()
answer = 0
for i in range(len(num_list) - 1):
    if i % 2 == 0:
        answer += num_list[i]
print(answer)
