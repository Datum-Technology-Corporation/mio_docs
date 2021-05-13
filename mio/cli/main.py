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



"""Moore.io (`mio`) Command Line Interface (CLI)

               <INTERACTIVE DEMO>

Usage:
   mio [-C <path>] [-c <name>=<value>] [--config-env <name>=<envvar>]
       [-p|--paginate | -P|--no-pager] [--debug=<level>]
       <command> [<args> ...]
   mio <command> (-h | --help)
   mio (-h | --help   )
   mio (-v | --version)
   mio (--html-path | --man-path | --info-path)
   mio --list-commands

Options:
   -C <path>
      Run as if mio was started in <path> instead of the current working
      directory. When multiple -C options are given, each subsequent
      non-absolute -C <path> is interpreted relative to the preceding -C <path>.
      If <path> is present but empty, e.g. -C "", then the current working
      directory is left unchanged.
   
   -c <name>=<value>
      Pass a configuration parameter to the command. The value given will
      override values from configuration files. The <name> is expected in the
      same format as listed by `mio config` (subkeys separated by dots).
      
      Note that omitting the `=` in `mio -c foo.bar ...` is allowed and sets
      `foo.bar` to the boolean true value (just like `[foo]bar` would in a
      config file). Including the equals but with an empty value (like
      `mio -c foo.bar= ...`) sets foo.bar to the empty string which
      `mio config --type=bool` will convert to `false`.
      
   --config-env=<name>=<envvar>
      Like `-c <name>=<value>`, give configuration variable <name> a value,
      where <envvar> is the name of an environment variable from which to
      retrieve the value. Unlike `-c` there is no shortcut for directly setting
      the value to an empty string, instead the environment variable itself must
      be set to the empty string. It is an error if the `<envvar>` does not
      exist in the environment. `<envvar>` may not contain an equals sign to
      avoid ambiguity with `<name>` containing one.
   
   -p, --paginate
      Pipe all output into less (or if set, $PAGER) if standard output is a
      terminal.
   
   -P, --no-pager
      Do not pipe mio output into a pager.
    
   --debug=<level>
      Enables debugging and tracing outputs from mio. [default: 0]

   -v, --version
      Prints the mio version and exits.
   
   -h, --help
      Prints the overall synopsis and a list of the most commonly used commands
      and exits. If preceded by <command>
   
   --html-path
      Prints the path, without trailing slash, where mio's HTML
      documentation is installed and exits.
   
   --man-path
      Prints the manpath (see `man(1)`) for the man pages for this version of
      Moore.io and exits.
   
   --info-path
      Prints the path where the Info files documenting this version of mio are
      installed and exits.
   
   --list-commands
      Prints a list of all mio commands and exits.

These are common `mio` commands used in various situations:

start a project (see also: mio help tutorial)
   completion   Produces outputs for shell/editor tab completion of mio commands
   init         Starts project creation dialog
   config       Reads/writes to/from mio configuration space
   ip           Creates, modifies and manages IPs
   new          Creates new source code via the mio template engine
   vcs          Automates version control system tasks
   help         Documentation for all mio commands

run design simulations and manage results
   sim          Performs necessary steps to simulate IP
   regr         Runs regression against IP(s)
   results      Views and manage results from EDA tools

automate EDA tools
   lint         Executes hdl linting tool against IP(s)
   synth        Executes logic synthesis tool against IP(s)
   sta          Executes static timing analysis tool against IP(s)
   formal       Executes formal logic verification tool against IP(s)
   
`mio help -a` and `mio help -g` list available subcommands and some concept
guides. See `mio help <command>` or `mio help <concept>` to read about a
specific subcommand or concept. See `mio help mio` for an overview of the
system."""

commands = """Moore.io (`mio`) Full Command List

Help and Shell/Editor Integration
   help           Documentation for all mio commands
   help-search    Searches mio documentation for the terms provided and lists
                  the results by relevance.
   doctor         Runs a set of checks to ensure mio installation has what it
                  needs to operate properly
   completion     Produces outputs for shell/editor tab completion of mio
                  commands

Project and Environment Management
   init           Starts project creation dialog
   config         Reads/writes to/from mio configuration space
   new            Creates new source code via the mio template engine
   vcs            Automates version control system tasks

IP and Credentials Management
   ip             Creates, modify and manage IPs
   org            Manages organizations
   team           Manages teams
   user           Manages users

Automate Moore.io, F&OS and Vendor EDA Tools
   sim            Performs necessary steps to simulate IP
   regr           Runs regression(s) against IP(s)
   lint           Executes hdl linting tool against IP(s)
   synth          Executes logic synthesis tool against IP(s)
   sta            Executes static timing analysis tool against IP(s)
   formal         Executes formal logic verification tool against IP(s)
   hdl-doc        HDL source code documentation generator
   hdl-refactor   HDL refactorization engine
   
Manage Results and other EDA Tool Outputs
   results        Manages results from EDA tools
   clean          Manages outputs from tools (other than job results)"""



