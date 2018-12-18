"""
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
# Class 풀이
# class 정의


class Deque:
    def __init__(self):
        self.list = []  # 리스트 초기화

    def push_front(self, x):
        self.list.insert(0, x)  # 정수 x를 덱앞에 넣는다.

    def push_back(self, x):
        self.list.append(x)  # 정수 x를 덱 맨뒤에 넣는다

    def pop_front(self):  # 맨앞의 정수를 빼고 출력
        try:
            print(self.list.pop(0))
        except IndexError:  # 덱에 들어있는 정수가 없다면 -1 출력
            print("-1")

    def pop_back(self):  # 맨뒤의 정수를 빼고 출력
        try:
            print(self.list.pop(-1))
        except IndexError:  # 덱에 들어있는 정수가 없다면 -1 출력
            print("-1")

    def size(self):  # 현제 덱의 리스트의 길이 = 정수의 개수를 출력한다.
        print(len(self.list))

    def empty(self):  # 덱이 비어있으면 1출력 아니면 0 출력
        if len(self.list) == 0:
            print("1")
        else:
            print("0")

    def front(self):  # 덱의 맨앞의 정수를 출력
        try:
            print(self.list[0])
        except IndexError:  # 아무것도 없으면 -1 출력
            print("-1")

    def back(self):  # 덱의 맨뒤의 정수를 출력
        try:
            print(self.list[-1])
        except IndexError:  # 아무것도 없으면 -1 출력
            print("-1")


# 실행부
r = int(input())
d = Deque()
for i in range(0,r):
    cmd = input().split()
    if cmd[0] == "push_front":
        d.push_front(cmd[1])
    elif cmd[0] == "push_back":
        d.push_back(cmd[1])
    elif cmd[0] == "pop_front":
        d.pop_front()
    elif cmd[0] == "pop_back":
        d.pop_back()
    elif cmd[0] == "size":
        d.size()
    elif cmd[0] == "empty":
        d.empty()
    elif cmd[0] == "front":
        d.front()
    elif cmd[0] == "back":
        d.back()
