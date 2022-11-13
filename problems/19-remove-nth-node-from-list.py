from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

      temp=head
      length=0
      index=0
      current_index=head
      list=[]
      while temp:
        temp=temp.next
        length=length+1
      target_node_index=(length-n)
      while current_index is not None:
        if index==target_node_index:
          current_index = current_index.next
          index=index+1
          continue
        else:
          list.append(current_index.val)
        current_index=current_index.next
        index+=1

      final_list=None
      for i in range(len(list)-1,-1,-1):
        node=ListNode(list[i])
        if final_list is None:
          final_list=node
        else:
          node.next=final_list
          final_list=node

      return final_list


obj=Solution()

list1=ListNode(1)
list1.next=ListNode(2)
# list1.next.next=ListNode(3)
# list1.next.next.next=ListNode(4)
# list1.next.next.next.next=ListNode(5)
n=1

final_list=obj.removeNthFromEnd(list1,n)
temp=final_list
while(temp is not None):
  print(temp.val,end=' ')
  temp=temp.next
