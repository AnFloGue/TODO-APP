from functions_todos import load_todos, add_todo, show_todos, edit_todo, remove_todo, exit_todo


def main():
    running = True
    todos = load_todos()
    while running:
        user_action = input(
            f"Menu\nA\t\tAdd\nS\t\tShow\nED\tEdit\nR\t\tRemove item\nE\t\tExit\nPlease choose:  ").lower().strip()
        
        if user_action == "a":
            todos = add_todo(todos)
        elif user_action == "s":
            show_todos(todos)
        elif user_action == "ed":
            todos = edit_todo(todos)
            if todos is None:  # If 'cancel' was entered, continue to the next iteration
                continue
        elif user_action == "r":
            todos = remove_todo(todos)
        elif user_action == "e":
            running = exit_todo(todos)
        else:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()
