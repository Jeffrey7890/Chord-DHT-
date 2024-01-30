from chord import Node, fingerEntry

import unittest

class TestChord(unittest.TestCase):

    def setUp(self):
        self.NODES = [Node(0), Node(1), Node(3)]

        numberOfEntry = len(self.NODES)
        # ... (same setup as before)
        for node in self.NODES:
            node.initializeFingetTableStartInterval(numberOfEntry)
        
        successors = [[1, 2, 0], [2, 2, 0], [0, 0, 0]]

        index = 0
        for i, successor in enumerate(successors):
            for j in successor:
                s = self.NODES[j]
                self.NODES[i].fingerTable[index].successor = s
                index += 1
            index = 0

    def test_findSuccessor_case1(self):
        node = self.NODES[0]
        key = 7
        self.assertTrue(node.isValid((7, 3), key))
        closest_node = node.findPredecessor(key)
        self.assertEqual(closest_node.identifier, 0)

    def test_findSuccessor_case2(self):
        node = self.NODES[1]
        key = 5
        self.assertTrue(node.isValid((5, 1), key))
        closest_node = node.findSuccessor(key)
        self.assertEqual(closest_node.identifier, 0)

    def test_findSuccessor_case3(self):
        node = self.NODES[2]
        key = 4
        self.assertFalse(node.isValid((0, 1), key))
        closest_node = node.closestPrecedingFinger(key)
        self.assertEqual(closest_node.identifier, 0)

    def test_findSuccessor_case4(self):
        node = self.NODES[0]
        key = 2
        self.assertTrue(node.isValid((7, 3), key))
        closest_node = node.findSuccessor(key)
        self.assertEqual(closest_node.identifier, 3)

    def test_findSuccessor_case5(self):
        node = self.NODES[1]
        key = 2
        self.assertTrue(node.isValid((5, 3), key))
        closest_node = node.findSuccessor(key)
        self.assertEqual(closest_node.identifier, 3)

    def test_predecessor_case(self):
        node = self.NODES[2]

        key = 1
        self.assertTrue(node.isValid((7, 3), key))
        closest_node = node.findPredecessor(key)
        self.assertEqual(closest_node.identifier, 0)

    def test_empty_finger_table(self):
        # Create a node with an empty finger table
        node = Node(2)

        # Ensure the finger table is initially empty
        self.assertEqual(len(node.fingerTable), 0)

        # Test finding the successor for a key
        key = 5
        successor = node.findSuccessor(key)

        # The node itself should be the successor since the finger table is empty
        self.assertEqual(successor, node)

        # Test finding the predecessor for a key
        predecessor = node.findPredecessor(key)

        # The node itself should be the predecessor since the finger table is empty
        self.assertEqual(predecessor, node)

        # Additional assertions based on the expected behavior of a node with an empty finger table

    def test_node_with_identical_successor_predecessor(self):
        NODES = [self.NODES[0],self.NODES[2]]
        # print('\n', NODES)

        NODES[0].fingerTable[0].successor = NODES[1]
        NODES[0].fingerTable[1].successor = NODES[1]
        NODES[0].fingerTable[2].successor = NODES[0]

        node = NODES[1]

        key = 6

        self.assertTrue(node.isValid((5, 7), key))
        successor = node.findSuccessor(key)
        self.assertEqual(successor.identifier, 0)

        


if __name__ == '__main__':
    unittest.main()
