# 2. Add Two Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1 = 0
        p1 = 0 # To track the power (10^0, 10^1, etc)
        while l1:
            x1 += (l1.val) * (10**p1)
            l1 = l1.next
            p1 += 1
        
        x2 = 0
        p2 = 0
        while l2:
            x2 += (l2.val) * (10**p2)
            l2 = l2.next
            p2 += 1

        total_sum = x1 + x2
        
        # To build the result, start with a dummy node
        dummy = ListNode(0)
        current = dummy
        
        # Special case: if sum is 0, the loop below won't run
        if total_sum == 0:
            return ListNode(0)

        # Convert the integer back to a linked list
        while total_sum > 0:
            digit = total_sum % 10
            current.next = ListNode(digit)
            current = current.next
            total_sum //= 10
            
        return dummy.next


        

             


# take the list and traverse through it , take the first element and multiple by the power of 10 to the power
# of the index , keep on doing it till you finish the traversel
# take the second list and repeat it, ones both the list have been traversed then add them up and then break down 
# the final ressult. Take the number and with each power of 10 take the modulus and fit into the linked list and print it out.

