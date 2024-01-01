


# Node Numbering is hashed in the hash space of 
# 2**m - 1

# 
# @fingerEntry: structure containing an entry in the finger table
# @start
class fingerEntry:
	def __init__(self, start, interval, successor):
		self.start = start
		self.interval = interval
		self.successor = successor

	def dict(self):
		return self.__dict__

class Node:
	def __init__(self, id):
		self.identifier = id
		self.fingerTable = []


	# 
	# @checkFinger: Checks node's finger table for identifier
	# @finger: fingerEntry object
	# @id: idenitifier or key to be found in network
	# returns: True if found or False if not
	#
	def checkFinger(self,finger, id):
		return (id == finger.start or id == finger.successor.identifier or self.isValid(finger.interval, id))

	def emptyTable(self):
		return (len(self.fingerTable) == 0)

	# 
	# @findSuccessor: locate the successor of a given key or id 
	# @id: identifier or key to be found
	# returns: successor node or the id
	#
	def findSuccessor(self, id):
		if id == self.identifier:
			return self


		if self.emptyTable():
			return self

		for finger in self.fingerTable[::-1]:
			if self.checkFinger(finger, id) == True:
				return finger.successor

		tempNode = self.findPredecessor(id)
		if tempNode == self:
			return tempNode
		return tempNode.fingerTable[0].successor

	# 
	# @findPredecessor: asks node n to find id's predecessor
	# @id: identifier or key to be found
	# returns: predecessor node
	#
	def findPredecessor(self, id):

		if self.emptyTable():
			return self

		tempNode = self
		while(self.isValid((tempNode.identifier, tempNode.fingerTable[0].successor.identifier), id) == False):
			tempNode = tempNode.closestPrecedingFinger(id)
			print(tempNode, "node", tempNode.fingerTable[0].successor.identifier)
			if tempNode == self:
				return tempNode

		return tempNode


	# 
	# @closestPrecedingFinger: return closest finger preceding id
	# @id: identifier or key
	# returns: closest node to id
	#
	def closestPrecedingFinger(self, id):
		if self.emptyTable():
			return self

		m = len(self.fingerTable)
		for i in range(m - 1, -1, -1):
			if self.isValid(self.fingerTable[i].interval, id):
				return self.fingerTable[i].successor
		return self

	def displayFingerTable(self):
		print(f"\nID: <{self.identifier}>")
		for finger in self.fingerTable:
			print(finger.dict())


	# 
	# @isValid: checks if id is in the given interval following 
	# 			a circular manner
	# @interval: intervals between nodes in the network
	# @id: identifier or key
	# return: True if id is in interval, or False if not
	#
	def isValid(self, interval, id):
	    start, end = interval
	    if start <= end:
	        return start <= id <= end
	    else:
	        return start <= id or id <= end


	def __repr__(self):
		return f"Node_{self.identifier}"


