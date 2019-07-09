# Copyright &copy; 2016 ISIS Rutherford Appleton Laboratory, NScD
# Oak Ridge National Laboratory & European Spallation Source
#
# This file is part of Mantid.
# Mantid is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Mantid is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# File change history is stored at: <https://github.com/mantidproject/mantid>.
# Code Documentation is available at: <http://doxygen.mantidproject.org>
from __future__ import (absolute_import, division, print_function)


class FittingResult(object):
    """
    Minimal definition of a class to hold results from a
    fitting problem test.
    """

    def __init__(self):
        self.problem = None
        self.fit_status = None
        self.chi_sq = None

        # Workspace with data to fit
        self.fit_wks = None
        self.params = None
        self.errors = None

        # Time it took to run the Fit algorithm
        self.runtime = None

        # Best minimizer for a certain problem and its function definition
        self.minimizer = None
        self.ini_function_def = None
        self.fin_function_def = None

    def __repr__(self):
        return 'Fitting problem class: minimizer = {0}'.format(self.minimizer)