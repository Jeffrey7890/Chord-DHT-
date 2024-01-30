from chord import Node

first_node = Node(0)
first_node.initializeFingetTableStartInterval(3)
first_node.join(None)

second = Node(1)
second.initializeFingetTableStartInterval(3)
second.join(first_node)

# print(second.isValid((second.identifier, 2), ))

second.updateOthers()
second.fingerTable[1].successor = first_node
first_node.displayFingerTable()
second.displayFingerTable()

