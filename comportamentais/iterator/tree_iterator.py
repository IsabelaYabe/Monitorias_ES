from __future__ import annotations

from typing import Optional, Iterator
from abc import ABC, abstractmethod

class TreeIterator(ABC):
    """Interface for tree iterators."""
    
    @abstractmethod
    def __iter__(self) -> Iterator[int]:
        """Returns an iterator for the tree."""
        pass    
    
    @abstractmethod
    def __next__(self) -> int:
        """Returns the next value in the iteration."""
        pass    

class BinaryTreeIterator(TreeIterator):
    """Iterator for binary trees."""
    def __init__(self, tree: Optional[BinaryTree]):
        self._stack: list[Tree] = []
        self._push_left_branch(tree)

    def _push_left_branch(self, node: Optional[BinaryTree]) -> None:
        """Pushes all left children of a node onto the stack."""
        while node is not None:
            self._stack.append(node)
            node = node.left

    def __iter__(self) -> BinaryTreeIterator:
        return self

    def __next__(self) -> int:
        if not self._stack:
            raise StopIteration
        
        node = self._stack.pop()
        value = node.root
        self._push_left_branch(node.right)
        return value

class TernaryTreeIterator(TreeIterator):    
    """Iterator for ternary trees."""
    def __init__(self, tree: Optional[TernaryTree]):
        self._stack: list[TernaryTree] = []
        self._push_left_branch(tree)

    def _push_left_branch(self, node: Optional[TernaryTree]) -> None:
        """Pushes all left children of a node onto the stack."""
        while node is not None:
            self._stack.append(node)
            node = node.left

    def __iter__(self) -> TernaryTreeIterator:
        return self

    def __next__(self) -> int:
        if not self._stack:
            raise StopIteration
        
        node = self._stack.pop()
        value = node.root
        self._push_left_branch(node.middle)
        self._push_left_branch(node.right)
        return value