#!/usr/bin/env python
""" This module configures and handles the test cases.

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
#import logging
from test_cases.gen_test_case import GenTestCase

################################################################################
# Variables

################################################################################
# Functions
def get_test_cases_for_file_list(files, parameter_file):
    """Returns the tests to execute per file
    """
    test_mgr = TestManager(parameter_file)
    return test_mgr.get_test_cases_for_file_list(files)

################################################################################
# Classes
class TestManager:
    """
    A class to represent the test cases.
    """


    ############################################################################
    # Member Functions

    def __init__(self, parameter_file, name = "TestManager"):
        """default constructor

        Args:
            parameter_file (_type_): parameter file name
            name (str, optional): Object Name. Defaults to "TestManager".
        """
        self.obj_name = name
        self.paramenter_file = parameter_file
        self.test_matrix:dict = {}
        #self._read_test_cases_per_file()
        self._set_dummy_test_matrix()

    def _read_test_cases_per_file(self)->dict:
        """Read all test cases for a particular file

        Returns:
            dict: tests per files as dict
        """
        self.test_matrix = {}
        return self.test_matrix

    def _set_dummy_test_matrix(self)->None:
        """Set a dummy test matrix for testing
        """
        dummy_file = "../examples/basic.c"
        dummy_test_case:list = []
        dummy_test_case.append(GenTestCase())
        self.test_matrix[dummy_file] = dummy_test_case

    def get_object_name(self)->str:
        """Returns the object name

        Return
        ------
        str : Name of the object
        """
        return self.obj_name

    def get_test_cases_for_file_list(self, files:list)->dict:
        """returns the test cases for a particular file

        Args:
            files (list): _description_

        Returns:
            dict: _description_
        """
        return self.test_matrix

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- any module script ---')
