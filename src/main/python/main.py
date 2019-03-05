from fbs_runtime.application_context import ApplicationContext

from mainwindow import *
from Export import *
from log import *

import sys

class AppContext(ApplicationContext):
    def run(self):
        startLogging()
        export_init()
        main_window()

if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)