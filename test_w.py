import pytest
from functions import Graph

@pytest.fixture
def setup_graph():
    graph = Graph()
    graph.graph = {
        'dog': ['bone', 'bark'],
        'bone': ['cat'],
        'bark': ['cat'],
        'cat': []
    }
    return graph

def test_find_bridge_words_word_not_in_graph(setup_graph):
    graph = setup_graph
    word1 = 'apple'
    word2 = 'banana'
    expected_output = "No word1 or word2 in the graph!"
    
    result = graph.find_bridge_words(word1, word2)
    
    assert result == expected_output

def test_find_bridge_words_bridge_words_found(setup_graph):
    graph = setup_graph
    word1 = 'dog'
    word2 = 'cat'
    expected_output = "The bridge words from word1 to word2 are: bone, bark."
    
    result = graph.find_bridge_words(word1, word2)
    
    assert result == expected_output

def test_find_bridge_words_bridge_words_not_found(setup_graph):
    graph = setup_graph
    word1 = 'apple'
    word2 = 'banana'
    expected_output = "No word1 or word2 in the graph!"
    
    result = graph.find_bridge_words(word1, word2)
    
    assert result == expected_output
