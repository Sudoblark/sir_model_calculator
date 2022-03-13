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
import argparse
import ArgparserHelp
from SIRModel import SIRModel

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(ArgparserHelp.return_header())
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", action="store_true", help="Show licensing information")

    args = parser.parse_args()
    if args.l:
        print(ArgparserHelp.return_license())
        exit(0)

    test_model = SIRModel(150, 4, 60, 0.43, 0.18)
    print(test_model.getModelConfiguration())
    test_model.runSimulation()
    print(test_model)
