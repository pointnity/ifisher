#!/usr/bin/env python
import os
import sys

#for monitor daemon
from service.demo import DemoThread

if __name__ == "__main__":
    DemoThread()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lynn.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
