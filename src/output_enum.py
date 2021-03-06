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
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class OutputEnum(Enum):
    """
    Enum of output options for program
    """
    CSV = 'csv'
    MATPLOTLIB = 'matplotlib'
    TERMINAL = 'terminal'

    def __str__(self):
        return self.value
