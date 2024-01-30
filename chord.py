


# Node Numbering is hashed in the hash space of 
# 2**m - 1
#
# 
# @fingerEntry: structure containing an entry in the finger table
# @start
class fingerEntry:
	def __init__(self, start, interval, successor):
		self.start = start
		self.interval = interval
		self.successor = successor

	##
	# dict - gets the dictionary object representateion of node class
	# Returns: dict objec
	##
	def dict(self):
		return self.__dict__

##
# Node - class for nodes in chord
##
class Node:
	def __init__(self, id):
		self.identifier = id
		self.predecessor = None
		self.fingerTable = [0]
		self.size = 0




	def getSuccessor(self, index):
		return self.fingerTable[index].successor

	def getSuccessorIdentifier(self, index):
		successor = self.getSuccessor(index)
		return successor.identifier

	def getFingerTableInterval(self, index):
		return self.fingerTable[index].interval

	def getPredecessor(self):
		return self.predecessor

	def getPredecessorIdentifier(self):
		return self.predecessor.identifier

	# Initializes the finger table entry of start, and interval
	# sets successors to None
	def initializeFingetTableStartInterval(self, size):
		self.size = size
		for j in range(size):
			successor = None
			start = (self.identifier + 2**j) % 2 ** size
			end = (self.identifier + 2 ** (j+1)) % 2 ** size
			interval = (start, end)
			self.fingerTable.append(fingerEntry(start, interval, successor))


	##
	# join - adds a node to an already existing network
	# @node: arbitrary node in a circular network
	##
	def join(self, node):
		if (node):
			self.initFingerTable(node)
		else:
			for i in range(1, self.size + 1):
				self.fingerTable[i].successor = self
			self.predecessor = self


	##
	# initFingerTable - initializes the new node with an existing node
	# @node: arbitrary node in the network
	##
	def initFingerTable(self, node):
		index1 = 1
		self.fingerTable[index1].successor = node.findSuccessor(self.fingerTable[index1].start)
		successor = self.getSuccessor(index1)
		self.predecessor = successor.predecessor
		successor.predecessor = self

		m = len(self.fingerTable)

		for i in range(1, m - 1):
			if (self.isValid((self.identifier, self.fingerTable[i].successor.identifier), self.fingerTable[i + 1].start)):
				self.fingerTable[i + 1].successor = self.fingerTable[i].successor
			else:
				self.fingerTable[i + 1].successor = node.findSuccessor(self.fingerTable[i + 1].start)


	##
	# updateOthers - updates other nodes in the network
	##
	def updateOthers(self):
		i = 1
		while (i <= self.size):
			p = self.findPredecessor(self.identifier - (2 ** (i-1)))
			print(p, self.identifier - (2 ** (i-1)))
			p.updateFingerTable(self, i)
			i +=1

	##
	# updateFingerTable - updates the finger table of affected nodes in the network
	# @s: node that joined the network
	# @i: index of new node's finger table
	##
	def updateFingerTable(self, s, i):

		# if (self.isValid((self.identifier, self.fingerTable[i].successor.identifier), s.identifier )):
		# 	print(s, self.identifier)
		if (self.isValid((s.identifier, self.identifier), self.fingerTable[i].successor.identifier)):

			self.fingerTable[i].successor = s
			p = self.predecessor
			p.updateFingerTable(s, i)


	##
	# checkFinger - Checks node's finger table for identifier
	# @finger: fingerEntry object
	# @id: idenitifier or key to be found in network
	# Returns: True if found or False if not
	##
	def checkFinger(self,finger, id):
		return (id == finger.start or id == finger.successor.identifier or self.isValid(finger.interval, id))

	def emptyTable(self):
		return (len(self.fingerTable) == 0)

	##
	# findSuccessor - locate the successor of a given key or id 
	# @id: identifier or key to be found
	# Returns: successor node or the id
	##
	def findSuccessor(self, id):
		if type(id) is not int:
			raise Exception("Invalid type")

		# if id == self.identifier:
		# 	return self


		# if self.emptyTable():
		# 	return self

		# for finger in self.fingerTable[::-1]:
		# 	if self.checkFinger(finger, id) == True:
		# 		return finger.successor

		tempNode = self.findPredecessor(id)
		# if tempNode == self:
		# 	return tempNode
		return tempNode.fingerTable[1].successor

	##
	# findPredecessor - asks node n to find id's predecessor
	# @id: identifier or key to be found
	# Returns: predecessor node
	##
	def findPredecessor(self, id):
		if type(id) is not int:
			raise Exception("Invalid type")

		if self.emptyTable():
			return self

		tempNode = self
		successorIndex = 1
		while(self.isValid((tempNode.identifier, tempNode.getSuccessorIdentifier(successorIndex)), id) == False):
			if tempNode == tempNode.closestPrecedingFinger(id):
				return tempNode
			tempNode = tempNode.closestPrecedingFinger(id)
			if tempNode == self:
				return tempNode

		return tempNode


	##
	# closestPrecedingFinger - return closest finger preceding id
	# @id: identifier or key
	# Returns: closest node to id
	##
	def closestPrecedingFinger(self, id):
		if self.emptyTable():
			return self

		m = len(self.fingerTable) - 1
		for i in range(m - 1, -1, -1):
			if self.isValid((self.identifier, id), self.fingerTable[i].successor.identifier):
				return self.getSuccessor(i)
		return self

	def displayFingerTable(self):
		print(f"\nID: <{self.identifier}>")
		for finger in self.fingerTable[1:]:
			print(finger.dict())


	##
	# isValid - checks if id is in the given interval following 
	# 			a circular manner
	# @interval: intervals between nodes in the network
	# @id: identifier or key
	# Return: True if id is in interval, or False if not
	##
	def isValid(self, interval, id):
		start, end = interval
		if start <= end:
			return start <= id <= end
		else:
			return start <= id or id <= end



	def __repr__(self):
		return f"Node_{self.identifier}"


##
# simulateNetwork - simulate an existing network of nodes
##
def simulateNetwork():
	NODES = [Node(0), Node(1), Node(3)]

	numberOfEntry = len(NODES)
	for node in NODES:
		node.initializeFingetTableStartInterval(numberOfEntry)

	successors = [[1, 2, 0], [2, 2, 0], [0, 0, 0]]
	index = 1
	for i, successor in enumerate(successors):
		for j in successor:
			s = NODES[j]
			NODES[i].fingerTable[index].successor = s
			index += 1
		index = 1

	# set predecessors manunally
	NODES[0].predecessor = NODES[2]
	NODES[1].predecessor = NODES[0]
	NODES[2].predecessor = NODES[1]

	return NODES

	

if __name__ == '__main__':
	NODES = simulateNetwork()


	newNode = Node(6)
	newNode.initializeFingetTableStartInterval(3)
	newNode.join(NODES[1])
	NODES.append(newNode)
	newNode.updateOthers()



	temp = NODES[1]

	# while (temp):
	# 	temp.displayFingerTable()
	# 	print(temp.identifier)
	# 	temp = temp.fingerTable[1].successor
	for node in NODES:
		node.displayFingerTable()
		print(node.predecessor , "<-", node)
		
