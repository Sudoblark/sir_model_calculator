from src.output_enum import OutputEnum


def test_enum():
    assert OutputEnum.CSV.value == "csv"
    assert OutputEnum.TERMINAL.value == "terminal"
    assert OutputEnum.MATPLOTLIB.value == "matplotlib"


def test_str():
    assert str(OutputEnum.CSV) == "csv"
    assert str(OutputEnum.TERMINAL) == "terminal"
    assert str(OutputEnum.MATPLOTLIB) == "matplotlib"
