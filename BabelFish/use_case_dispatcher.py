
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'use_case_dispatcher_b88061fbce7b4e828c04f62db3d5b5de.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
