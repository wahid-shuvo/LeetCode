#Definition for singly-linked list.
from typing import Optional

class ListNode:

  def __init__(self, val):
    self.val = val
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
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

    list1=None
    list2=None
    list3=None
    temp=head
    count=1
    while temp is not None:
      node = ListNode(temp.val)
      if count<left and count<right:
        if list1 is None:
          list1=node
        else:
          node.next = list1
          list1 = node
      if count>right:
        if list3 is None:
          list3=node
        else:
          node.next = list3
          list3 = node
      if count>=left and count<=right:
        if list2 is None:
          list2=node
        else:
          node.next = list2
          list2 = node
      temp=temp.next
      count=count+1

    prev1 = None
    current = list1
    next = None
    while current is not None:
      next = current.next
      current.next = prev1
      prev1 = current
      current = next
    prev3 = None
    current = list3
    next = None
    while current is not None:
      next = current.next
      current.next = prev3
      prev3 = current
      current = next
    final_list=None

    if list1 is None and list3 is not None:
      final_list = list2
      last = final_list
      while last.next:
        last = last.next
      last.next = prev3
      return final_list

    elif list1 is not None and list3 is  None:
      final_list = prev1
      last = final_list
      while last.next:
        last = last.next
      last.next = list2
      return final_list

    elif list1 is not None and list3 is not None:
      final_list=prev1

      last=final_list
      while last.next:
        last=last.next
      last.next=list2

      last=final_list
      while last.next:
        last=last.next
      last.next=prev3
      return final_list
    else:
      final_list=list2
      return final_list


obj = Solution()

list=LinkedList()
list.head=ListNode(1)
list.head.next=ListNode(2)
list.head.next.next=ListNode(3)
list.head.next.next.next=ListNode(4)
list.head.next.next.next.next=ListNode(5)
list.head.next.next.next.next.next=ListNode(6)
rev_list=obj.reverseBetween(list.head,1,5)

temp=rev_list
while(temp is not None):
  print(temp.val,end=' ')
  temp=temp.next





