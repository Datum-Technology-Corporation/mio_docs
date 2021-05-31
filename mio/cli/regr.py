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


"""Moore.io Regr(ession) command
   Executes regression(s) against target IP(s).

Usage:
   mio regr [[@<scope>/]<ip>] <regression>   [options] [-- <parameters>]  Single IP and regression
   mio regr [@<scope>/]<ip> <regression> ... [options]                    Multiple regressions against the same IP
   mio regr [@<scope>/]<ip>/<regression> ... [options]                    Multiple regressions against multiple IPs

Options:
   -f <path>, --params-file=<path>
      Specifies regression parameters file (inline parameters take precedence).
   
   -e <address>, --email=<address>
      Specifies email address(es) (comma separated) to contact once regression(s) have finished.
   
Examples:
   mio regr sanity                             # Run specific regression against Default IP
   mio regr @my_scope/my_ip nightly            # Run specific regression against specific IP
   mio regr nightly -f P2.txt -- multiplier=1  # Run specific regression against specific IP with mixed parameters
   mio regr client_1_bugs client_2_features    # Launch multiple regressions in parallel against Default IP
   mio regr my_ip/sanity some_ip/sanity        # Launch multiple regressions in parallel against multiple IPs"""


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
   logging.debug("regr - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("regr - args: " + str(args))
########################################################################################################################
