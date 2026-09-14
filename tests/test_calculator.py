from app.calculator import calculator


def run_calculator_with_input(monkeypatch, capsys, inputs):
    """Simulates user input and captures calculator output."""
    input_iter = iter(inputs)

    def mock_input(prompt):
        return next(input_iter)

    monkeypatch.setattr("builtins.input", mock_input)

    calculator()

    captured = capsys.readouterr()
    return captured.out


def test_invalid_operation(monkeypatch, capsys):
    """Test invalid operation in REPL."""
    inputs = ["modulus 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Unknown operation" in output


def test_invalid_input(monkeypatch, capsys):
    """Test invalid input format in REPL."""
    inputs = ["add two three", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Invalid input. Please follow the format: <operation> <operand1> <operand2>" in output


def test_division_by_zero(monkeypatch, capsys):
    """Test division by zero in REPL."""
    inputs = ["divide 5 0", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "Division by zero is not allowed." in output


def test_addition(monkeypatch, capsys):
    """Test addition in REPL."""
    inputs = ["add 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "8.0" in output


def test_subtraction(monkeypatch, capsys):
    """Test subtraction in REPL."""
    inputs = ["subtract 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "2.0" in output


def test_multiplication(monkeypatch, capsys):
    """Test multiplication in REPL."""
    inputs = ["multiply 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "15.0" in output


def test_division(monkeypatch, capsys):
    """Test division in REPL."""
    inputs = ["divide 6 3", "exit"]
    output = run_calculator_with_input(monkeypatch, capsys, inputs)
    assert "2.0" in output
