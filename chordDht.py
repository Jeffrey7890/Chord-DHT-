class Node:
    def __init__(self, identifier):
    	self.identifier = identifier
    	self.successor = None
    	self.predecessor = None 
    	self.finger = []


    # ask node n to find id's predecessor
    def find_predecessor(self, id):
    	temp_node = self
    	while (id not in range(temp_node.identifier, temp_node.successor.identifier+1)):
    		temp_node = temp_node.closest_preceding_finger(id)
    		print(temp_node)
    	return temp_node


    def closest_preceding_finger(self, id):
    	for i in range(len(self.finger)-1, -1, -1):
    		if self.finger[i].identifier in range(self.identifier, id, -1):
    			return(self.finger[i])
    	return self

    def __str__(self):
    	return f'node_{self.identifier}'

    def __repr__(self):
    	return f'node_{self.identifier}'

    def __lt__(self, node):
    	return (self.identifier < node.identifier)

if __name__ == "__main__":
	# List of Nodes in the network
	NODES = [Node(5), Node(10), Node(14), Node(21), Node(35), Node(40), Node(50)]
	node_length = len(NODES)

	# Link all nodes in the network 
	# and update their finger tables
	for i, node in enumerate(NODES):
		node.successor = NODES[(i + 1) % node_length]
		for j in range(3):
			node.finger.append(NODES[(j + i + 1) % node_length])
		node.finger = sorted(node.finger, reverse=True)

		# print(node, node.successor, node.finger)

	# Implement a closest_preceding_finger procedure
	key = 15

	node = NODES[5]
	print(node.finger)
	closes_node = node.closest_preceding_finger(key)
	closes_node = closes_node.closest_preceding_finger(key)

	# print(node_predecessor)
	print(f"{closes_node} is the closest node to the id of {key} from {node}")
