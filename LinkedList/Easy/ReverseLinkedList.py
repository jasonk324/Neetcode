# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        newList = None
        current = head

        while current:
            # Temp variable to keep the rest of the list as it is 
            nextNode = current.next 
            # The next pointer of current will follow new list to be in the reverse order of the original
            current.next = newList  
            # So the new list one needs to be updated to the current node so that next loop the next of current 
            # can be equal to the value
            newList = current
            current = nextNode

        return newList
        """
        :type head: ListNode
        :rtype: ListNode
        """
        