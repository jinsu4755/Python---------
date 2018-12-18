"""
push X: 정수 X를 큐에 넣는 연산이다.

pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 큐에 들어있는 정수의 개수를 출력한다.

empty: 큐가 비어있으면 1, 아니면 0을 출력한다.

front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""


# class 풀이

# Class 정의
class Queue:
    def __init__(self):
        self.list = []
        # class에서 list를 초기화

    def push(self, x):
        self.list.append(x)
        # push명령어로 입력받은 x를 list에 추가한다.

    def pop(self):
        try:
            print(self.list.pop(0))
            # pop명령어로 맨앞의 정수를 빼낸다.
        except IndexError:
            print("-1")
        # pop명령어로 정수를 빼다가 list에 정수가 없으면 IndexError발생

    def size(self):
        print(len(self.list))
        # size 명령어로 list의 길이를 출력한다 = 리스트에 들어있는 정수 개수

    def empty(self):
        if len(self.list) == 0:
            print("1")
        else:
            print("0")
        # empty명령어로 리스트의 길이가 0이면 1 그렇지 않으면 0을 출력

    def front(self):
        try:
            print(self.list[0])
        except IndexError:
            print("-1")
        # front 맨앞의 원소를 출력, 원소가 없는 경우 -1 출력

    def back(self):
        try:
            print(self.list[-1])
        except IndexError:
            print("-1")
        # 맨 뒤의 원소를 출력, 원소가 없는 경우 -1 출력


# 실행부

r = int(input())  # 실행 횟수 입력
q = Queue()
for i in range(0, r):  # 입력받는 반복 횟수만큼 반복 실행
    cmd = input().split(" ")
    if cmd[0] == "push":
        q.push(int(cmd[1]))
    elif cmd[0] == "pop":
        q.pop()
    elif cmd[0] == "size":
        q.size()
    elif cmd[0] == "empty":
        q.empty()
    elif cmd[0] == "front":
        q.front()
    elif cmd[0] == "back":
        q.back()
