
sourcecode = """def mymethod(x, y):
    return x+y"""

obj = compile(sourcecode, '<String>','exec')
exec(obj)

print(mymethod(10,20))



# output
# ======
# 30