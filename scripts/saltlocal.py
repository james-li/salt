#!/usr/bin/env python2

import sys
import os
import platform

def get_python2_minor():
    if hasattr(sys.version_info, 'index'):
        return sys.version_info[1]
    elif hasattr(sys.version_info, 'minor'):
        return sys.version_info.minor
    else:
        sys.exit(1)

def getSaltCall(prefix):
    libpath = os.path.abspath(os.path.join(prefix, "lib64/python2.{0}/site-packages".format(get_python2_minor())))
    sys.path.insert(0, libpath)
    libpath = os.path.abspath(os.path.join(prefix, "lib/python2.{0}/site-packages".format(get_python2_minor())))
    sys.path.insert(0, libpath)


    conf_file = os.path.join(prefix, './etc/salt/minion')
    if not os.path.isfile(conf_file):
        os.makedirs(os.path.dirname(conf_file))
        with open(conf_file, 'w') as f:
            f.write('{"id" :"%s"}'%(platform.uname()[1]))
    from salt.utils import parsers
    from salt.utils.verify import verify_log
    import salt
    import salt.cli.caller
    import salt.defaults.exitcodes
    class SaltLocalCall(parsers.SaltCallOptionParser):
        def run(self, args):
            args.extend(['-c', os.path.abspath(os.path.join(prefix, './etc/salt'))])
            self.parse_args(args = args)
            self.config['file_client'] = 'local'
            self.setup_logfile_logger()
            verify_log(self.config)
            caller = salt.cli.caller.BaseCaller(self.config)
            if self.options.doc:
                caller.print_docs()
                self.exit(salt.defaults.exitcodes.EX_OK)

            if self.options.grains_run:
                caller.print_grains()
                self.exit(salt.defaults.exitcodes.EX_OK)
            caller.run()
    return SaltLocalCall()




