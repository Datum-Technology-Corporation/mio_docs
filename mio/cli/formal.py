## 
## Copyright 2021 Datum Technology Corporation
## SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
## 
## Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may
## not use this file except in compliance with the License, or, at your option,
## the Apache License version 2.0. You may obtain a copy of the License at
## 
##     https://solderpad.org/licenses/SHL-2.1/
## 
## Unless required by applicable law or agreed to in writing, any work
## distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
## WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
## License for the specific language governing permissions and limitations
## under the License.
## 



"""Moore.io Formal command
   Executes formal logic verification tool against IP(s)

Usage: mio formal [<ip>...] [options]

Options:
   # TBD

Examples:
   mio formal my_pcie_rc my_pcie_ep
"""



################################################################################
# IMPORTS
################################################################################
from docopt import docopt
import logging
################################################################################



################################################################################
# FUNCTIONS
################################################################################
################################################################################



################################################################################
# ENTRY POINT
################################################################################
def main(upper_args):
   logging.debug("formal - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("formal - args: " + str(args))
################################################################################
