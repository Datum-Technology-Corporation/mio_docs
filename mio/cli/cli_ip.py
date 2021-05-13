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
import cli_ip_access
import cli_ip_author
import cli_ip_bugs
import cli_ip_dedupe
import cli_ip_deprecate
import cli_ip_diff
import cli_ip_docs
import cli_ip_edit
import cli_ip_exec
import cli_ip_explain
import cli_ip_explore
import cli_ip_fund
import cli_ip_hook
import cli_ip_install
import cli_ip_integrate
import cli_ip_ls
import cli_ip_outdated
import cli_ip_pack
import cli_ip_prune
import cli_ip_publish
import cli_ip_repo
import cli_ip_run_script
import cli_ip_search
import cli_ip_set_script
import cli_ip_shrinkwrap
import cli_ip_tag
import cli_ip_test
import cli_ip_uninstall
import cli_ip_unpublish
import cli_ip_update
import cli_ip_version
import cli_ip_view
################################################################################



################################################################################
# FUNCTIONS
################################################################################
def ip_main():
    if args['<command>'] == 'access':
        print(docopt(mio_ip_access.__doc__, argv=argv))
    elif args['<command>'] == 'author':
        print(docopt(mio_ip_author.__doc__, argv=argv))
    elif args['<command>'] == 'bugs':
        print(docopt(mio_ip_bugs.__doc__, argv=argv))
    elif args['<command>'] == 'dedupe':
        print(docopt(mio_ip_dedupe.__doc__, argv=argv))
    elif args['<command>'] == 'deprecate':
        print(docopt(mio_ip_deprecate.__doc__, argv=argv))
    elif args['<command>'] == 'diff':
        print(docopt(mio_ip_diff.__doc__, argv=argv))
    elif args['<command>'] == 'docs':
        print(docopt(mio_ip_docs.__doc__, argv=argv))
    elif args['<command>'] == 'edit':
        print(docopt(mio_ip_edit.__doc__, argv=argv))
    elif args['<command>'] == 'exec':
        print(docopt(mio_ip_exec.__doc__, argv=argv))
    elif args['<command>'] == 'explain':
        print(docopt(mio_ip_explain.__doc__, argv=argv))
    elif args['<command>'] == 'explore':
        print(docopt(mio_ip_explore.__doc__, argv=argv))
    elif args['<command>'] == 'fund':
        print(docopt(mio_ip_fund.__doc__, argv=argv))
    elif args['<command>'] == 'hook':
        print(docopt(mio_ip_hook.__doc__, argv=argv))
    elif args['<command>'] == 'install':
        print(docopt(mio_ip_install.__doc__, argv=argv))
    elif args['<command>'] == 'integrate':
        print(docopt(mio_ip_integrate.__doc__, argv=argv))
    elif args['<command>'] == 'ls':
        print(docopt(mio_ip_ls.__doc__, argv=argv))
    elif args['<command>'] == 'outdated':
        print(docopt(mio_ip_outdated.__doc__, argv=argv))
    elif args['<command>'] == 'pack':
        print(docopt(mio_ip_pack.__doc__, argv=argv))
    elif args['<command>'] == 'prune':
        print(docopt(mio_ip_prune.__doc__, argv=argv))
    elif args['<command>'] == 'publish':
        print(docopt(mio_ip_publish.__doc__, argv=argv))
    elif args['<command>'] == 'repo':
        print(docopt(mio_ip_repo.__doc__, argv=argv))
    elif args['<command>'] == 'run-script':
        print(docopt(mio_ip_run_script.__doc__, argv=argv))
    elif args['<command>'] == 'search':
        print(docopt(mio_ip_search.__doc__, argv=argv))
    elif args['<command>'] == 'set-script':
        print(docopt(mio_ip_set_script.__doc__, argv=argv))
    elif args['<command>'] == 'shrinkwrap':
        print(docopt(mio_ip_shrinkwrap.__doc__, argv=argv))
    elif args['<command>'] == 'tag':
        print(docopt(mio_ip_tag.__doc__, argv=argv))
    elif args['<command>'] == 'test':
        print(docopt(mio_ip_test.__doc__, argv=argv))
    elif args['<command>'] == 'uninstall':
        print(docopt(mio_ip_uninstall.__doc__, argv=argv))
    elif args['<command>'] == 'unpublish':
        print(docopt(mio_ip_unpublish.__doc__, argv=argv))
    elif args['<command>'] == 'update':
        print(docopt(mio_ip_update.__doc__, argv=argv))
    elif args['<command>'] == 'version':
        print(docopt(mio_ip_version.__doc__, argv=argv))
    elif args['<command>'] == 'view':
        print(docopt(mio_ip_view.__doc__, argv=argv))
    else:
        exit_error():

def exit_error():
    sys.exit("'ip {}' is not an mio command. See 'mio help'." \
             .format(args['<command>']))
################################################################################



################################################################################
# ENTRY POINT
################################################################################
if __name__ == '__main__':
    if sys.version_info >= (3, 0):
        ip_main()
    else:
        sys.exit("Python version (" + \
             str(sys.version_info) + \
             ") not supported. Need 3.0 or higher.")
################################################################################
