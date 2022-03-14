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


def return_header():
    top_line = "SIR Model Animation Copyright (C) 2022 Sudoblark"
    header_string = "-" * len(top_line) + os.linesep
    header_string += top_line + os.linesep
    header_string += "Run 'main -h' for more information" + os.linesep
    header_string += "-" * len(top_line) + os.linesep
    return header_string


def return_license():
    license_string = "Program to model an epidemic outbreak, using a basic SIR Model, then visualise in matplotlib" + \
                     os.linesep
    license_string += "Copyright (C) 2022 Sudoblark" + os.linesep + os.linesep
    license_string += "This program is free software: you can redistribute it and/or modify" + os.linesep
    license_string += "it under the terms of the GNU General Public License as published by" + os.linesep
    license_string += "the Free Software Foundation, either version 3 of the license, or" + os.linesep
    license_string += "(at your opinion) any later version." + os.linesep + os.linesep
    license_string += "This program is distributed in the hope it will be useful," + os.linesep
    license_string += "but WITHOUT ANY WARRANT; without even the implied warranty of" + os.linesep
    license_string += "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the" + os.linesep
    license_string += "GNU General Public License for more details." + os.linesep + os.linesep
    license_string += "You should have received a copy of the GNU General Public License" + os.linesep
    license_string += "along with this program. If not, see <https://www.gnu.org/licenses/>."
    return license_string
