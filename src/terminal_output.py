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
import os


def output_data(sir_data: list) -> None:
    """
    Outputs SIR data to terminal, in format: Dau, Susceptible, Infected, Recovered
    """
    output_string = ', '.join(str(data) for data in sir_data)
    print(output_string)


def output_header() -> None:
    """
    Outputs header to terminal to contextualise data
    """
    header_string = "SIR model data - terminal output" + os.linesep
    header_string += "-" * len(header_string) + os.linesep
    header_string += "Day, Susceptible, Individual, Recovered" + os.linesep
    print(header_string)
