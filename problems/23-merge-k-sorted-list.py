from typing import Optional, List


class ListNode:

  def __init__(self, val):
    self.val = val
    self.next = None



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

      value_list=[]
      for item in lists:
        temp=item
        while temp:
          value_list.append(temp.val)
          temp=temp.next

      final_list = None
      for i in range(len(value_list) - 1, -1, -1):
        node = ListNode(value_list[i])
        if final_list is None:
          final_list = node
        else:
          node.next = final_list
          final_list = node

      temp=final_list
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
      return final_list


obj=Solution()

list1=ListNode(1)
list1.next=ListNode(2)
list1.next.next=ListNode(4)


list2=ListNode(1)
list2.next=ListNode(3)
list2.next.next=ListNode(6)
x=obj.mergeKLists([[]])

temp=x
while(temp is not None):
  print(temp.val,end=' ')
  temp=temp.next
