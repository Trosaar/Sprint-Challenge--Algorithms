#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
1 +
#n
	1
sum = O(n)

b)
1
#n
	1
	#logn
		1
		1
sum = O(n*logn)

c)
1
	1
		1
		
	n
sum = O(n)

## Exercise II

# notes
	if n >= f
		dropped egg += 1
		broken egg += 1

	if n < f
		dropped egg +=1
#


def will_egg_break(nth-story buiilding as number)

	binary search floors for f (floors of a building are already sorted)
		if egg breaks at n // 2, f is lower
		else f is higher

should run at O(log(n))

or, being more realistic, f is likely to be one of the bottom if not just the bottom floorsince we are throwing EGGS. Loop from 0 (ground floor) to n until egg breaks.

this would have O(n) on paper but in practice should only ever run for first MAYBE two floors before the egg breaks so depeding on how much real life we factor in, this could be the best option.


