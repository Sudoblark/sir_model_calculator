from src.sir_model import SIRModel
import random


def __setup_basic_sir_model():
    population = random.randint(10, 100)
    initial_infection = random.randint(0, 10)
    days = random.randint(10, 100)
    transmission_rate = random.random()
    recovery_rate = random.random()

    sir_model = SIRModel(population, initial_infection, days, transmission_rate, recovery_rate)

    return population, initial_infection, days, transmission_rate, recovery_rate, sir_model


def test_get_model_configuration():
    """
    Unit test which tests that getModelConfiguration method returns correct values
    :return:
    """
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()
    sir_model_configuration = sir_model.get_model_configuration()
    assert sir_model_configuration['closed_population'] == population, "Population returned in getModelConfiguration is not " \
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


def test_run_simulation():
    """
    Unit test which tests if runSimulation executes callback_function for every day simulated day in model,
    returning non-null data for each day
    :return:
    """
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()
    test_sir_data = []

    def callback_test(sir_list):
        test_sir_data.append(sir_list)

    sir_model.run_simulation(callback_test)

    assert len(test_sir_data) == (days - 1), "Simulation did not run for expected number of days"
    for i in range(days - 1):
        assert len(test_sir_data[i]) == 4, "Data on day {0} was not in expected format [D, S, I, R]".format(i)
        for j in range(4):
            assert test_sir_data[j] is not None, "Data on day {0} for field {1} was None".format(i, j)


def test_run_simulation_accuracy():
    """
    Unit test which tests if our simulation can accurately calculate SIR numbers for a model using calculated
    numbers from a good, known, working version (My TMA results which got full marks)

    This tests the following:
    - Accurate starting SIR numbers
    - Accurate infection numbers for each day
    - Accurate ending SIR numbers
    :return:
    """
    # Taken from Java implementation of SIR Model from 99% assignment submitted for Open University M250 TMA02
    # Listed with 5 values a row
    known_infection_numbers = [
        4.000000,
        4.954133,
        6.112083,
        7.504773,
        9.161167,
        11.104172,
        13.344930,
        15.875675,
        18.661860,
        21.635091,
        24.689285,
        27.682847,
        30.449145,
        32.815464,
        34.627489,
        35.773360,
        36.200449,
        35.920091,
        34.999805,
        33.546719,
        31.687850,
        29.552320,
        27.258416,
        24.906153,
        22.574511,
        20.321921,
        18.188614,
        16.199756,
        14.368694,
        12.699910,
        11.191533,
        9.837360,
        8.628421,
        7.554155,
        6.603270,
        5.764338,
        5.026213,
        4.378291,
        3.810668,
        3.314226,
        2.880659,
        2.502465,
        2.172917,
        1.886013,
        1.636428,
        1.419450,
        1.230926,
        1.067204,
        0.925081,
        0.801753,
        0.694767,
        0.601983,
        0.521535,
        0.451795,
        0.391350,
        0.338969,
        0.293581,
        0.254257,
        0.220191
    ]
    known_ending_sir = [16, 0, 134]

    population = 150
    initial_infection = 4
    days = 60
    transmission_rate = 0.43
    recovery_rate = 0.18

    sir_model = SIRModel(population, initial_infection, days, transmission_rate, recovery_rate)

    def callback_test(sir_list):
        pass

    sir_model.run_simulation(callback_test)
    test_sir_data = sir_model.get_model_result_matrix()

    for i in range(days -1):
        assert round(test_sir_data[i][1], 3) == round(known_infection_numbers[i], 3), \
            "Infected numbers for day {0} did not match those returned from working model".format(i)


def test_get_model_matrix():
    """
    Unit test which tests if, after running RunSimulation, getModelMatrix returns an appropraite matrix of our
    model's results
    :return:
    """
    population, initial_infection, days, transmission_rate, recovery_rate, sir_model = __setup_basic_sir_model()

    def callback_test(sir_list):
        pass

    sir_model.run_simulation(callback_test)
    test_sir_data = sir_model.get_model_result_matrix()

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
