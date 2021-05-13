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



"""Moore.io IP command
   IP Management

Usage:
   mio ip add <user> [<@scope>/]<ip>                                   # Adds author to target IP
   mio ip author rm <user> [<@scope>/]<ip>                             # Removes author from target IP
   mio ip author ls [<@scope>/]<ip>                                    # Lists authors for target IP
   mio ip bugs <ip>                                                    # Tries to guess at the likely location of an IP's bug tracker URL or the mailto URL
   mio ip deprecate <ip>[@<version range>] <message>                   # Updates registry entry for IP (not compatible with workspace IPs)
   mio ip dedupe [--dry-run]                                           # Attempts to simplify the overall structure by moving dependencies further up the tree
   mio ip diff <ip a>[@<version a>] <ip b>[@<version b]                # Performs diff between two IPs
   mio ip docs <ip> [--html | --pdf | --man]                           # Opens IP documentation
   mio ip edit <ip>                                                    # Opens IP source in default editor. If IP is a dependecy, it is first linked into the source tree.
   mio ip exec <ip> <command>                                          # Executes shell command for IP (ex: run scripts in IP bin directory)
   mio ip explain [<ip>]                                               # Prints the chain of dependencies causing a given IP to be installed in the current project.
   mio ip explore <ip> [-- <command>]                                  # Spawns a subshell in the IP directory. If 'command' is specified, it is run and the subshell immediately terminates.
   mio ip fund [<ip>]                                                  # Retrieves information on how to fund the Project dependencies.
   mio ip hook ls [<ip>]                                               # Allows you to manage IP hooks, including adding, removing, listing, and updating.
   mio ip hook add <entity> <url> <secret>                             #
   mio ip hook update <id> <url> [<secret>]                            #
   mio ip hook rm <id>                                                 # 
   mio ip install [--global] [@<scope>/]<name>[@<semver>]              # Installs an IP and any IPs that it depends on
   mio ip install [--global] <name> --repo=<uri> --location=<path>     # 
   mio ip install <name>[@<version>] --location=<path>                 # Installs local IP into global IP location
   mio ip integrate <ip> [@<scope>/]<name>[@<semver>]                  # Adds dependency to IP (does not install anything)
   mio ip integrate <ip> <name> [--local=<path>]                       # Adds dependency to IP (does not install anything)
   mio ip ls [[<@scope>/]<ip>...] [--all]                              # Prints all the versions of IPs that are installed, as well as their dependencies when --all is specified, in a tree structure
   mio ip outdated [[<@scope>/]<ip>...]                                # Checks registry to see if any (or, speific) installed packages are currently outdated
   mio ip pack [[<@scope>/]<pkg>...] [--dry-run]                       # Creates tarball (.tgz) of IP(s) and dependencies
   mio ip prune [[<@scope>/]<ip>...] [--dry-run]                       # Removes extraneous IPs. If an IP name is provided, then only IPs matching one of the supplied names are removed.
   mio ip publish [<ip>] [--tag <tag>] [options]
   mio ip repo [<ip> [<ip>...]]                                        # Opens IP repository page using default app for given VCS
   mio ip run-script 
   mio ip search
   mio ip set-script
   mio ip shrinkwrap
   mio ip uninstall
   mio ip unpublish
   mio ip update [--global] [--clean] [<ip>...]
   mio ip version
   mio ip view 
   mio ip tag add <ip>@<version> [<tag>]                               # Adds, removes, or enumerates distribution tags on an IP
   mio ip tag rm <ip> <tag>                                            # 
   mio ip tag ls [<ip>]                                                # 
   mio ip test                                                         # Runs the IP's specified testing section. Used primarily for contributing computing resources to FOS IPs

Options:
   
  
Examples:
   mio ip new ss_mem      --template='mio-rtl-ss'   # Creates a new IP named 'ss_mem' from template 'mio-rtl-ss'
   mio ip new uvmt_ss_mem --template='mio-dv-ss'    # Creates a new VIP named 'uvmt_ss_mem' from template 'mio-dv-ss'
   mio ip update                                    # Retrieves latest versions of IP dependencies
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