################################################################################
# IMPORTS
################################################################################
from docopt import docopt
from art import *
import sys
import logging
from . import clean
from . import completion
from . import config
from . import doctor
from . import formal
from . import hdl_doc
from . import hdl_refactor
from . import help_search
from . import help
from . import init
from . import ip
from . import lint
from . import new
from . import org
from . import regr
from . import results
from . import sim
from . import sta
from . import synth
from . import team
from . import user
from . import vcs
################################################################################



################################################################################
# GLOBAL VARIABLES
################################################################################
mio_version = '0.1.0.0'
################################################################################



################################################################################
# TOP-LEVEL FUNCTIONS
################################################################################
def proccess_args():
    args = docopt(__doc__)
    argv = [args['<command>']] + args['<args>']
    debug = 0
    if '--debug' in args:
        try:
            debug = int(args['--debug'])
        except ValueError:
            sys.exit(str(ValueError))
        except TypeError:
            debug = 0
        else:
            debug *= 10
            if debug > 0:
                print("Setting debug level to {}".format(debug))
                logging.Logger.setLevel(logging.getLogger(), debug)

    logging.debug('global arguments:\n' + str(args))
    logging.debug('command arguments:\n' + str(argv))

    process_version(args, argv)
    process_list_commands(args, argv)
    process_html_path(args, argv)
    process_info_path(args, argv)
    process_command(args, argv, debug)


def process_version(args, argv):
    print_version_info = False
    if '-v' in args and args['-v']:
        print_version_info = True

    if not print_version_info:
        if '--version' in args and args['--version']:
            print_version_info = True

    if print_version_info:
        print_version()
        sys.exit()


def process_list_commands(args, argv):
    if '--list-commands' in args and args['--list-commands']:
        print_list_of_commands()
        sys.exit()


def process_html_path(args, argv):
    if '--html-path' in args and args['--html-path']:
        print_html_path()
        sys.exit()


def process_man_path(args, argv):
    if '--man-path' in args and args['--man-path']:
        print_man_path()
        sys.exit()


def process_info_path(args, argv):
    if '--info-path' in args and args['--info-path']:
        print_info_path()
        sys.exit()


def process_command(args, argv, debug):
    if args['<command>'] == 'clean':
        print(docopt(clean.__doc__, argv=argv))
    elif args['<command>'] == 'completion':
        print(docopt(completion.__doc__, argv=argv))
    elif args['<command>'] == 'config':
        print(docopt(config.__doc__, argv=argv))
    elif args['<command>'] == 'doctor':
        print(docopt(doctor.__doc__, argv=argv))
    elif args['<command>'] == 'formal':
        print(docopt(formal.__doc__, argv=argv))
    elif args['<command>'] == 'hdl-doc':
        print(docopt(hdl_doc.__doc__, argv=argv))
    elif args['<command>'] == 'hdl-refactor':
        print(docopt(hdl_refactor.__doc__, argv=argv))
    elif args['<command>'] == 'help-search':
        print(docopt(help_search.__doc__, argv=argv))
    elif args['<command>'] == 'help':
        print(docopt(help.__doc__, argv=argv))
    elif args['<command>'] == 'init':
        print(docopt(init.__doc__, argv=argv))
    elif args['<command>'] == 'ip':
        ip.main(argv)
    elif args['<command>'] == 'lint':
        print(docopt(lint.__doc__, argv=argv))
    elif args['<command>'] == 'new':
        print(docopt(new.__doc__, argv=argv))
    elif args['<command>'] == 'org':
        print(docopt(org.__doc__, argv=argv))
    elif args['<command>'] == 'regr':
        print(docopt(regr.__doc__, argv=argv))
    elif args['<command>'] == 'results':
        print(docopt(results.__doc__, argv=argv))
    elif args['<command>'] == 'sim':
        print(docopt(sim.__doc__, argv=argv))
    elif args['<command>'] == 'sta':
        print(docopt(sta.__doc__, argv=argv))
    elif args['<command>'] == 'synth':
        print(docopt(synth.__doc__, argv=argv))
    elif args['<command>'] == 'team':
        print(docopt(team.__doc__, argv=argv))
    elif args['<command>'] == 'user':
        print(docopt(user.__doc__, argv=argv))
    elif args['<command>'] == 'vcs':
        print(docopt(vcs.__doc__, argv=argv))
    else:
        exit_error(args, argv, debug)


def exit_error(args, argv, debug):
    sys.exit("'{}' is not an mio command. See 'mio --list-commands'."
             .format(args['<command>']))


def feature_not_supported():
    sys.exit("Feature not yet supported.")


def print_version():
    print(f"Moore.io CLI v{mio_version}")


def print_list_of_commands():
    print(commands)


def print_html_path():
    feature_not_supported()


def print_man_path():
    feature_not_supported()


def print_info_path():
    feature_not_supported()
################################################################################
