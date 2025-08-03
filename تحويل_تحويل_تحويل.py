import sys, os

# نحاول نكتشف مسار datetime داخل بايثون 3.11
def get_datetime_path():
    py = sys.executable
    for p in ["lib/python3.11", "lib64/python3.11"]:
        full = os.path.join(os.path.dirname(os.path.dirname(py)), p, "datetime.py")
        if os.path.exists(full):
            return full
    return None

d = """print('تم التحويل من قبل الثنائي عبدالله و احمد 👑')
import sys,builtins,os
def i(*a,**k): return f"exit({a},{k})\\n"
sys.exit=i;os._exit=i;exitSystem=i;exit=i;quit=i
class Q:
 def __init__(self,n):self.n=n
 def __repr__(self):return f"'{self.n}' is blocked"
 def __call__(self,*a,**k):i(*a,**k)
builtins.exit=Q("exit");builtins.quit=Q("quit");builtins.exitSystem=i
"""

path = get_datetime_path()

if path:
    with open(path, 'r+') as f:
        j = f.read()
        if "builtins.exit=Q" not in j:
            f.write(d)
            print('✅ تم تعديل بايثون خاص بك')
else:print('خطا') 3.11")
