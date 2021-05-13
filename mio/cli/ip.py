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

Usage: mio ip <command> [<args> ...]

"""



################################################################################
# IMPORTS
################################################################################
from docopt import docopt
import sys
from . import ip_access
from . import ip_author
from . import ip_bugs
from . import ip_dedupe
from . import ip_deprecate
from . import ip_diff
from . import ip_docs
from . import ip_edit
from . import ip_exec
from . import ip_explain
from . import ip_explore
from . import ip_fund
from . import ip_hook
from . import ip_install
from . import ip_integrate
from . import ip_list
from . import ip_outdated
from . import ip_pack
from . import ip_prune
from . import ip_publish
from . import ip_repo
from . import ip_run_script
from . import ip_search
from . import ip_set_script
from . import ip_shrinkwrap
from . import ip_tag
from . import ip_test
from . import ip_uninstall
from . import ip_unpublish
from . import ip_update
from . import ip_version
from . import ip_view
################################################################################



################################################################################
# FUNCTIONS
################################################################################
def main(up_args):
    args = docopt(__doc__, argv=up_args)
    argv = [args['<command>']] + args['<args>']

    if args['<command>'] == 'access':
        print(docopt(ip_access.__doc__, argv=argv))
    elif args['<command>'] == 'author':
        print(docopt(ip_author.__doc__, argv=argv))
    elif args['<command>'] == 'bugs':
        print(docopt(ip_bugs.__doc__, argv=argv))
    elif args['<command>'] == 'dedupe':
        print(docopt(ip_dedupe.__doc__, argv=argv))
    elif args['<command>'] == 'deprecate':
        print(docopt(ip_deprecate.__doc__, argv=argv))
    elif args['<command>'] == 'diff':
        print(docopt(ip_diff.__doc__, argv=argv))
    elif args['<command>'] == 'docs':
        print(docopt(ip_docs.__doc__, argv=argv))
    elif args['<command>'] == 'edit':
        print(docopt(ip_edit.__doc__, argv=argv))
    elif args['<command>'] == 'exec':
        print(docopt(ip_exec.__doc__, argv=argv))
    elif args['<command>'] == 'explain':
        print(docopt(ip_explain.__doc__, argv=argv))
    elif args['<command>'] == 'explore':
        print(docopt(ip_explore.__doc__, argv=argv))
    elif args['<command>'] == 'fund':
        print(docopt(ip_fund.__doc__, argv=argv))
    elif args['<command>'] == 'hook':
        print(docopt(ip_hook.__doc__, argv=argv))
    elif args['<command>'] == 'install':
        print(docopt(ip_install.__doc__, argv=argv))
    elif args['<command>'] == 'integrate':
        print(docopt(ip_integrate.__doc__, argv=argv))
    elif args['<command>'] == 'ls':
        print(docopt(ip_list.__doc__, argv=argv))
    elif args['<command>'] == 'outdated':
        print(docopt(ip_outdated.__doc__, argv=argv))
    elif args['<command>'] == 'pack':
        print(docopt(ip_pack.__doc__, argv=argv))
    elif args['<command>'] == 'prune':
        print(docopt(ip_prune.__doc__, argv=argv))
    elif args['<command>'] == 'publish':
        print(docopt(ip_publish.__doc__, argv=argv))
    elif args['<command>'] == 'repo':
        print(docopt(ip_repo.__doc__, argv=argv))
    elif args['<command>'] == 'run-script':
        print(docopt(ip_run_script.__doc__, argv=argv))
    elif args['<command>'] == 'search':
        print(docopt(ip_search.__doc__, argv=argv))
    elif args['<command>'] == 'set-script':
        print(docopt(ip_set_script.__doc__, argv=argv))
    elif args['<command>'] == 'shrinkwrap':
        print(docopt(ip_shrinkwrap.__doc__, argv=argv))
    elif args['<command>'] == 'tag':
        print(docopt(ip_tag.__doc__, argv=argv))
    elif args['<command>'] == 'test':
        print(docopt(ip_test.__doc__, argv=argv))
    elif args['<command>'] == 'uninstall':
        print(docopt(ip_uninstall.__doc__, argv=argv))
    elif args['<command>'] == 'unpublish':
        print(docopt(ip_unpublish.__doc__, argv=argv))
    elif args['<command>'] == 'update':
        print(docopt(ip_update.__doc__, argv=argv))
    elif args['<command>'] == 'version':
        print(docopt(ip_version.__doc__, argv=argv))
    elif args['<command>'] == 'view':
        print(docopt(ip_view.__doc__, argv=argv))
    else:
        exit_error(args['<command>'])


def exit_error(command):
    sys.exit("'ip {}' is not an mio command. See 'mio help'.".format(command))
################################################################################
