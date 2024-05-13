import ML

while True:
	text = input('Welcome to Mobile Legends:')
	result, error = ML.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)
