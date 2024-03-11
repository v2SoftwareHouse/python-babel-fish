
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'use_case_decorator_06d82d755e964ef28231bde4fc29472c.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
