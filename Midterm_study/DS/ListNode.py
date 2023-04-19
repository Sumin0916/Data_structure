class ListNode:
    def __init__(self, newItem, nextNode:'ListNode'):
        self.newItem = newItem
        self.nextNode = nextNode

class BidirectNode:
    def __init__(self, newItem, nextNode:'BidirectNode', prevNode:'BidirectNode'):
        self.item = newItem
        self.next = nextNode
        self.prev = prevNode