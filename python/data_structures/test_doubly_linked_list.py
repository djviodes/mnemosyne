"""
Tests the implementation of the doubly-linked-list data structure.
"""

import pytest
from python.data_structures.doubly_linked_list import Node, DoublyLinkedList


def test_node_initialization():
    new_node = Node(key="node_initialization_key", data="node_initialization_data")

    assert new_node is not None
    assert new_node.key == "node_initialization_key"
    assert new_node.data == "node_initialization_data"
    assert new_node.next_node is None
    assert new_node.previous_node is None


def test_node_key_update():
    new_node = Node(key="node_key_update_key", data="node_key_update_data")

    with pytest.raises(AttributeError):
        new_node.key = "updated_node_key_update_key"


def test_node_data_update():
    new_node = Node(key="node_data_update_key", data="node_data_update_data")

    new_node.data = "updated_node_data_update_data"

    assert new_node.data == "updated_node_data_update_data"


def test_node_pointers():
    new_node_one = Node(key="node_pointers_key_one", data="node_pointers_data_one")
    new_node_two = Node(key="node_pointers_key_two", data="node_pointers_data_two")

    new_node_one.next_node = new_node_two
    new_node_two.previous_node = new_node_one

    assert new_node_one.next_node == new_node_two
    assert new_node_two.previous_node == new_node_one