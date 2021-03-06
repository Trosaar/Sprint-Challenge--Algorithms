'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

Inside the `recursive_count_th` directory you'll find the `count_th.py` file. In this file, please add your recursive implementation to the `count_th()` method following these rules:

* Your function should take in a signle parameter (a string `word`)
* Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
* Your function must utilize recursion. 
  * It cannot contain any loops.

Run `python test_count_th.py` to run the tests for your `count_th()` function to ensure that your implementation is correct.

'''
def count_th(word):
	count = 0
	l = len(word)
	if len(word) > 1:
		if "th" in word[l-2:]:
			count +=1

		count += count_th(word[:l-1])
	return count