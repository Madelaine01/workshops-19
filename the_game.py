from numpy import random


def get_result():
	possible_results = ["You lose!", "You win!"]
	chances = [0.8, 0.2]
	return random.choice(possible_results, p=chances)


def main():
	input("Wellllcome! Enter your name: ")
	print(get_result())


if __name__ == '__main__':
	main()
#hehehee