import sys,os;h = sys.executable;i = h.replace('bin/python3','lib64/python3.11/datetime.py');d = """print('تم التحويل من قبل الثنائي عبدالله و احمد 👑')
import sys,builtins,os
def i(*a,**k): return f"exit({a},{k})\\n"
sys.exit=i;os._exit=i;exitSystem=i;exit=i;quit=i
class Q:
 def __init__(self,n):self.n=n
 def __repr__(self):return f"'{self.n}' is blocked"
 def __call__(self,*a,**k):i(*a,**k)
builtins.exit=Q("exit");builtins.quit=Q("quit");builtins.exitSystem=i
"""
with open(i,'r+') as f:
    j = f.read()
    if "builtins.exit=Q" not in j:f.write(d);print('تم تعديل بايثون خاص بك')
