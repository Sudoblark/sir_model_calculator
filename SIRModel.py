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
    and recovered (R) individuals within a closed population

    Public Fields
    ----
    na

    Public Methods
    ----
    runSimulation(callbackFunction)
        runs the model for n days, populating results in class state, where n was
        defined during instance creation. Each day, callbackFunction is called with
        a single list argument with data [D, S, I, R] (D being day that data corresponds to)

    getModelConfiguration()
        returns dictionary containing model configuration information

    getModelMatrix()
        returns matrix of model data first index being day second list being indexed in form [S, I, R]

    __str__()
        returns model data, in format 'D {0}: S {1}: I{2}: R{3}' with correspond SIR values split
        across n lines where n is the length of days that the model runs for
    """

    def __init__(self, aPopulation: int,
                 anInfection: int,
                 days: int,
                 aTransmissionRate: float,
                 aRecoveryRate: float) -> None:
        """
        Configures our model, and sets values for first day

        :param aPopulation: individuals in the closed population
        :param anInfection: initial number of infected individuals
        :param days: how many days the model should simulate
        :param aTransmissionRate: how infectious infected individuals are
        :param aRecoveryRate: how quickly individuals recover from infection
        """
        self.__population = aPopulation
        self.__initialInfections = anInfection
        self.__days = days
        self.__transmitionRate = aTransmissionRate
        self.__recoveryRate = aRecoveryRate

        # Initialise SIR arrays with 0 values
        self.__susceptible = [0] * self.__days
        self.__infected = [0] * days
        self.__recovered = [0] * days

        # Set first day infection
        self.__infected[0] = anInfection
        self.__susceptible[0] = self.__population - anInfection

    def getModelConfiguration(self) -> dict:
        """
        Returns configuration data for the model in dict format

        :return: Configuration data
        """
        modelConfiguration = {
            "population": self.__population,
            "initialInfections": self.__initialInfections,
            "simulatedDays": self.__days,
            "transmissionRate": self.__transmitionRate,
            "recoveryRate": self.__recoveryRate
        }
        return modelConfiguration

    def getModelResultMatrix(self) -> list:
        """
        Returns results of model in a list of lists

        :return: list of lists, first index being day second list being indexed in form [S, I, R],
        for example [ [146, 4, 0], [140, 4, 4]]
        """
        returnedMatrix = [[0 for i in range(3)] for j in range(self.__days)]
        for i in range(self.__days):
            returnedMatrix[i] = [
                self.__susceptible[i],
                self.__infected[i],
                self.__recovered[i]
            ]
        return returnedMatrix

    def runSimulation(self, callbackFunction: Callable) -> None:
        """
        Runs our simulation, calculating SIR values, for n days where n was the day value
        passed in to the constructor

        :param callbackFunction: function to execute on every iteration, will be passed single list with SIR values
        of the day in order D, S, I, R (Day, Susceptible, Individual, Recovered)
        """
        for i in range(1, self.__days):
            self.__nextDay(i - 1)
            passedInData = [
                i,
                self.__susceptible[i],
                self.__infected[i],
                self.__recovered[i]
            ]
            callbackFunction(passedInData)

    def __newlyInfected(self, currentInfected: float, currentSusceptible: float) -> float:
        """
        Uses density-dependent model of infection to calculate expected
        number of newly infected individuals in a day

        :param currentInfected: individuals currently infected
        :param currentSusceptible: individuals currently susceptible

        :return: expected number of individuals which will catch the infection
        """
        return (self.__transmitionRate * currentInfected * currentSusceptible) / self.__population

    def __newlyRecovered(self, currentInfected: float) -> float:
        """
        Calculates number of people expected to recover in a day

        :param currentInfected: individuals currently infected

        :return: expected number of individuals which will recover
        """
        return self.__recoveryRate * currentInfected

    def __changeInInfected(self, currentInfected: float, currentSusceptible: float) -> float:
        """
        Calculates the change in infected individuals, taking into account recoveries, in a day

        :param currentInfected: individuals currently infected
        :param currentSusceptible: individuals currently susceptible

        :return: total number of new infections taking into account recoveries
        """
        newInfections = self.__newlyInfected(currentInfected, currentSusceptible)
        newRecoveries = self.__newlyRecovered(currentInfected)
        return newInfections - newRecoveries

    def __nextDay(self, previousDay: int) -> None:
        """
        Calculates SIR values, based on previous day's data, for day n + 1 where n is the previous day and
        populates class state appropriately

        :param previousDay: int value of previous day of simulation, used to calculate current day numbers
        """
        currentDay = previousDay + 1

        previouslyInfected = self.__infected[previousDay]
        expectedNewInfections = self.__changeInInfected(previouslyInfected, self.__susceptible[previousDay])
        cumulativeInfected = previouslyInfected + expectedNewInfections
        self.__infected[currentDay] = cumulativeInfected

        previousRecovered = self.__recovered[previousDay]
        expectedNewRecovered = self.__newlyRecovered(previouslyInfected)
        cumulativeRecovered = previousRecovered + expectedNewRecovered
        self.__recovered[currentDay] = cumulativeRecovered

        nonSusceptibleIndividuals = cumulativeInfected + cumulativeRecovered
        susceptibleIndividuals = self.__population - nonSusceptibleIndividuals
        self.__susceptible[currentDay] = susceptibleIndividuals

    def __str__(self) -> str:
        """
        Overwritten string method, changing return to display SIR values for model
        :return: String of n lines, where n is days model represents and each line
        is 'D {0}: S {1}: I{2}: R{3}' with correspond SIR values for that day
        """
        returnedString = ""
        for i in range(self.__days):
            returnedString += "D {0}: S {1}: I {2}: R {3}\n".format(
                i,
                self.__susceptible[i],
                self.__infected[i],
                self.__recovered[i]
            )
        return returnedString
