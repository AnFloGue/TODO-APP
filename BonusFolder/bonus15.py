import json
import random


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def read_all_data(data):
    for index_quix, quix in enumerate(data):
        print(f"\nQUESTION {index_quix + 1}:  {quix['question_text']}")
        for index_option, option in enumerate(quix['options_answers']):
            print(f"{index_option + 1}. {option}")


def question(data, question_number):
    question = data[question_number]['question_text']
    print(f"\nQUESTION {question_number}:  {question}")
    for index_option, option in enumerate(data[question_number]['options_answers']):
        print(f"{index_option + 1}. {option}")


def answer(data, question_number):
    user_answer = input("Enter your answer: ")
    if user_answer == data[question_number]['correct_answer']:
        print("Correct!")
        return 1  # Return 1 if the answer is correct
    else:
        print("Incorrect!")
        return -1  # Return -1 if the answer is incorrect


def main():
    play = "y"
    questions_answered = 0  # Initialize the counter
    score = 0  # Initialize the score outside the loop
    while True:  # Use an infinite loop with a break condition
        file_path = 'files/Quix_01.json'
        question_number = random.randint(0, 9)
        data = read_json(file_path)

        question(data, question_number)
        score += answer(data, question_number)  # Update the score
        questions_answered += 1  # Increment the counter

        print(f"You have answered {questions_answered} questions\nYour score is: {score}")  # Print the number of questions answered

        while True:
            play = input("Do you want to play? (y/n): ").lower().strip()
            if play in ("y", "n"):
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if play == "n":
            break

    # Display final score after exiting the loop
    print(f"You have answered {questions_answered} questions\nYour final score is: {score}")


if __name__ == "__main__":
    main()
