from src.SIRModel import SIRModel
import random


def __setup_basic_sir_model():
    population = random.randint(10, 100)
    initial_infection = random.randint(0, 10)
    days = random.randint(10, 100)
    transmission_rate = random.random()
    recovery_rate = random.random()

    sir_model = SIRModel(population, initial_infection, days, transmission_rate, recovery_rate)

    return population, initial_infection, days, transmission_rate, recovery_rate, sir_model


def test_getModelConfiguration():
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()
    sir_model_configuration = sir_model.getModelConfiguration()
    assert sir_model_configuration['population'] == population
    assert sir_model_configuration['initialInfections'] == initial_infection
    assert sir_model_configuration['simulatedDays'] == days
    assert sir_model_configuration['transmissionRate'] == transmission_rate
    assert sir_model_configuration['recoveryRate'] == recovery_rate


def test_runSimulation():
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()
    test_sir_data = []

    def callback_test(sir_list):
        test_sir_data.append(sir_list)

    sir_model.runSimulation(callback_test)

    assert len(test_sir_data) == (days - 1)
    for data in test_sir_data:
        assert len(data) == 4
        for subdata in data:
            assert subdata is not None


def test_getModelMatrix():
    pass


def test_str_override():
    pass
