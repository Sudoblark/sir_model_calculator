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
import matplotlib.pyplot as plt


class MatplotlibOutput:
    """
    Handles output of model data to matplotlib line chart

    Public methods
    ----
    """

    def __init__(self):
        """
        Sets up state to allow periodic updating of line graphs
        """
        self.__susceptible = []
        self.__infected = []
        self.__recovered = []
        self.__days = []

        self.__modelConfiguration = None

    def addModelConfigurationValues(self, modelConfiguration: dict):
        """
        Adds model configuration to state to allow display of relevant legend
        :param modelConfiguration: Returned configuration of SIRModel
        """
        self.__modelConfiguration = modelConfiguration

    def updateValues(self, sirData: list) -> None:
        """
        Public interface called to update state values for graphs
        :param sirData: list of days, correlate to list with values [day, susceptible, infected, recovered]
        """
        self.__days.append(sirData[0])
        self.__susceptible.append(sirData[1])
        self.__infected.append(sirData[2])
        self.__recovered.append(sirData[3])

    def showGraph(self):
        """
        Actually creates and shows line graph
        """
        # Map overlapping lines
        plt.plot(self.__days, self.__susceptible, color="b", label="susceptible")
        plt.plot(self.__days, self.__infected, color="r", label="infected")
        plt.plot(self.__days, self.__recovered, color="g", label="recovered")
        # Add labels
        plt.xlabel("Days since outbreak")
        plt.ylabel("Individuals")
        plt.title("SIR Model showing outbreak in a closed population")
        # Anchor legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")
        plt.text(len(self.__days) + 5, 1.0, str(self.__returnModelConfigurationText()))
        plt.tight_layout()
        plt.show()

    def __returnModelConfigurationText(self):
        returnText = "Population: {0}\nInitial Infections: {1}\nTransmission Rate: {2}\nRecovery Rate: {3}".format(
            self.__modelConfiguration['population'],
            self.__modelConfiguration['initialInfections'],
            self.__modelConfiguration['transmissionRate'],
            self.__modelConfiguration['recoveryRate']
        )
        return returnText
