"""
    Program to model epidemic outbreak, using basic SIR Model, then visualise in matplotlib
    Copyright (C) 2022 Sudoblark

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from typing import Callable


class SIRModel:
    """
    A class to represent a basic SIR model to simulate susceptible (S), infected (I)
    and recovered (R) individuals within a closed closed_population

    Public Methods
    ----
    runSimulation(callback_function)
        runs the model for n days, populating results in class state, where n was
        defined during instance creation. Each day, callback_function is called with
        a single list argument with data [D, S, I, R] (D being day that data corresponds to)

    getModelConfiguration()
        returns dictionary containing model configuration information

    getModelMatrix()
        returns matrix of model data first index being day second list being indexed in form [S, I, R]

    __str__()
        returns model data, in format 'D {0}: S {1}: I{2}: R{3}' with correspond SIR values split
        across n lines where n is the length of days that the model runs for
    """

    def __init__(self, closed_population: int,
                 initial_infected: int,
                 days: int,
                 transmission_rate: float,
                 recovery_rate: float) -> None:
        """
        Configures our model, and sets values for first day

        :param closed_population: individuals in the closed closed_population
        :param initial_infected: initial number of infected individuals
        :param days: how many days the model should simulate
        :param transmission_rate: how infectious infected individuals are
        :param recovery_rate: how quickly individuals recover from infection
        """
        self._closed_population = closed_population
        self._initial_infected = initial_infected
        self._days = days
        self._transmission_rate = transmission_rate
        self.__recovery_rate = recovery_rate

        # Initialise SIR arrays with 0 values
        self._susceptible = [0] * self._days
        self._infected = [0] * days
        self._recovered = [0] * days

        # Set first day infection
        self._infected[0] = initial_infected
        self._susceptible[0] = self._closed_population - initial_infected

    def get_model_configuration(self) -> dict:
        """
        Returns configuration data for the model in dict format

        :return: Configuration data
        """
        model_configuration = {
            "closed_population": self._closed_population,
            "initialInfections": self._initial_infected,
            "simulatedDays": self._days,
            "transmissionRate": self._transmission_rate,
            "recoveryRate": self.__recovery_rate
        }
        return model_configuration

    def get_model_result_matrix(self) -> list:
        """
        Returns results of model in a list of lists

        :return: list of lists, first index being day second list being indexed in form [S, I, R],
        for example [ [146, 4, 0], [140, 4, 4]]
        """
        returned_matrix = [[0 for i in range(3)] for j in range(self._days)]
        for i in range(self._days):
            returned_matrix[i] = [
                self._susceptible[i],
                self._infected[i],
                self._recovered[i]
            ]
        return returned_matrix

    def run_simulation(self, callback_function: Callable) -> None:
        """
        Runs our simulation, calculating SIR values, for n days where n was the day value
        passed in to the constructor. I values are rounded to 6 decimal places.

        :param callback_function: function to execute on every iteration, will be passed single list with SIR values
        of the day in order D, S, I, R (Day, Susceptible, Individual, Recovered)
        """
        for i in range(1, self._days):
            self._next_day(i - 1)
            passed_in_data = [
                i,
                self._susceptible[i],
                self._infected[i],
                self._recovered[i]
            ]
            callback_function(passed_in_data)

    def _newly_infected(self, current_infected: float, current_susceptible: float) -> float:
        """
        Uses density-dependent model of infection to calculate expected
        number of newly infected individuals in a day

        :param current_infected: individuals currently infected
        :param current_susceptible: individuals currently susceptible

        :return: expected number of individuals which will catch the infection
        """
        return (self._transmission_rate * current_infected * current_susceptible) / self._closed_population

    def _newly_recovered(self, current_infected: float) -> float:
        """
        Calculates number of people expected to recover in a day

        :param current_infected: individuals currently infected

        :return: expected number of individuals which will recover
        """
        return self.__recovery_rate * current_infected

    def _change_in_infected(self, current_infected: float, current_susceptible: float) -> float:
        """
        Calculates the change in infected individuals, taking into account recoveries, in a day

        :param current_infected: individuals currently infected
        :param current_susceptible: individuals currently susceptible

        :return: total number of new infections taking into account recoveries
        """
        new_infections = self._newly_infected(current_infected, current_susceptible)
        new_recoveries = self._newly_recovered(current_infected)
        return new_infections - new_recoveries

    def _next_day(self, previous_day: int) -> None:
        """
        Calculates SIR values, based on previous day's data, for day n + 1 where n is the previous day and
        populates class state appropriately

        :param previous_day: int value of previous day of simulation, used to calculate current day numbers
        """
        current_day = previous_day + 1

        previously_infected = self._infected[previous_day]
        expected_new_infections = self._change_in_infected(previously_infected, self._susceptible[previous_day])
        cumulative_infected = round(previously_infected + expected_new_infections, 6)
        self._infected[current_day] = cumulative_infected

        previous_recovered = self._recovered[previous_day]
        expected_new_recovered = self._newly_recovered(previously_infected)
        cumulative_recovered = previous_recovered + expected_new_recovered
        self._recovered[current_day] = cumulative_recovered

        non_susceptible_individuals = cumulative_infected + cumulative_recovered
        susceptible_individuals = self._closed_population - non_susceptible_individuals
        self._susceptible[current_day] = susceptible_individuals

    def __str__(self) -> str:
        """
        Overwritten string method, changing return to display SIR values for model
        :return: String of n lines, where n is days model represents and each line
        is 'D {0}: S {1}: I{2}: R{3}' with correspond SIR values for that day
        """
        returned_string = ""
        for i in range(self._days):
            returned_string += "D {0}: S {1}: I {2}: R {3}\n".format(
                i,
                self._susceptible[i],
                self._infected[i],
                self._recovered[i]
            )
        return returned_string
