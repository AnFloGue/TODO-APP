def load_todos():
    """Loads todo items from a file.

    Returns:
        A list of todo items (strings with newline characters).
    """
    try:
        with open("../Data_files/todos.txt", "r") as file:
            return file.readlines()
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return []  # Handle empty list case


def save_todos(todos):
    """Saves todo items to a file.

    Args:
        todos: A list of todo items (strings with newline characters).
    """
    try:
        with open("../Data_files/todos.txt", "w") as file:
            file.writelines(todos)
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")


def add_todo(todos):
    """Adds a new todo item to the list and saves it to the file.

    Args:
        todos: A list of todo items (strings with newline characters).

    Returns:
        The updated list of todo items with the new item added.
    """
    item = input("Enter a new todo item: ").title() + "\n"
    todos.append(item)
    save_todos(todos)
    return todos


def show_todos(todos):
    """Prints the numbered todo list.

    Args:
        todos: A list of todo items (strings with newline characters).
    """
    for index, item in enumerate(todos, start=1):  # Start enumeration from 1
        print(f"{index} - {item.strip()}")


def edit_todo(todos):
    """Edits a todo item in the list and saves the changes to the file.

    Args:
        todos: A list of todo items (strings with newline characters).

    Returns:
        The updated list of todo items or None if 'cancel' is entered.
    """
    while True:
        try:
            index = input("Enter the index of the item to edit or 'cancel' to return: ")
            if index.lower() == 'cancel':
                return None
            index = int(index) - 1  # Adjust for 0-based indexing
            if 0 <= index < len(todos):
                break
            raise IndexError
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid integer or 'cancel'.")
            continue
    
    new_todo = input("Enter the new todo item: ").title() + "\n"
    todos[index] = new_todo
    save_todos(todos)
    return todos


def remove_todo(todos):
    """Removes a todo item from the list and saves the changes to the file.

    Args:
        todos: A list of todo items (strings with newline characters).

    Returns:
        The updated list of todo items with the item removed.
    """
    while True:
        try:
            index = int(input("Enter the index of the item to remove: ")) - 1
            if 0 <= index < len(todos):
                del todos[index]
                save_todos(todos)
                break
            raise IndexError
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid integer.")
    return todos


def exit_todo(todos):
    """Exits the todo application.

    Returns:
        False to indicate program termination.
    """
    return False
