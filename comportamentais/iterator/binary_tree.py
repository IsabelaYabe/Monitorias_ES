from __future__ import annotations

from typing import Optional, Iterator
from logger import logger

from .tree_iterator import BinaryTreeIterator

class BinaryTree:
    """Binary tree node."""

    def __init__(self, root: int, *, left: Optional[BinaryTree] = None, right: Optional[BinaryTree] = None):
        self.root = root
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """String representation of the tree node."""
        return str(self.root)

    def __iter__(self) -> Iterator[int]:
        """Returns an iterator for the tree."""
        return BinaryTreeIterator(self)

    
def main():
    """Demonstration of BinaryTree and its iterator."""
    tree_left = BinaryTree(5, left=BinaryTree(2), right=BinaryTree(8))
    tree_right = BinaryTree(13, right = BinaryTree(15))
    tree = BinaryTree(11, left=tree_left, right=tree_right)
    
    logger.debug(f"Root: {tree}")
    logger.debug("Tree traversal:")
    for node in tree:
        logger.info(node)
        
    logger.debug("Tree traversal again:")
    for node in tree:
        logger.info(node)

    logger.debug(f"List of nodes: {list(tree)}")

if __name__ == "__main__":
    main()