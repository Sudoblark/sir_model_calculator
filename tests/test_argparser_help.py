import src.argparser_help as argparser_help


def test_return_header():
    returned_header = argparser_help.return_header()
    assert "SIR Model Animation Copyright (C) 2022 Sudoblark" in returned_header
    assert "main -h" in returned_header


def test_return_license():
    returned_license = argparser_help.return_license()
    assert "Program to model an epidemic outbreak, using a basic SIR Model, then visualise in matplotlib" in returned_license
    assert "This program is free software" in returned_license
    assert "WITHOUT ANY WARRANT" in returned_license
    assert "GNU General Public License" in returned_license
