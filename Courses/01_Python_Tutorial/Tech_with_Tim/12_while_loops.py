x = [3, 4, 42, 3, 2, 4]

'''
i = 0
while i < 10:
	print('run')
	i += 1 
	"""
	i -= 2
	i *= 3
	i /= 4

	"""
'''

"""
i = 1
while True:
	print('Yo')
	i += 1
	while True: # Returns only 1 'Yo' because there's no statement inside this loop which makes the loop run infinitely doing nothing
		if i == 10:
			break # break will break out of the loop that's closest to it
		i += 1
"""


'''
ChatGPT explanation for the above loop:

Let’s walk through what happens step by step:

Step 1: 
	i = 1
	Outer while True starts.
	Prints "Yo".
	i becomes 2.

Step 2:
	Inner while True starts.
	It checks if i == 10: not yet (i = 2).
	i increments again and again inside the inner loop until i == 10.

That means the inner loop executes repeatedly (i = 2, 3, 4, 5, 6, 7, 8, 9, 10) doing no printing, just incrementing i.

When i == 10, the break executes — but that only breaks the inner loop, not the outer one.

Step 3: 
	Control goes back to the outer while True.
	It prints "Yo" again.
	Increments i to 11.
	Then it enters the inner while True again.

Now, since i is already 11, if i == 10 is false, so it never breaks — meaning the inner loop runs forever doing nothing.

Result:
	You’ll see two "Yo" prints:
		Yo
		Yo
	Then your program freezes in the inner infinite loop.

'''

'''
To make it work properly:
If your goal is to print "Yo" until i reaches 10, you could do this:
'''

i = 1
while True:
	print('Yo')
	i += 1
	if i == 10:
		break

# That prints "Yo" 9 times and then stops — exactly what you might expect.
