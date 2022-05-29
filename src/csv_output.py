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
import logging

logger = logging.getLogger(__name__)

class CsvOutput:
    """
    Handles output of model data to CSV

    Public methods
    ----
    open_handler()
        opens file handler for our csv output file

    close_handler()
        closes file handler for our csv output file

    write(sir_data: list)
        writes provided list values in a new line, with comma as delimiter

    write_header()
        writes header value to csv, with comma as delimiter
    """

    def __init__(self, sir_path: str):
        """
        Sets up initial state of class

        :param sir_path: Path of CSV to write to
        """
        self._csv_path = sir_path
        self._csv_handler = None

    def open_handler(self):
        """
        opens file handler for output and adds to state
        """
        self._csv_handler = open(self._csv_path, "w", encoding="utf-8")

    def close_handler(self):
        """
        closes file handler recorded in state
        """
        if self._csv_handler is not None:
            self._csv_handler.close()

    def write(self, sir_data: list):
        """
        Writes new line to csv output, with sir_data files delimited by a comma

        :param sir_data: values to write to file, should be in format matched by header
        """
        line_data = ', '.join(str(data) for data in sir_data)
        line_data += "\n"
        self._csv_handler.write(line_data)

    def write_header(self):
        """
        Writes header to file:

        Day, Susceptible, Infected, Recovered
        """
        self._csv_handler.write("Day, Susceptible, Infected, Recovered\n")
