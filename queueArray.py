#implement queue using array
#fixed queue
class Queue:
    def __init__(self,size):
        self.front=0
        self.rear=-1
        self.queue=[0]*size
    def enqueue(self):
        print("Input number: ",end=" ")
        x=int(input())
        if self.rear==len(self.queue)-1:
            print("Overflow...")
            return
        self.rear+=1
        self.queue[self.rear]=x
    def dequeue(self):
        if self.front>self.rear:
            print("Underflow...")
        print("Dequeued element is: ",self.queue[self.front])
        self.front+=1
    def display(self):
        if self.front>self.rear:
            print("Queue is empty")
            return
        print(self.queue[self.front:self.rear+1])
q=Queue(5)
for i in range(5):
    q.enqueue()
q.display()
q.dequeue()
q.display()
