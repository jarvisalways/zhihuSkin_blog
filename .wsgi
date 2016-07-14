#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname


sys.path.insert(0, abspath(dirname(__file__)))


# 这句要改一下
# 根据最终不改版1 这里应该是
from app import init_app
application = init_app()

# from app import app as application

# 结束
