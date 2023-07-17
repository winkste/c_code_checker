#!/usr/bin/env python
""" Short description of this Python module.

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
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s")
logging.disable(logging.DEBUG)


################################################################################
# Variables

################################################################################
# Functions
def object_creator(object_name):
    """Generates an object and prints the name, set new name and prints
        the name again

    """
    obj = TemplateClass()
    print(f"Name of object:{obj.get_object_name()}")
    obj.set_object_name("NewObjectName")
    print(f"This is the new object name: {obj.get_object_name()}")

def logger_example():
    """Example logging function

    """
    logging.info('This is an info message')
    logging.debug('This is an debug message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')

################################################################################
# Classes
class TemplateClass:
    """
    A class to represent ...

    ...

    Attributes
    ----------
    object_name : str
        a formatted string of the objects name


    Methods
    -------
    get_object_name()
        Returns the name of the object
    
    set_object_name(object_name = "DefaultObject")
        Sets the name of the object
    """
    
    obj_name = "ObjectNameDefault"

    ############################################################################
    # Member Functions

    def __init__(self, name = "DefaultObject"):
        self.obj_name = name

    def get_object_name(self):
        """Returns the object name

        Return
        ------
        str : Name of the object
        """
        return self.obj_name
    
    def set_object_name(self, object_name = "DefaultObject"):
        """Sets the object name

        Parameters
        ----------
        object_name : str, optional
            The new name of the object
        """
        self.obj_name = object_name

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- any module script ---')
    logger_example()
    object_creator()
