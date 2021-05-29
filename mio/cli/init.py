# Copyright 2021 Datum Technology Corporation
# SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1
#######################################################################################################################
# Licensed under the Solderpad Hardware License v 2.1 (the "License"); you may not use this file except in compliance
# with the License, or, at your option, the Apache License version 2.0.  You may obtain a copy of the License at
#                                       https://solderpad.org/licenses/SHL-2.1/
# Unless required by applicable law or agreed to in writing, any work distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#######################################################################################################################


"""Moore.io Init command
   Creates .mio.toml configuration file for a new Project.

Usage: mio init [<generator>] [<name>] [options] -- <arguments>

Options:
   -s, --skip-questions
      Skips the questionnaire
   
   -w <path>, --work-dir=<path>
      Specifies the directory in which the IP will be initialized
   
   -f <path>, --args-file=<path>
      Specifies an argument file for the questionnaire (in-line arguments take precedence)

Examples:
   mio init                                                        # Create Project .mio.toml through stock questionnaire
   mio init my_project                                             # Init a scoped and named IP
   mio init my-generator -w ./some_path --skip-questions           # Use a generator but skip the questions and use a custom path
   mio init my_project --args-file=./my_args.txt -- -a --b=1 -c=2  # Use stock behavior, but answer questions with an arg file and inline arguments"""



#######################################################################################################################
# IMPORTS
#######################################################################################################################
from docopt import docopt
import logging
#######################################################################################################################


#######################################################################################################################
# ENTRY POINT
#######################################################################################################################
def main(upper_args):
   logging.debug("init - upper_args: " + str(upper_args))
   args = docopt(__doc__, argv=upper_args, options_first=True)
   logging.debug("init - args: " + str(args))
#######################################################################################################################
