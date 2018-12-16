"""
문제: 백준 10828번 스택의 구현

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.

pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

size: 스택에 들어있는 정수의 개수를 출력한다.

empty: 스택이 비어있으면 1, 아니면 0을 출력한다.

top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""


# Class 사용
class Stack:
    def __init__(self):
        self.list = []  # 리스트의 초기화.

    def push(self, x):
        self.list.append(x)  # 리스트에 x라는 변수의 값을 추가하는 method

    def pop(self):
        try:
            print(self.list.pop())  # 리스트에서 가장위에 정수를 빼낸다.
        except IndexError:
            print("-1")  # 리스트가 비어있는경우 IndexError 발생, 해당 오류 발생시 실행

    def size(self):
        print(len(self.list))  # 리스트의 길이 = 현재 들어있는 정수의 개수

    def empty(self):
        if len(self.list) == 0:  # 만약 리스트가 비어있는 경우
            print("1")
        else:  # 그렇지 않은 경우
            print("0")

    def top(self):
        if len(self.list) == 0:  # 리스트가 비어있는경우
            print("-1")
        else:
            print(self.list[-1])  # 그렇지 않으면 리스트 마지막 원소를 반환하여 출력


# 실행부

r = int(input())  # 반복횟수를 입력 받는다
st = Stack()  # 클래스 사용
for i in range(0, r):  # 입력받는 반복 횟수만큼 반복 실행
    cmd = input().split(" ")
    if cmd[0] == "push":
        st.push(int(cmd[1]))
    elif cmd[0] == "pop":
        st.pop()
    elif cmd[0] == "size":
        st.size()
    elif cmd[0] == "empty":
        st.empty()
    elif cmd[0] == "top":
        st.top()