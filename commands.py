"""Module that defines command classes for basic arithmetic operations."""

class AddCommand:
    """Command to add two numbers."""

    def execute(self, a, b):
        """Add two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    def description(self):
        """Return a description of the command."""
        return "Add two numbers."


class SubtractCommand:
    """Command to subtract two numbers."""

    def execute(self, a, b):
        """Subtract two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The difference of a and b.
        """
        return a - b

    def description(self):
        """Return a description of the command."""
        return "Subtract two numbers."


class MultiplyCommand:
    """Command to multiply two numbers."""

    def execute(self, a, b):
        """Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        return a * b

    def description(self):
        """Return a description of the command."""
        return "Multiply two numbers."


class DivideCommand:
    """Command to divide two numbers."""

    def execute(self, a, b):
        """Divide two numbers.

        Args:
            a (float): Numerator.
            b (float): Denominator.

        Returns:
            float: The result of a divided by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def description(self):
        """Return a description of the command."""
        return "Divide two numbers."
