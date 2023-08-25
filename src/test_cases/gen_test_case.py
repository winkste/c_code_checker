#!/usr/bin/env python
""" This module defines the generic test case interface.

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

from msg_hdl.gen_msg_hdl import GenericMsgHdl


################################################################################
# Variables

################################################################################
# Functions

################################################################################
# Classes
class GenTestCase:
    """Generic Test Case Class to derive all test cases from
    """


    ############################################################################
    # Member Functions

    def __init__(self, name = "GenTestCase"):
        self.obj_name = name

    def get_object_name(self):
        """Returns the object name

        Return
        ------
        str : Name of the object
        """
        return self.obj_name

    def test_case_func(self, file_name:str, msg_handler:GenericMsgHdl):
        """This function represents the implementation of a test case

        Args:
            file_name (str): name of file to test
            msg_handler (GenericMsgHdl): message handling, e.g. GCC format handler
        """

        logging.debug("File to parse %s", file_name)
        msg_handler.print_message("any message", file_name, "ERROR")


################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- any module script ---')
