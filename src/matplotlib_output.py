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
        self._susceptible = []
        self._infected = []
        self._recovered = []
        self._days = []

        self._model_configuration = None

    def add_model_configuration_values(self, model_configuration: dict):
        """
        Adds model configuration to state to allow display of relevant legend
        :param model_configuration: Returned configuration of SIRModel
        """
        self._model_configuration = model_configuration

    def update_values(self, sir_data: list) -> None:
        """
        Public interface called to update state values for graphs
        :param sir_data: list of days, correlate to list with values [day, susceptible, infected, recovered]
        """
        self._days.append(sir_data[0])
        self._susceptible.append(sir_data[1])
        self._infected.append(sir_data[2])
        self._recovered.append(sir_data[3])

    def show_graph(self):
        """
        Actually creates and shows line graph
        """
        # Map overlapping lines
        plt.plot(self._days, self._susceptible, color="b", label="susceptible")
        plt.plot(self._days, self._infected, color="r", label="infected")
        plt.plot(self._days, self._recovered, color="g", label="recovered")
        # Add labels
        plt.xlabel("Days since outbreak")
        plt.ylabel("Individuals")
        plt.title("SIR Model showing outbreak in a closed closed_population")
        # Anchor legend outside the plot
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")
        plt.text(len(self._days) + 5, 1.0, str(self._return_model_configuration_text()))
        plt.tight_layout()
        plt.show()

    def _return_model_configuration_text(self):
        return_text = "Population: {0}\nInitial Infections: {1}\nTransmission Rate: {2}\nRecovery Rate: {3}".format(
            self._model_configuration['closed_population'],
            self._model_configuration['initialInfections'],
            self._model_configuration['transmissionRate'],
            self._model_configuration['recoveryRate']
        )
        return return_text
