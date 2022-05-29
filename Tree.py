from LimitedQueue import *


class TreeNode(object):
    def __init__(self, data, parent=None, children=None):
        self._data = data
        self._parent = parent
        if parent is not None:
            parent.add_child(self)
        if children is None:
            children = []
        self._children = children

    def __eq__(self, other):
        return self._data == other.data

    def __str__(self):
        return str(self._data)

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, new_parent):
        self._parent = new_parent

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, new_children):
        self._children = new_children

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    def remove_child(self, sad_child):
        self._children.remove(sad_child)

    def add_child(self, new_child):
        self._children.append(new_child)
        new_child.parent = self

    def is_root(self):
        return self._parent is None

    def is_leaf(self):
        return self._children == []

    def num_children(self):
        return len(self._children)


class Tree(object):
    def __init__(self, root=None):
        self._root = root
        self._current = root

    @property
    def root(self):
        return self._root

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, new_current):
        self._current = new_current

    @root.setter
    def root(self, node):
        self._root = node

    def is_empty(self):
        return self._root is None

    def replace(self, old_node, new_node):
        parent = old_node.parent
        parent.children[parent.children.index(old_node)] = new_node
        new_node.parent = parent

        children = old_node.children
        new_node.children = children
        for child in children:
            child.parent = new_node

    def depth(self, node):

        parent = node.parent
        if parent is None:
            return 1
        return 1 + self.depth(parent)

    def height(self):
        return self._height(self._root)

    def _height(self, node):
        if node.is_leaf():
            return 1
        else:
            return 1 + max(self._height(x) for x in node.children)

    def preorder(self, f):
        self._preorder(self._root, f)

    def _preorder(self, node, f):
        f(node)
        for child in node.children:
            self._preorder(child, f)

    def postorder(self, f):
        self._postorder(self._root, f)

    def _postorder(self, node, f):
        for child in node.children:
            if child is not None:
                self._postorder(child, f)
        f(node)

    def breadth(self, f):
        tree_queue = LimitedQueue(500)
        tree_queue.enqueue(self._root)
        while not tree_queue.is_empty():
            node = tree_queue.dequeue()
            f(node)
            for child in node.children:
                tree_queue.enqueue(child)
