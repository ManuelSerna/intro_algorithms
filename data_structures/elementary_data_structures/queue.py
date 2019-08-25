#************************************************
# Queue class
# FIFO
# This implementation assumes that every unused element in the queue is null.
#************************************************

class Queue():
    def __init__(self, length):
        self.length = length
        self.head = 0
        self.tail = 0
        self.Q = []
        for i in range(length):
            self.Q = self.Q + [None]

    '''
    Check:
        - If head is at index zero and tail happens to index this as the next "available" spot, then the the queue is full with the head at the beginning and the last element inserted is at the very end of the array.
        We do this by utilizing out assumption that there are no more null elements.
        
        - Both above conditions are false, thus we can insert.
    '''
    def is_full(self):
        if self.head == self.tail and self.Q[self.tail] != None:
            return True
        else:
            return False
    
    # Check if value at head is null, thus our queue must be empty.
    def is_empty(self):
        if self.Q[self.head] == None:
            return True
        else:
            return False
    
    def enqueue(self, x):
        if self.is_full():
            raise Exception("overflow!")
        else:
            self.Q[self.tail] = x
            if self.tail == self.length-1:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("underflow!")
        else:
            x = self.Q[self.head]
            self.Q[self.head] = None # maintain assumption
            if self.head == self.length-1:
                self.head = 0
            else:
                self.head += 1
            return x
    
    def print(self):
        print(self.Q)
