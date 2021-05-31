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


"""Moore.io Results Command
   Manages results from EDA tools of all types: 'sim', 'sim-logs', 'regr', 'cov', 'waves', 'lint', 'formal', 'emul',
   'synth' and 'timing'.  If the job type is not specified, then the last job type run is assumed.

Usage:
   mio results view    [<type>] [[@<scope>]/<ip> ... | *] [options]  Opens results in $EDITOR or application
   mio results delete  [<type>] [[@<scope>]/<ip> ... | *] [options]  Deletes results from file system
   mio results collate [<type>] [[@<scope>]/<ip> ... | *] [options]  Combines results from separate runs (not all types)
   mio results pack    [<type>] [[@<scope>]/<ip> ... | *] [options]  Creates tarball from results

Options:
   -F       , --force            Forces the deletion of files (if read-only and/or locked)
   -a       , --all              Selects all results for the command, not just the latest results
   -p <path>, --location=<path>  Location for results of 'collate' and 'pack' commands
  
Examples:
   mio results view                          # View latest results for Default IP
   mio results view sim                      # View latest simulation results for Default IP
   mio results view regr *                   # View latest regression results for all IPs
   mio results view lint some_ip             # View latest linting results for a specific IP
   mio results view cov @my_scope/my_ip      # View latest coverage data for a specific IP
   mio results delete -F                     # Forcibly delete the latest results for Default IP
   mio results delete waves --all            # Delete all waveforms for Default IP
   mio results delete --all                  # Delete all results for Default IP
   mio results delete * --all                # Delete all results for all IPs
   mio results collate cov my_ip -p ~/cov    # Collate latest coverage data for a specific IP
   mio results pack synth -p ./netlists.tgz  # Creates tarball with latest synthesis results for Default IP"""


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
   logging.debug("results - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("results - args: " + str(args))
########################################################################################################################
