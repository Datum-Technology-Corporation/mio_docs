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


"""Moore.io Config Command
   Reads/writes to/from mio configuration space.
   
   Moore.io gets it configuration settings from the command line, environment
   variables, `.mio.toml` files, and in some cases, `ip.yml` file(s).
   
   See '.mio.toml' for more information about the mio configuration files.

Usage:
   mio config set    <key>=<value> ...  Writes configuration key/value pair(s)
   mio config get    <key>         ...  Prints configuration key(s)
   mio config delete <key>         ...  Deletes key(s)
   mio config list                      Prints all keys and their values
   mio config edit   [--global]         Opens 'local' .mio.toml configuration file in default editor.

Options:
   -g, --global   Edits the global configuration file
  
Examples:
   mio config set default-ip=uvmt_ss_mem   # Sets Default IP to uvmt_ss_mem
   mio config set default-test=smoke       # Sets Default Test to 'smoke'
   mio config get default-simulator        # Prints Default Simulator to stdout
"""


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
   logging.debug("config - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=False)
   logging.debug("config - args: " + str(args))
########################################################################################################################
