from src.sir_model import SIRModel
import src.terminal_output as terminal_output
import re


def test_output_data(capsys):
    """
    Unit test which tests if print statements in this method are in the format expected

    @param capsys: PyTest object that allows capture of data written to STDOUT
    """
    population = 150
    initial_infection = 4
    days = 60
    transmission_rate = 0.43
    recovery_rate = 0.18

    sir_model = SIRModel(population, initial_infection, days, transmission_rate, recovery_rate)
    sir_model.run_simulation(terminal_output.output_data)
    captured = capsys.readouterr().out
    outputted_string = str(captured).split("\n")
    for i in range(len(outputted_string) - 1):
        # Matches floats or ints as data will alternate between these types throughout program's execution
        assert re.match('\d+, [+-]?([0-9]*[.])?[0-9]+, [+-]?([0-9]*[.])?[0-9]+, [+-]?([0-9]*[.])?[0-9]+',
                        outputted_string[i]), "String output for day {0} is not in expected format".format(i)


def test_output_header(capsys):
    """
    Unit test which tests if print statments in this method has the format expected

    @param capsys: PyTest object that allows capture of data written to STDOUT
    """
    terminal_output.output_header()
    captured = capsys.readouterr().out
    outputted_string = str(captured).split("\n")
    assert "SIR model data - terminal output" in outputted_string[0]
    assert "Day, Susceptible, Individual, Recovered" in outputted_string[2]
