import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
deq = deque()

for i in range(n):
    cmd = sys.stdin.readline().rstrip().split(" ")
    if cmd[0] == "push":
        deq.append(cmd[1])
    elif cmd[0] == "front":
        try:
            print(deq[0])
        except:
            print("-1")
    elif cmd[0] == "back":
        try:
            print(deq[-1])
        except:
            print("-1")
    elif cmd[0] == "pop":
        try:
            print(deq.popleft())
        except:
            print("-1")
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if len(deq):
            print("0")
        else:
            print("1")
