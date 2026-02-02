#implement stack using array
#Fixed Size Array
class Stack:
    def __init__(self,size):
        self.top=-1
        self.stack=[0]*size
    def push(self,x):
        if self.top==len(self.stack)-1:
            print("Overflow...")
            return
        self.top+=1
        self.stack[self.top]=x
    def pop(self):
        if self.top==-1:
            print("Underflow...")
            return
        x=self.stack[self.top]
        self.top-=1
        print("Popped element is:",x)
    def display(self):
        if self.top==-1:
            print("Stack is empty")
            return
        print(self.stack[:self.top+1])

s=Stack(5)
for i in range(5):
    x=int(input())
    s.push(x)
# # print("Want to add more elements?Add:",end='')
# # x=int(input())
# s.push(x)
s.display()
s.pop()
s.display()