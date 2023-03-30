# Create a binary search tree that has operations
# that allow it to function correctly.

from Node import *
from SortStudentData import *
from StudentData import *
import copy
import sys


class BinarySearchTree:
    # This creates the tree. If the list is empty is that is passed then
    # the tree will be empty.
    def __init__(self, inputList=[]):
        # This means the tree is empty.
        if inputList == []:
            self.rootNode = None
        else:
            # This creates the tree in order.
            self.rootNode = Node(inputList[0])
            for i in range(len(inputList) - 1):
                self.insertNode(inputList[i + 1])

    # This inserts a node in the tree in the tree at the correct spot.
    def insertNode(self, inputStudent):
        # This means the tree is empty.
        if self.rootNode == None:
            self.rootNode = Node(inputStudent)
        else:
            tempNode = self.rootNode
            nodeFound = False
            # This keeps traveling through the tree and finds the
            # place in the tree in number should be inserted at.
            while(not nodeFound):
                # Check the left side of the tree.
                if tempNode.student.student_ID > inputStudent.student_ID:
                    if tempNode.child1 == None:
                        # Create a new node at the spot.
                        tempNode.child1 = Node(inputStudent)
                        nodeFound = True
                    else:
                        tempNode = tempNode.child1
                # Check the right side of the tree.
                else:
                    if tempNode.child2 == None:
                        # Create a new node at the spot.
                        tempNode.child2 = Node(inputStudent)
                        nodeFound = True
                    else:
                        tempNode = tempNode.child2

    # Checks the tree to see if it contains a value. It returns
    # a boolean value depending on if it containes it.
    def findValue(self, inputStudentID):
        # This means the tree was empty.
        if self.rootNode == None:
            return False
        else:
            tempNode = self.rootNode
            nodeFound = False
            # This keeps checking the given node in the tree.
            while (not nodeFound):
                if tempNode.student.student_ID == inputStudentID:
                    # The number was found.
                    nodeFound = True
                elif tempNode.student.student_ID > inputStudentID:
                    if tempNode.child1 == None:
                        # The number is not in the tree.
                        break
                    else:
                        # Check the next node.
                        tempNode = tempNode.child1
                else:
                    if tempNode.child2 == None:
                        # The number is not in the tree.
                        break
                    else:
                        # Check the next node.
                        tempNode = tempNode.child2
            return nodeFound

    # Performs a pre order traversal on the tree.
    def preOrderTraversal(self, tempList=[], inputNode=None, isStart=True):
        # Checks to see if it is the first time it is called.
        if isStart:
            tempList = []
            if self.rootNode == None:
                return tempList
            else:
                inputNode = self.rootNode
        # This means there was no node found.
        if inputNode == None:
            return tempList
        # Checks another part of the tree.
        if (inputNode.child1 != None):
            self.preOrderTraversal(tempList, inputNode.child1, False)

        # Adds the value to the list.
        tempList.append(inputNode)

        # Checks another part of the tree.
        if (inputNode.child2 != None):
            self.preOrderTraversal(tempList, inputNode.child2, False)

        return tempList

    def allStudentDetails(self):
        tempList = self.preOrderTraversal()
        for i in range(len(tempList)):
            print(str(tempList[i].student.student_ID) + " " + tempList[i].student.first_Name + " " +
                  tempList[i].student.last_Name + " " + tempList[i].student.email_ID + " " + tempList[i].student.major)


# tree1 = BinarySearchTree(sortFileID("Information.txt"))
# tree1.allStudentDetails()
# student1 = Student(790124923, "Syed", "Coral",
#                   "SyCoral@gmail.com", "CMPAB_BS")
# tree1.insertNode(student1)
# tree1.allStudentDetails()
# print(tree1.findValue(790124923))
# print(tree1.findValue(790124929))
