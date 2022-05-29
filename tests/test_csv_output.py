from io import TextIOWrapper
import random

from src.csv_output import CsvOutput
import tempfile


def test_init():
    tmp = tempfile.NamedTemporaryFile(delete=True)
    csv_output = CsvOutput(tmp.name)
    assert csv_output._csv_path == tmp.name
    assert csv_output._csv_handler is None


def test_open_handler():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    csv_output = CsvOutput(tmp.name)
    csv_output.open_handler()
    assert type(csv_output._csv_handler) is TextIOWrapper
    assert csv_output._csv_handler.closed is False


def test_close_handler():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    csv_output = CsvOutput(tmp.name)
    csv_output.open_handler()
    csv_output.close_handler()
    assert csv_output._csv_handler.closed is True


def test_write():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    csv_output = CsvOutput(tmp.name)
    csv_output.open_handler()
    int_data = [random.randint(10, 100), random.randint(10, 100), random.randint(10, 100)]
    string_data = [str(int) for int in int_data]
    csv_output.write(int_data)
    csv_output.close_handler()
    with open(tmp.name, 'r') as file:
        data = file.read().rstrip()
        assert data == ', '.join(string_data)


def test_write_header():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    csv_output = CsvOutput(tmp.name)
    csv_output.open_handler()
    csv_output.write_header()
    csv_output.close_handler()
    with open(tmp.name, 'r') as file:
        data = file.read().rstrip()
        assert data == "Day, Susceptible, Infected, Recovered"
