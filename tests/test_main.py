import pytest
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Initialize command instances
add_command = AddCommand()
subtract_command = SubtractCommand()
multiply_command = MultiplyCommand()
divide_command = DivideCommand()

def test_add_command():
    """Test the addition command."""
    assert add_command.execute(1, 2) == 3
    assert add_command.execute(-1, 1) == 0
    assert add_command.execute(0, 0) == 0

def test_subtract_command():
    """Test the subtraction command."""
    assert subtract_command.execute(5, 3) == 2
    assert subtract_command.execute(3, 5) == -2
    assert subtract_command.execute(0, 0) == 0

def test_multiply_command():
    """Test the multiplication command."""
    assert multiply_command.execute(2, 3) == 6
    assert multiply_command.execute(-1, 1) == -1
    assert multiply_command.execute(0, 5) == 0

def test_divide_command():
    """Test the division command."""
    assert divide_command.execute(6, 3) == 2
    assert divide_command.execute(-6, 3) == -2
    assert divide_command.execute(0, 1) == 0
    
    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide_command.execute(6, 0)

def test_command_descriptions():
    """Test the descriptions of the commands."""
    assert add_command.description() == "Add two numbers."
    assert subtract_command.description() == "Subtract two numbers."
    assert multiply_command.description() == "Multiply two numbers."
    assert divide_command.description() == "Divide two numbers."
