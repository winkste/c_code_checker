#!/usr/bin/env python
""" C Code Checker main module.

Longer description of this module.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "One solo developer"
__authors__ = ["One developer", "And another one", "etc"]
__contact__ = "mail@example.com"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "YYYY/MM/DD"
__deprecated__ = False
__email__ =  "mail@example.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"


################################################################################
# Imports
import logging
from cmd_line.cli_handler import parse_command_line
from test_cases.test_manager import get_test_cases_for_file_list
#from test_cases.gen_test_case import GenTestCase
from msg_hdl.message_factory import create_message_handler
from msg_hdl.gen_msg_hdl import GenericMsgHdl


################################################################################
# Variables

################################################################################
# Functions
def ccs_main():
    """Main function of the C Code Checker program
    """

    # check commandline parameter, parameter:
    # single c file or path to files, path to xml config for tests
    files_to_parse:str = None
    parameter_file:str = None
    files_to_parse, parameter_file = parse_command_line()

    # create the output message handler
    msg_hdl:GenericMsgHdl = create_message_handler()

    # create test manager with help of parameter file and message handler
    test_matrix:dict = get_test_cases_for_file_list(files_to_parse, parameter_file)


    # start processing the c file / files
    for file, test_case_list in test_matrix.items():
        for single_test_case in test_case_list:
            single_test_case.test_case_func(file, msg_hdl)

################################################################################
# Classes

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- C Code Checker ---')
    MSG_FORMAT = "%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=MSG_FORMAT)
    ccs_main()
