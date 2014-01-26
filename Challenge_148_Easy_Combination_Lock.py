def master_lock(n, first, second, third):
	spin = ((2 * n) + first + (second + n) + third)
	return spin
