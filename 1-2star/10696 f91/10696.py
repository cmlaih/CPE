# Output 
while True:
	n = int(input())
	
	if not n:
		break

	if n <= 100:
		print("f91({0}) = 91".format(n))
	else:
		print("f91({0}) = {1}".format(n, n-10))