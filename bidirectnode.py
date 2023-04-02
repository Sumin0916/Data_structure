class BidirectNode:
    def __init__(self, value, prevNode: 'BidirectNode', nextNode:'BidirectNode', key = -1):
        self.value = value
        self.key = key
        self.prev = prevNode
        self.next = nextNode
