class Stack:
  def __init__(self):  #stores the data in the form of list but realluy data structure s
       self.items=[]
  def is_empty(self):
      return len(self.items)==0 # returns true if the dat structures  is empty
  def push(self,data):
      self.items.append(data)# to use add data into stack
  def pop(self)  :
      if not self.is_empty() :  # to  remove the last element of list which is the first elemrnt of stack 
        return self.items.pop()                     
      else:
          raise IndexError("stack is empty")
  def peek(self):
      if not self.is_empty():
          return self.items[-1]
      else:
          raise IndexError("stack is empty")
  def size(self):
      return len(self.items)
s1=Stack()
#s1.push(10)
#s1.push(20)
#s1.push(30)
#print("top element is",s1.peek())
print(s1.is_empty())











      