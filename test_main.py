from main import *

def test_myfunction():
	""" done. """
	assert myfunction('Hello') == 'Hello'
	assert myfunction(1) == 1
	assert myfunction(6) == -1
