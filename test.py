import pytest
from functions import generate_directed_graph, process_text_file

def test_valid_input_sentence():
    content = "This is a simple test."
    graph = generate_directed_graph(content)
    assert 'this' in graph.graph
    assert 'is' in graph.graph['this']
    assert 'a' in graph.graph['is']
    assert 'simple' in graph.graph['a']
    assert 'test.' in graph.graph['simple']

def test_empty_file():
    content = ""
    graph = generate_directed_graph(content)
    assert len(graph.graph) == 0

def test_invalid_characters():
    content = "@#$%^&*"
    with open("temp_invalid_characters.txt", 'w') as f:
        f.write(content)
    words = process_text_file("temp_invalid_characters.txt", "output.txt")
    assert len(words) == 0

def test_existing_start_and_target_nodes():
    content = "this is a simple test"
    graph = generate_directed_graph(content)
    result = graph.find_bridge_words("this", "test")
    assert result == "No word1 or word2 in the graph!"

def test_nonexistent_start_node():
    content = "this is a simple test"
    graph = generate_directed_graph(content)
    result = graph.find_bridge_words("nonexistent", "test")
    assert result == "No word1 or word2 in the graph!"

def test_nonexistent_target_node():
    content = "this is a simple test"
    graph = generate_directed_graph(content)
    result = graph.find_bridge_words("this", "nonexistent")
    assert result == "No word1 or word2 in the graph!"

def test_direct_connection():
    content = "this is a simple test"
    graph = generate_directed_graph(content)
    result = graph.find_bridge_words("this", "is")
    assert result == "No bridge words from word1 to word2!"
