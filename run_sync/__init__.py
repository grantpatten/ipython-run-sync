"""Automatically yield all futures and replace them with their result."""
from datetime import timedelta

from tornado.gen import IOLoop, Future, with_timeout

from IPython.core.magic import Magics, magics_class, line_magic
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring


@magics_class
class FutureYielder(Magics):
    def __init__(self, shell):
        super(FutureYielder, self).__init__(shell)
        self.shell = shell
        self.timeout = 5

        self.shell.events.register('post_execute', self.post_execute)

    @magic_arguments()
    @argument('timeout', type=int, help="Time in seconds to wait for a future")
    @line_magic
    def run_sync_timeout(self, args):
        """Set the max amount of time to wait for a Future to resolve."""
        args = parse_argstring(self.run_sync_timeout, args)
        self.timeout = args.timeout

    def post_execute(self):
        """Check to see if anything has been set to a running Future after each command.

        Yield the future, and update the user value if so.
        """
        for name, value in self.shell.user_ns.iteritems():
            if isinstance(value, Future) and value.running():
                # Wrap the future in a timeout
                timeout_future = with_timeout(timedelta(seconds=self.timeout), value)
                result = IOLoop.current().run_sync(lambda: timeout_future)
                self.shell.user_ns[name] = result

                if name == "_":
                    print result


def load_ipython_extension(ip):
    ip.register_magics(FutureYielder)
