#Task 3
import random

#Task 3.1
class Tree:
    def __init__(self,data):
        self.left_pointer = None
        self.right_pointer = None
        self.data = data

    def insert_node(self,new_data):
        if new_data < self.data:
            if self.left_pointer == None:
                self.left_pointer = Tree(new_data)
            else:
                self.left_pointer.insert_node(new_data)
        else:
            if self.right_pointer == None:
                self.right_pointer = Tree(new_data)
            else:
                self.right_pointer.insert_node(new_data)

    def in_order_traversal(self):
        if self.left_pointer != None:
            self.left_pointer.in_order_traversal()

        print(self.data)

        if self.right_pointer != None:
            self.right_pointer.in_order_traversal()

    def post_order_traversal(self):
        if self.left_pointer != None:
            self.left_pointer.post_order_traversal()
            
        if self.right_pointer != None:
            self.right_pointer.post_order_traversal()
        

        print(self.data)
            

data = random.randint(0,999)
tree = Tree(data)
for i in range(9):
    data = random.randint(0,999)
    tree.insert_node(data)

tree.in_order_traversal()
print()
tree.post_order_traversal()
