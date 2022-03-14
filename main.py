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
from OutputEnum import OutputEnum
import TerminalOutput
from CsvOutput import CsvOutput

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(ArgparserHelp.return_header())
    parser = argparse.ArgumentParser()

    parser.add_argument("output", type=OutputEnum, choices=list(OutputEnum), help="Select output type")
    parser.add_argument("population", type=int, help="Size of closed population")
    parser.add_argument("initialInfection", type=int, help="Infected individuals on day 0")
    parser.add_argument("days", type=int, help="Number of days our simulation should model")
    parser.add_argument("transmissionRate", type=float, help="How infectious infected individuals are")
    parser.add_argument("recoveryRate", type=float, help="How quickly individuals move into recovered state")

    parser.add_argument("-l", action="store_true", help="Show licensing information")
    parser.add_argument("--csvFile", help="Full path to CSV file to output to")

    args = parser.parse_args()
    if args.l:
        print(ArgparserHelp.return_license())
        exit(0)

    sirModel = SIRModel(args.population, args.initialInfection, args.days, args.transmissionRate, args.recoveryRate)

    if args.output is OutputEnum.csv:
        csvHandler = CsvOutput(args.csvFile)
        csvHandler.openHandler()
        csvHandler.writeHeader()
        sirModel.runSimulation(csvHandler.write)
        csvHandler.closeHandler()


    elif args.output is OutputEnum.matplotlib:
        pass
    elif args.output is OutputEnum.terminal:
        TerminalOutput.outputHeader()
        sirModel.runSimulation(TerminalOutput.outputData)
