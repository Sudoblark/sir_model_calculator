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


class CsvOutput:
    """
    Handles output of model data to CSV

    Public methods
    ----
    openHandler()
        opens file handler for our csv output file

    closeHandler()
        closes file handler for our csv output file

    write(sirData: list)
        writes provided list values in a new line, with comma as delimiter

    writeHeader()
        writes header value to csv, with comma as delimiter
    """

    def __init__(self, csvPath: str):
        """
        Sets up initial state of class

        :param csvPath:
        """
        self.__csvPath = csvPath
        self.__csvHandler = None

    def openHandler(self):
        """
        opens file handler for output and adds to state
        """
        self.__csvHandler = open(self.__csvPath, "w")

    def closeHandler(self):
        """
        closes file handler recorded in state
        """
        if self.__csvHandler is not None:
            self.__csvHandler.close()

    def write(self, sirData: list):
        """
        Writes new line to csv output, with sirData files delimited by a comma

        :param sirData: values to write to file, should be in format matched by header
        """
        lineData = ', '.join(str(data) for data in sirData)
        lineData += "\n"
        self.__csvHandler.write(lineData)

    def writeHeader(self):
        """
        Writes header to file:

        Day, Susceptible, Infected, Recovered
        """
        self.__csvHandler.write("Day, Susceptible, Infected, Recovered\n")
