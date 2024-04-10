# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    if list1 == None:
        return list2
    if list2 == None:
        return list1
    head = None
    if list1.val > list2.val:
        head = list2
        list2 = list2.next
    else:
        head = list1
        list1 = list1.next
    current = head
    while list1 != None or list2 != None:
        if list1 == None:
            current.next = list2
            current = current.next
            list2 = list2.next
            continue
        elif list2 == None:
            current.next = list1
            current = current.next
            list1 = list1.next
            continue
        if list1.val > list2.val:
            current.next = list2
            current = current.next
            list2 = list2.next
        else:
            current.next = list1
            current = current.next
            list1 = list1.next

    return head
