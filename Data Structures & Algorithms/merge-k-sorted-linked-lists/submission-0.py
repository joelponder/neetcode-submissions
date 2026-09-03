# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = ListNode()
        current = output
        while any(lists):
            nexts = [1001]*len(lists)
            for x in range(len(lists)):
                if lists[x]:
                    nexts[x] = lists[x].val  
            next_val = min(nexts)
            current.next = ListNode(next_val)
            current = current.next
            node_to_advance = nexts.index(next_val)
            lists[node_to_advance] = lists[node_to_advance].next
        return output.next 
                

        