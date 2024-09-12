# AirBnB Clone - The Console

## Description
This project is the first step toward building a full web application: the **AirBnB Clone**. The focus of this stage is on building a command-line interface (CLI) that manages different aspects of the project using a custom command interpreter.

The command interpreter allows for the creation, modification, and deletion of objects (such as users, places, cities, etc.) in the system. The project will be expanded over time to include more advanced features, leading to a complete clone of the AirBnB platform.

## Command Interpreter

The command interpreter allows you to interact with the application through a command-line interface. It can be run in both interactive and non-interactive modes.

### How to start the command interpreter:

To start the command interpreter, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/AceDemo2/AirBnB_clone.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AirBnB_clone
    ```
3. Run the console:
    ```bash
    ./console.py
    ```

### How to use the command interpreter:
In interactive mode, once the interpreter is running, you can use the following commands:

#### Available Commands:
- `help`: Displays the list of available commands.
- `quit`: Exits the interpreter.
- `create <class_name>`: Creates a new instance of a class.
- `show <class_name> <id>`: Shows the details of an object based on its ID.
- `destroy <class_name> <id>`: Deletes an object based on its ID.
- `all <class_name>`: Shows all objects or all objects of a class.
- `update <class_name> <id> <attribute_name> <value>`: Updates the attribute of an object.

### Examples:

1. Start the console and display available commands:
    ```bash
    $ ./console.py
    (hbnb) help
    ```

2. Create a new object:
    ```bash
    (hbnb) create User
    ```

3. Show an object:
    ```bash
    (hbnb) show User 1234-1234-1234
    ```

4. Exit the interpreter:
    ```bash
    (hbnb) quit
    ```

### Non-interactive mode:

You can also pass commands to the interpreter using echo:
```bash
$ echo "create User" | ./console.py

