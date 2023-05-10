#!/usr/bin/python

class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.distance = None
        self.depth = None


def depth(root):
    if root is None:
        return 0
    left_depth = depth(root.left)
    right_depth = depth(root.right)
    return left_depth+1 if left_depth > right_depth else right_depth+1


def max_distance(root):
    max_value = 0

    def walk(root):
        if root.left is None and root.right is None:
            root.distance = 0
            root.depth = 0
        left_depth = 0
        if root.left is not None:
            walk(root.left)
            left_depth = root.left.depth

        right_depth = 0
        if root.right is not None:
            walk(root.right)
            right_depth = root.right.depth
        root.distance = left_depth + right_depth
        if root.distance > max_value:
            max_value = root.distance
    walk(root)
    return max_value
