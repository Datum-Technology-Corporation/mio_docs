#
# Copyright 2021 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
#
# Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may not use this file except in compliance
# with the License, or, at your option, the Apache License version 2.0. You may obtain a copy of the License at
#
#                                       https://solderpad.org/licenses/SHL-2.1/
#
# Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#



"""Moore.io Sim command
   Performs necessary steps to perform simulation of IP

Usage: mio sim [<ip>] [options]

Options:
    -t <name>   , --test=<name>
    -s <integer>, --seed=<integer>
    -v <level>  , --verbosity=<level>
    -w          , --waves
    -g          , --gui
    -c <flags>  , --cov=<flags>
    -O <level>  , --optimization=<level>
    -L          , --library-creation-only
    -C          , --compilation-only
    -E          , --elaboration-only
    -S          , --simulation-only
    -N <name>   , --netlist=<name>
    -T <name>   , --sdf=<name>
  
Examples:
   mio sim --seed 42 --verbosity high   # Simulates default IP with default test, seed 42 and a high verbosity
   mio sim my_ip -t smoke -s 1 -w --cov=f
   mio sim uvmt_pcie_rc -t scenario_678 -s 8477203 --gui
   mio sim -CE --netlist=latest.sv --sdf=default.sdf"""



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
   logging.debug("sim - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("sim - args: " + str(args))
################################################################################
