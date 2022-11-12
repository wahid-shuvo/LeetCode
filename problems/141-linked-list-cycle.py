from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      temp=head
      pointer_list=[]
      flag=False
      while temp is not None:
        if temp.next in pointer_list:
          flag=True
          break
        pointer_list.append(temp.next)
        temp=temp.next
      return flag

pos=1
list=LinkedList()
list.head=ListNode(1)
list.head.next=ListNode(2)
# list.head.next.next=ListNode(0)
# list.head.next.next.next=ListNode(-4)
list.head.next=list.head
obj=Solution()
print(obj.hasCycle(list.head))