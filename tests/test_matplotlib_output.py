from src.matplotlib_output import MatplotlibOutput
from src.sir_model import SIRModel
import random


def test_init():
    matplot_lib_output = MatplotlibOutput()
    assert matplot_lib_output._susceptible == []
    assert matplot_lib_output._infected == []
    assert matplot_lib_output._recovered == []
    assert matplot_lib_output._days == []
    assert matplot_lib_output._model_configuration is None


def test_update_values():
    matplot_lib_output = MatplotlibOutput()

    population = random.randint(10, 100)
    initial_infection = random.randint(0, 10)
    days = random.randint(10, 100)
    transmission_rate = random.random()
    recovery_rate = random.random()
    sir_model = SIRModel(population, initial_infection, days, transmission_rate, recovery_rate)
    sir_model.run_simulation(matplot_lib_output.update_values)

    assert len(matplot_lib_output._susceptible) == days - 1
    assert len(matplot_lib_output._infected) == days - 1
    assert len(matplot_lib_output._recovered) == days - 1
    assert len(matplot_lib_output._days) == days - 1


def test_add_model_configuration_values():
    matplot_lib_output = MatplotlibOutput()
    test_dict = {
        "key": "value",
    }
    matplot_lib_output.add_model_configuration_values(test_dict)
    assert matplot_lib_output._model_configuration["key"] == "value"


def test_return_model_configuration_text():
    matplot_lib_output = MatplotlibOutput()

    population = random.randint(10, 100)
    initial_infection = random.randint(0, 10)
    days = random.randint(10, 100)
    transmission_rate = random.random()
    recovery_rate = random.random()
    sir_model = SIRModel(population, initial_infection, days, transmission_rate, recovery_rate)
    sir_model.run_simulation(matplot_lib_output.update_values)

    matplot_lib_output.add_model_configuration_values(sir_model.get_model_configuration())
    returned_output = matplot_lib_output._return_model_configuration_text()
    expected_output = "Population: %s\nInitial Infections: %s\nTransmission Rate: %s\nRecovery Rate: %s" % \
                      (str(population), str(initial_infection), str(transmission_rate), str(recovery_rate))

    assert returned_output == expected_output


def test_show_graph():
    pass
