class Node: 
    def __init__(self, data, key): 
        self.data = data
        self.key = key
        self.next = None 
        self.prev = None
            
class Queue: 
    def __init__(self): 
        self.head = None
        self.last = None
           
    def enqueue(self, data, key): 
        if self.isEmpty(): 
            self.head = Node(data, key) 
            self.last = self.head 
        else: 
            temp = self.last
            while True:
                if temp == self.last and temp.key >= key:
                    self.last.next = Node(data, key) 
                    self.last.next.prev = self.last 
                    self.last = self.last.next
                    break
                elif temp == None:
                    self.head.prev = Node(data, key) 
                    self.head.prev.next = self.head
                    self.head = self.head.prev
                    break
                elif temp.key >= key:
                    x = Node(data, key)
                    x.prev = temp
                    x.next = temp.next
                    temp.next.prev = x
                    temp.next = x
                    break
                temp = temp.prev
               
    def dequeue(self):    
        if self.isEmpty(): 
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
        temp = self.last 
        if self.isEmpty():
            print("queue is Empty")
        else:
            print(f"(data {temp.data}: priority {temp.key})", end="")
            temp = temp.prev
            while temp is not None:
                print(f"->(data {temp.data}: priority {temp.key})", end="") 
                temp = temp.prev
            print()


if __name__=='__main__':
    que = Queue()
    while True:
        command = input("\nwrite command:\n1-enqueue with priority, 2-dequeue, 0-exit\n")
        if command == "1":
            data = input("write data:\n")
            key = int(input("write key(int):\n"))
            que.enqueue(data, key)
            print("queue status:")  
            que.printqueue()

        elif command == "2":
            if not que.isEmpty():
                x = que.dequeue()
                print(f"dequeued (data {x.data}: key {x.key})")
                print("queue status:") 
                que.printqueue()
            else:
                print("queue is empty")
        
        elif command == "0":
            break
        
        else: 
            print("incorrect command")