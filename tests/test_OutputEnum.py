from src.output_enum import OutputEnum


def test_enum():
    assert OutputEnum.csv.value == "csv"
    assert OutputEnum.terminal.value == "terminal"
    assert OutputEnum.matplotlib.value == "matplotlib"


def test_str():
    assert str(OutputEnum.csv) == "csv"
    assert str(OutputEnum.terminal) == "terminal"
    assert str(OutputEnum.matplotlib) == "matplotlib"
