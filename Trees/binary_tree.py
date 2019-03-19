#myTree = ['a',['b', ['d', [], []], ['e', [], []] ], ['c', ['f', [], []], ['g', [], []], ] ] 
	       #root#left tree   						#right tree

"""
def BinaryTree(r):
	return [r,[], []]

def insertLeft(root, newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[], []])
	return root

def insertRight(root, newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch, [], t])
	else:
		root.insert(2,[newBranch,[],[]])

def getRootVal(root):
	return root[0]

def setRootVal(root,newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]


r = BinaryTree('a')
insertLeft(r,'b')
insertRight(getLeftChild(r), 'd')

insertRight(r,'c')
insertLeft(getRightChild(r), 'e')
insertRight(getRightChild(r), 'f')
print(r)
"""

class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj
		
	def getRootVal(self):
		return self.key

























