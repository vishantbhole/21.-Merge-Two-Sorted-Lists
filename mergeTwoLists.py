
#21. Merge Two Sorted Lists
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   def __str__(self):
        # Helper method for printing linked list
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return "->".join(result)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next
