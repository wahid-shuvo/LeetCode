from typing import Optional


class ListNode:

  def __init__(self, val):
    self.val = val
    self.next = None



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      temp=list1
      while temp:
        node=ListNode(temp.val)
        node.next=list2
        list2=node
        temp=temp.next

      temp=list2
      next_pointer=None
      while temp:
        next_pointer=temp.next
        while next_pointer is not None:
          if temp.val>next_pointer.val:
            swap=temp.val
            temp.val=next_pointer.val
            next_pointer.val=swap
          next_pointer=next_pointer.next
        temp=temp.next
      return list2







obj=Solution()

list1=ListNode(1)
list1.next=ListNode(2)
list1.next.next=ListNode(4)


list2=ListNode(1)
list2.next=ListNode(3)
list2.next.next=ListNode(6)
x=obj.mergeTwoLists(list1,list2)

temp=x
while(temp is not None):
  print(temp.val,end=' ')
  temp=temp.next

