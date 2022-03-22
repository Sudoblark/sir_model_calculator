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
    """
    Unit test which tests that getModelConfiguration method returns correct values
    :return:
    """
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()
    sir_model_configuration = sir_model.getModelConfiguration()
    assert sir_model_configuration['population'] == population, "Population returned in getModelConfiguration is not " \
                                                                "that passed in to init"

    assert sir_model_configuration['initialInfections'] == initial_infection, "initialInfection returned in " \
                                                                              "getModelConfiguration is not " \
                                                                              "that passed in to init"

    assert sir_model_configuration['simulatedDays'] == days, "Days returned in getModelConfiguration is not " \
                                                             "that passed in to init"

    assert sir_model_configuration['transmissionRate'] == transmission_rate, "TransmissionRate returned in " \
                                                                             "getModelConfiguration is not " \
                                                                             "that passed in to init"

    assert sir_model_configuration['recoveryRate'] == recovery_rate, "RecoveryRate returned in getModelConfiguration " \
                                                                     "is not that passed in to init"


def test_runSimulation():
    """
    Unit test which tests if runSimulation executes callbackFunction for every day simulated day in model,
    returning non-null data for each day
    :return:
    """
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()
    test_sir_data = []

    def callback_test(sir_list):
        test_sir_data.append(sir_list)

    sir_model.runSimulation(callback_test)

    assert len(test_sir_data) == (days - 1), "Simulation did not run for expected number of days"
    for i in range(days - 1):
        assert len(test_sir_data[i]) == 4, "Data on day {0} was not in expected format [D, S, I, R]".format(i)
        for j in range(4):
            assert test_sir_data[j] is not None, "Data on day {0} for field {1} was None".format(i, j)


def test_runSimulation_accuracy():
    """
    Unit test which tests if our simulation can accurately calculate SIR numbers for a model using calculated
    numbers from a good, known, working version (My TMA results which got full marks)

    This tests the following:
    - Accurate starting SIR numbers
    - Accurate infection numbers for each day
    - Accurate ending SIR numbers
    :return:
    """
    #TODO: Triple verify expected numbers
    known_infection_numbers = [4, 5, 6, 8, 9, 11, 13, 16, 19, 22, 25, 28, 30, 33, 35, 36, 36, 36, 35, 34, 32, 30, 27,
                               25, 23, 20, 18, 16, 14, 13, 11, 10, 9, 8, 7, 6, 5, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1,
                               1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    known_ending_sir = [16, 0, 134]

    population = 150
    initial_infection = 4
    days = 60
    transmission_rate = 0.43
    recovery_rate = 0.18

    sir_model = SIRModel(population, initial_infection, days, transmission_rate, recovery_rate)

    def callback_test(sir_list):
        pass

    sir_model.runSimulation(callback_test)
    test_sir_data = sir_model.getModelResultMatrix()

    for i in range(days):
        assert test_sir_data[i][1] == known_infection_numbers[i], "Infected numbers for day {0} did not match those " \
                                                                  "returned from working model".format(i)

    assert test_sir_data[-1][0] == known_ending_sir[0], "Susceptible on end day did not match that returned from " \
                                                        "working model "

    assert test_sir_data[-1][1] == known_ending_sir[1], "Infected on end day did not match that returned from working " \
                                                        "model "

    assert test_sir_data[-1][2] == known_ending_sir[2], "Recovered on end day did not match that returned from " \
                                                        "working model "


def test_getModelMatrix():
    """
    Unit test which tests if, after running RunSimulation, getModelMatrix returns an appropraite matrix of our
    model's results
    :return:
    """
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()

    def callback_test(sir_list):
        pass

    sir_model.runSimulation(callback_test)
    test_sir_data = sir_model.getModelResultMatrix()

    assert len(test_sir_data) == days, "getModelMatrix did not return data for all days in model"
    for i in range(days):
        assert len(test_sir_data[i]) == 3, "Data on day {0} was not in expected format [S, I, R]".format(i)
        for j in range(3):
            assert test_sir_data[j] is not None, "Data on day {0} for field {1} was None".format(i, j)


def test_str_override():
    """
    Unit test which tests if overridden __str__ method returns non-null data for our model in the format
    expected
    :return:
    """
    pass
