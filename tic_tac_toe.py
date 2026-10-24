def print_board(board: list[str]) -> None:
	for row in range(3):
		start = row * 3
		print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
		if row < 2:
			print("---+---+---")


def has_won(board: list[str], mark: str) -> bool:
	winning_lines = (
		(0, 1, 2),
		(3, 4, 5),
		(6, 7, 8),
		(0, 3, 6),
		(1, 4, 7),
		(2, 5, 8),
		(0, 4, 8),
		(2, 4, 6),
	)
	return any(all(board[index] == mark for index in line) for line in winning_lines)


def get_move(board: list[str], mark: str) -> int:
	while True:
		choice = input(f"Player {mark}, choose a square (1-9): ").strip()
		if not choice.isdigit() or not 1 <= int(choice) <= 9:
			print("Please enter a number from 1 to 9.")
			continue

		index = int(choice) - 1
		if board[index] in ("X", "O"):
			print("That square is already taken. Choose another one.")
			continue
		return index


def play_game() -> None:
	board = [str(number) for number in range(1, 10)]
	current_mark = "X"

	while True:
		print_board(board)
		board[get_move(board, current_mark)] = current_mark

		if has_won(board, current_mark):
			print_board(board)
			print(f"Player {current_mark} wins!")
			return

		if all(square in ("X", "O") for square in board):
			print_board(board)
			print("It's a tie!")
			return

		current_mark = "O" if current_mark == "X" else "X"


def main() -> None:
	while True:
		play_game()
		play_again = input("Play again? (y/n): ").strip().lower()
		if play_again not in ("y", "yes"):
			print("Thanks for playing!")
			break


if __name__ == "__main__":
	main()
