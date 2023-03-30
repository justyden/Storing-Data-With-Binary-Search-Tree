# A node class that functions as the links for the binary tree class.

class Node:
    def __init__(self, inputStudent, inputNode1=None, inputNode2=None):
        self.student = inputStudent
        self.child1 = inputNode1
        self.child2 = inputNode2
