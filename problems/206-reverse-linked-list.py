#Definition for singly-linked list.
from typing import Optional

class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def printList(self):
    temp = self.head
    while (temp):
      print(temp.data, end=' ')
      temp = temp.next

class LinkedList:

  def __init__(self):
    self.head=None

class Solution:

  def reverseList(self, head: Optional[Node]) -> Optional[Node]:
    prev = None
    current = head
    next = None
    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev
    return prev

obj = Solution()

list=LinkedList()
list.head=Node(1)
list.head.next=Node(2)
list.head.next.next=Node(3)

rev_list=obj.reverseList(list.head)

temp=rev_list
while(temp is not None):
  print(temp.data,end=' ')
  temp=temp.next





