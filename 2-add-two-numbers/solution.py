# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        iter1, iter2 = l1, l2
        carry_over, dest = 0, ListNode(0)
        dest_iter = dest
        while iter1 or iter2:
            val1 = iter1.val if iter1 else 0
            val2 = iter2.val if iter2 else 0

            dest_iter.val = (val1 + val2 + carry_over) % 10
            carry_over = (val1 + val2 + carry_over) / 10

            iter1 = iter1.next if iter1 else None
            iter2 = iter2.next if iter2 else None
            if iter1 or iter2 or carry_over:
                dest_iter.next = ListNode(carry_over)
                dest_iter = dest_iter.next
        return dest
