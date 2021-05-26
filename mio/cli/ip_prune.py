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



"""Moore.io IP Prune command
   Removes extraneous IPs. If an IP name is provided, then only IPs matching one
   of the supplied names are removed.
   
   Extraneous IPs are those present in IP dependencies directories that are not
   listed as any IP's dependency list.

   If the --production flag is specified or the MIO_ENV environment variable is
   set to production, this command will remove the IPs specified in your
   dev-dependencies. Setting --no-production will negate MIO_ENV being set to
   production.

   If the --dry-run flag is used then no changes will actually be made.

Usage:
   mio ip prune [[<@scope>/]<ip> ...] [options]
   mio ip prune *                     [options]

Options:
   -d, --dry-run        Disables any action(s) from taking place
   -p, --production     Enables production mode
   -n, --no-production  Disables production mode
  
Examples:
   mio ip prune                                  # Prune dependency tree for default-ip
   mio ip prune @greece/antikythera diff_eng -p  # Prune multiple IP trees in production mode
   mio ip prune * --no-production                # Prune all IP trees in development mode"""



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
   logging.debug("ip_prune - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("ip_prune - args: " + str(args))
################################################################################
