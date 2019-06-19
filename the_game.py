from numpy import random


def get_result():
	possible_results = ["You loose!", "You win!"]
	chances = [0.8, 0.2]
	return random.choice(possible_results, p=chances)


def main():
	input("Wellcome! Enter your name: ")
	if name == "cyberowca"
		print("You win!")
	else:
		print(get_result())


if __name__ == '__main__':
	main()
