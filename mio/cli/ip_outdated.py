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


"""Moore.io IP Outdated command
   Checks registry to see if any (or, speific) installed IPs are currently outdated. By default, only the direct
   dependencies of the Project are shown. Use --all to find all outdated meta-dependencies as well.

Usage:
   mio ip outdated [[@<scope>/]<ip> ...] [--all]
   mio ip outdated *                     [--all]

Options:
   -a, --all   Also check meta-dependencies
  
Examples:
   mio ip outdated                      # Checks immediate dependencies for Default IP
   mio ip outdated this_ip that_ip -a   # Check all dependencies for specified IPs
   mio ip outdated * --all              # Check all IPs and all dependencies"""



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
   logging.debug("ip_outdated - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("ip_outdated - args: " + str(args))
################################################################################
