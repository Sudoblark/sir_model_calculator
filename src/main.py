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
import sys
import argparse
import argparser_help
from sir_model import SIRModel
from output_enum import OutputEnum
import terminal_output
from csv_output import CsvOutput
from matplotlib_output import MatplotlibOutput
import logging

logger = logging.getLogger(__name__)
logger_formatter = logging.Formatter(fmt="%(asctime)s %(filename)s: %(levelname)s: %(message)s")
logging.basicConfig(format="%(asctime)s %(filename)s: %(levelname)s: %(message)s")

log_level_dictionary = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(argparser_help.return_header())
    parser = argparse.ArgumentParser()

    parser.add_argument("output", type=OutputEnum, choices=list(OutputEnum), help="Select output type")
    parser.add_argument("closed_population", type=int, help="Size of closed closed_population")
    parser.add_argument("initial_infection", type=int, help="Infected individuals on day 0")
    parser.add_argument("days", type=int, help="Number of days our simulation should model")
    parser.add_argument("transmission_rate", type=float, help="How infectious infected individuals are")
    parser.add_argument("recovery_rate", type=float, help="How quickly individuals move into recovered state")

    parser.add_argument("-l", action="store_true", help="Show licensing information")
    parser.add_argument("--csvFile", help="Full path to CSV file to output to")
    parser.add_argument("--logLevel", help="Log level for the application", type=str, choices=list(log_level_dictionary), default="INFO")

    args = parser.parse_args()

    if args.logLevel:
        loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
        for logger in loggers:
            logger.setLevel(log_level_dictionary[args.logLevel])
    if args.l:
        print(argparser_help.return_license())
        sys.exit(0)

    logger.debug("Program entry")
    sirModel = SIRModel(args.closed_population, args.initial_infection, args.days, args.transmission_rate, args.recovery_rate)

    if args.output is OutputEnum.CSV:
        logger.debug("csv output entry")
        csvHandler = CsvOutput(args.csvFile)
        csvHandler.open_handler()
        csvHandler.write_header()
        sirModel.run_simulation(csvHandler.write)
        csvHandler.close_handler()
        logger.debug("csv outputter successfully written to " + args.csvFile)
    elif args.output is OutputEnum.MATPLOTLIB:
        logger.debug("matplotlib output entry")
        MatplotlibHandler = MatplotlibOutput()
        sirModel.run_simulation(MatplotlibHandler.update_values)
        MatplotlibHandler.add_model_configuration_values(sirModel.get_model_configuration())
        MatplotlibHandler.show_graph()
    elif args.output is OutputEnum.TERMINAL:
        logger.debug("terminal output entry")
        terminal_output.output_header()
        sirModel.run_simulation(terminal_output.output_data)
