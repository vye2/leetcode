# Python program to do inorder traversal without recursion

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative function for inorder tree traversal
def inOrder(root):

    # Set current to root of binary tree
    current = root
    stack = [] # initialize stack
    done = 0

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left


        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.data, end=" ") # Python 3 printing

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break

    print()

# Driver program to test above function

""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)
# 4 2 5 1 3
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# Iterative function to perform in-order traversal of the tree
def inorderIterative(root):

	# create an empty stack
	stack = deque()

	# start from root node (set current node to root node)
	curr = root

	# if current node is None and stack is also empty, we're done
	while stack or curr:

		# if current node is not None, push it to the stack (defer it)
		# and move to its left child
		if curr:
			stack.append(curr)
			curr = curr.left
		else:
			# else if current node is None, we pop an element from the stack,
			# print it and finally set current node to its right child
			curr = stack.pop()
			print(curr.data, end=' ')

			curr = curr.right
