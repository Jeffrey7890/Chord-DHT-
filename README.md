# Chord Implementation README

## Overview

This Python code provides an implementation of the Chord distributed hash table (DHT). Chord is a decentralized protocol that enables distributed storage and retrieval of key-value pairs across a network of nodes. The key feature of Chord is its ability to efficiently locate the node responsible for a given key.

## Node Numbering

In this implementation, node numbering is hashed in the hash space of `2**m - 1`, where `m` is a configurable parameter. This hash space defines the circular ring structure used by Chord.

## Classes

### `fingerEntry`

- **Attributes:**
  - `start`: The starting point of the finger's interval.
  - `interval`: The interval of the finger in the Chord ring.
  - `successor`: The successor node associated with the finger.

- **Methods:**
  - `dict()`: Returns a dictionary representation of the `fingerEntry` object.

### `Node`

- **Attributes:**
  - `identifier`: The unique identifier of the node.
  - `fingerTable`: The finger table, which is a list of `fingerEntry` objects.

- **Methods:**
  - `checkFinger(finger, id)`: Checks the node's finger table for a given identifier.
  - `emptyTable()`: Returns `True` if the finger table is empty, `False` otherwise.
  - `findSuccessor(id)`: Locates the successor of a given key or identifier.
  - `findPredecessor(id)`: Asks the node to find the predecessor of a given key or identifier.
  - `closestPrecedingFinger(id)`: Returns the closest finger preceding a given key or identifier.
  - `displayFingerTable()`: Displays the contents of the node's finger table.
  - `isValid(interval, id)`: Checks if the given identifier is in the specified circular interval.

- **Representation:**
  - `__repr__()`: Returns a string representation of the node.

## Usage

1. Import the `Node` and `fingerEntry` classes from the `chord` module.

   ```python
   from chord import Node, fingerEntry
   ```

2. Create nodes and initialize the Chord network.

   ```python
   # Example: Create three nodes in the network
   NODES = [Node(0), Node(1), Node(3)]
   ```

3. Customize the Chord network by linking nodes and updating their finger tables.

   ```python
   # Example: Link nodes in the network and update finger tables
   for i, node in enumerate(NODES):
       for j in range(3):
           successor = None  # Replace with actual successor logic
           start = (node.identifier + 2**j) % 2**m
           end = (node.identifier + 2**(j+1)) % 2**m
           interval = (start, end)
           node.fingerTable.append(fingerEntry(start, interval, successor))
   ```

4. Test the Chord network by querying for successors, predecessors, and other functionalities.

   ```python
   # Example: Test querying for the successor of a key
   node = NODES[0]
   key = 7
   successor_node = node.findSuccessor(key)
   print(successor_node)
   ```

## Testing

To ensure the correctness of the Chord implementation, consider writing test cases using the `unittest` module. Test scenarios should cover various aspects, including empty finger tables, node join and departure, querying for successors and predecessors, and edge cases.

```python
# Example: Write a test for an empty finger table
import unittest
from chord import Node, fingerEntry

class TestEmptyFingerTable(unittest.TestCase):

    def test_empty_finger_table(self):
        node = Node(0)
        self.assertEqual(len(node.fingerTable), 0)
        # Add more assertions based on expected behavior

if __name__ == '__main__':
    unittest.main()
```

## Contributors

- Add your name here if you contribute to the project.

## License

This Chord implementation is licensed under the [MIT License](LICENSE).
