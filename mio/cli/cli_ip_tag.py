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



"""Moore.io IP Tag command
   Adds, removes, or enumerates distribution tags on an IP

Usage:
   mio ip tag add <ip>@<version> [<tag>]
   mio ip tag rm <ip> <tag>
   mio ip tag ls [<ip>]

Options:
   
  
Examples:
   
"""



################################################################################
# IMPORTS
################################################################################
from docopt import docopt
################################################################################



################################################################################
# FUNCTIONS
################################################################################
################################################################################



################################################################################
# ENTRY POINT
################################################################################
if __name__ == '__main__':
    if sys.version_info >= (3, 0):
        print(docopt(__doc__))
    else:
        sys.exit("Python version (" + \
             str(sys.version_info) + \
             ") not supported. Need 3.0 or higher.")
################################################################################
