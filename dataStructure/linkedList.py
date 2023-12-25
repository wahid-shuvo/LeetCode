class Node:
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

class SLinkedList:
  def __int__(self):
    self.headval=None

  #FUnction for printing linked list
  def listPrint(self):
    printVal=self.headval
    while printVal is not None:
      print(printVal.dataval)
      printVal=printVal.nextval

  #Inserting value at the begining
  def AtBegining(self,newdata):
    NewNode=Node(newdata)
    NewNode.nextval=self.headval
    self.headval=NewNode

  # Function to add node
  def Inbetween(self, middle_node, newdata):
    if middle_node is None:
      print("The mentioned node is absent")
      return

    NewNode = Node(newdata)
    NewNode.nextval = middle_node.nextval
    middle_node.nextval = NewNode

  # Inserting value at the end
  def AtEnd(self,newdata):
    NewNode=Node(newdata)
    if list.headval is None:
      self.headval=NewNode
      return
    last=self.headval
    while(last.nextval):
      last=last.nextval
    last.nextval=NewNode

  #Function to remove node
  def RemoveNode(self,Removekey):
    HeadVal=self.headval
    if HeadVal is not None:
      if HeadVal.dataval == Removekey:
        self.headval=HeadVal.nextval
        HeadVal=None
    while (HeadVal is not None):
      if HeadVal.dataval == Removekey:
        break
      prev = HeadVal
      HeadVal = HeadVal.nextval

    if (HeadVal == None):
      return

    prev.nextval = HeadVal.nextval
    HeadVal = None




list=SLinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3

list.AtBegining("Sun")

list.AtEnd("Thu")

list.Inbetween(list.headval.nextval,"Fri")

list.listPrint()
list.RemoveNode("Fri")
print("AFter deletion")
list.listPrint()
