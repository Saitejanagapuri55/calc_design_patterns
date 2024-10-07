import importlib
import os
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Load commands into a dictionary
commands = {
    'add': AddCommand(),
    'subtract': SubtractCommand(),
    'multiply': MultiplyCommand(),
    'divide': DivideCommand(),
}

def load_plugins():
    plugins = {}
    for filename in os.listdir('plugins'):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py
            module = importlib.import_module(f'plugins.{module_name}')
            class_name = module_name[:-7].capitalize() + 'Plugin'  # Remove '_plugin' from the name
            plugins[module_name] = getattr(module, class_name)()  # Instantiate the plugin class
    return plugins

def display_menu():
    print("Available commands: add, subtract, multiply, divide, menu, exit")

def repl():
    display_menu()
    while True:
        user_input = input("Enter command: ")
        if user_input == 'exit':
            break
        elif user_input in commands:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = commands[user_input].execute(a, b)
            print(f"Result: {result}")
        elif user_input == 'menu':
            display_menu()
        else:
            print("Unknown command.")

if __name__ == "__main__":
    # Load plugins and add them to the command dictionary
    loaded_plugins = load_plugins()
    commands.update(loaded_plugins)  # Add loaded plugins to commands
    repl()
