"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  if right < left:
        return -1

    mid = (right + left) // 2  # or: left + (right - left) // 2
    if mylist[mid] == key:
        return mid
    elif mylist[mid] > key:
        return _binary_search(mylist, key, left, mid - 1)
    else:
        return _binary_search(mylist, key, mid + 1, right)
    ###
"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO

	###

def test_binary_search():
    assert binary_search([1,2,3,4,5], 5) == 4
    assert binary_search([1,2,3,4,5], 1) == 0
    assert binary_search([1,2,3,4,5], 6) == -1
    ### TODO: add two more tests here.
    assert binary_search([1,2,3,4,5], 2) == 1
    assert binary_search([], 2) == -1


def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
start = time.time()
    search_fn(mylist, key)
    return (time.time() - start) * 1000

	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
    result = []
    for size in sizes:
        mylist = list(range(int(size)))
        result.append([
            len(mylist),
            time_search(linear_search, mylist, -1),
            time_search(binary_search, mylist, -1)
        ])
    return result
	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
    res = compare_search(sizes=[10, 100])
    assert res[0][0] == 10
    assert res[1][0] == 100
    assert res[0][1] < 1
    assert res[1][1] < 1


