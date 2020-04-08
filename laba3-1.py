import random
class Node: 
    def __init__(self, data): 
        self.data = data
        self.next = None 
        self.prev = None
            
class Queue: 
    def __init__(self): 
        self.head = None
        self.last = None
           
    def enqueue(self, data): 
        if self.last is None: 
            self.head = Node(data) 
            self.last = self.head 
        else: 
            self.last.next = Node(data) 
            self.last.next.prev = self.last 
            self.last = self.last.next
               
    def dequeue(self):    
        if self.head is None: 
            return None
        else: 
            temp = self.head.data 
            self.head = self.head.next
            self.head.prev = None
            return temp 
      
    def size(self):    
        temp = self.head 
        count = 0
        while temp is not None: 
            count = count+1
            temp = temp.next
        return count 
          
    def isEmpty(self):    
        if self.head is None: 
            return True
        else: 
            return False
               
    def printqueue(self): 
        temp = self.head 
        if self.isEmpty():
            print("queue is Empty")
        else:
            print(f"id{temp.data}", end="")
            temp = temp.next
            while temp is not None:
                print(f"->id{temp.data}", end="") 
                temp = temp.next
            print()




if __name__=='__main__':  
    M = int(input("write number of windows\n"))
    que = [Queue() for _ in range(M)]
    while True:
        command = input("\nwrite command:\n1-add person to random queue, 2-call to random window, 0-exit\n")
        if command == "1":
            name = input("write person id:\n")
            i = random.randrange(M)
            que[i].enqueue(name)
            print(f"person with id{name} added to queue №{i}")
            print(f"queue №{i} status:")  
            que[i].printqueue()

        elif command == "2":
            unEmptyQueues = [i for i in range(M) if not que[i].isEmpty()]
            if len(unEmptyQueues) != 0:
                i = random.choice(unEmptyQueues)
                print("window №{i} was chosen at random")
                print("person with id{que[i].dequeue()} left queue №{i}")
                print("queue №{i} status:") 
                que[i].printqueue()
            else:
                print("all queues are empty")
        
        elif command == "0":
            break
        
        else: 
            print("incorrect command")




