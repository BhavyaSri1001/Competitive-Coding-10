# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    """Time complexity-O(1)
    Space compexity-O(1)"""
    def __init__(self, iterator):
        self.iterator=iterator
        self.nextEle=self.iterator.next() if self.iterator.hasNext() else None
        
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        

    def peek(self):
        return self.nextEle
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        

    def next(self):
        temp=self.nextEle
        self.nextEle=self.iterator.next() if self.iterator.hasNext() else None
        return temp
        """
        :rtype: int
        """
        

    def hasNext(self):
        return self.nextEle!=None
        
        """
        :rtype: bool
        """
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].