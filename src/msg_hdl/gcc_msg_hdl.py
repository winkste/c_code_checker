#!/usr/bin/env python
""" GCC Message Handler

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
from msg_hdl.gen_msg_hdl import GenericMsgHdl


################################################################################
# Variables

################################################################################
# Functions

################################################################################
# Classes
class GccMsgHdl(GenericMsgHdl):
    """
    A class to represents the gcc handler

    """

    ############################################################################
    # Member Functions

    def __init__(self, name = "GccMessageHandler"):
        super().__init__()
        self.obj_name = name

    def get_object_name(self):
        """Returns the object name

        Return
        ------
        str : Name of the object
        """
        return self.obj_name

    def print_message(self, msg, location, severity):
        """Prints the message to standard output

        Args:
            msg (_type_): _description_
            location (_type_): _description_
            sverity (_type_): _description_
        """
        print(f" GCC FORMAT TBD {location}, {severity}, {msg}")

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- any module script ---')
