
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
