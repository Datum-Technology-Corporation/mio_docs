# Copyright 2021 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
########################################################################################################################
# Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may not use this file except in compliance
# with the License, or, at your option, the Apache License version 2.0.  You may obtain a copy of the License at
#                                       https://solderpad.org/licenses/SHL-2.1/
# Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
########################################################################################################################


"""Moore.io New command
   Invokes the mio code generator system.  If no generator name is specified, the user is prompted to select from a
   list of what is currently installed (and applicable in this context).  All arguments right of '--' are passed
   untouched to the generator.

Usage: mio new [[@<scope>/]<ip>] [[@<scope>/]<generator>] [options] [-- <args>]

Options:
   -f <path>, --args-file=<path>  Specifies arguments file (inline arguments take precedence)

Examples:
   mio new uvm-test -- name=smoke                       # Create new UVM test for Default IP named 'smoke'
   mio new @my_scope/my_ip reg-block -a ./reg-spec.yml  # Create new Register Block for specific IP with an arguments file
   mio new some_ip reg -- name=abc size=4B              # Create new Register for a specific IP with inline arguments"""


########################################################################################################################
# IMPORTS
########################################################################################################################
from docopt import docopt
import logging
########################################################################################################################


########################################################################################################################
# ENTRY POINT
########################################################################################################################
def main(upper_args):
   logging.debug("new - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("new - args: " + str(args))
########################################################################################################################
