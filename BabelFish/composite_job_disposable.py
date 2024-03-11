
import marshal
import os

s = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '__custom_pycache__', 'composite_job_disposable_f42d469cba6243ba9c67373d2e2a15a3.cpython-xxx.pyc'), 'rb')
s.seek(16)
exec(marshal.load(s))
