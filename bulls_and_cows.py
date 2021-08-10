from random import choice


def get_secret_num():
	num = []
	while len(num) < 4:
		x = choice(range(10))
		if str(x) not in num:
			num.append(str(x))

	num_str = ''.join(num)
	print(num_str)
	return num_str


def get_input(prompt, ref=None, find_in=[]):
	print(prompt)
	running = True
	while running:
		value = input(":> ").strip().lower()
		try:
			if ref == None:
				if len(set(value)) == 4:
					for i in value:
						if int(i) in range(10):
							pass
					else:
						running = False
						break
				else:
					continue
			else:
				if value not in find_in:
					continue
				else:
					break
		except ValueError:
			continue

	return value


def check_occurance(secret_num, guessed_num):
	cow, bull = [0], [0]
	if secret_num == guessed_num:
		cow = ['won']
	else:
		for ind, num in enumerate(secret_num):
			for ind2, num2 in enumerate(guessed_num):
				if ind == ind2 and num == num2:
					bull.append(1)
				elif num == num2:
					cow.append(1)

	return cow, bull


play = True
input_msg = "Enter 4 digit (unique) number."
again_msg = "Do you want to play again? (y/n)"
again_msg_find = ["y", "n"]

while play:
	print("Let's play bulls and cows game.")
	secret_num = get_secret_num()
	while True:
		guessed_num = get_input(input_msg)
		result = check_occurance(secret_num, guessed_num)
		if result[0][0] == "won":
			print("You won!")
			break
		else:
			print("Cows:", sum(result[0]))
			print("Bulls:", sum(result[1]))
	again = get_input(again_msg, "again", again_msg_find)
	if again == 'y':
		continue
	else:
		break