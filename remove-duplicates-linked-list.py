class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    # [1, 2, 4, 4]
    # [1, 2, 2, 3]
    nums_dict = {}
    prev_node = head
    current_node = head

    while current_node is not None:

        if current_node.val in nums_dict:
            print(current_node.val)
            prev_node.next = current_node.next
        else:
            nums_dict[current_node.val] = 1
            prev_node = current_node
        current_node = current_node.next

    return head
