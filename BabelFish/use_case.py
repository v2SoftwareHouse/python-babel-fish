
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'use_case_08f955aa0c864a8abd9f68c30ed8082f.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
