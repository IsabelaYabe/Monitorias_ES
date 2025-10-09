from __future__ import annotations

from typing import Iterator, Optional
from logger import logger

from .tree_iterator import TernaryTreeIterator

class TernaryTree:
    """Ternary tree node."""
    def __init__(self, root: int, *, left: Optional[KNodeTree] = None, middle: Optional[KNodeTree] = None, right: Optional[KNodeTree] = None):
        self.root = root
        self.left = left
        self.middle = middle
        self.right = right

    def __str__(self) -> str:
        """String representation of the tree node."""
        return str(self.root)

    def __iter__(self) -> Iterator[int]:
        """Returns an iterator for the tree."""
        return TernaryTreeIterator(self)

def main():
    """Demonstration of TernaryTree and its iterator."""
    tree_left = TernaryTree(13, left=TernaryTree(1), middle=TernaryTree(7), right=TernaryTree(23))
    tree_right = TernaryTree(42, right = TernaryTree(51))
    tree = TernaryTree(36, left=tree_left, right=tree_right)
    
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