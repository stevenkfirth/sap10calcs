import sys, os
if not sys.path[0] == os.pardir: sys.path.insert(0, os.pardir)  
import test  # the test module in the parent directory
dir_ = os.path.dirname(__file__)  # the directory where this file is located
test.run_tests(dir_)


