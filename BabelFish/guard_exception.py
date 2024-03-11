
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'guard_exception_93784142e91c4ed5985b3a66ee6956e3.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
