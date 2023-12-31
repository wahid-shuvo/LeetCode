# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head
        prev_node = temp
        current_node=temp
        map = set()

        while current_node:
            if current_node.val not in map:
                map.add(current_node.val)
            else:
                prev_node.next = current_node.next
                current_node = current_node.next
                continue

            prev_node = current_node
            current_node = current_node.next
        return temp

def list_to_linked_list(lst):
    if not lst:
        return None
    head=ListNode(lst[0])
    current=head

    for val in lst[1:]:
        current.next=ListNode(val)
        current=current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

head_values = [1, 1, 2]
head_linked_list = list_to_linked_list(head_values)

solution = Solution()
result_head = solution.deleteDuplicates(head_linked_list)
print_linked_list(result_head)