a = 10
while True:
    command = input(">>> ")
    try:
        compiled_code = compile(command, '<string>', 'exec')
        eval(compiled_code)
    except Exception as e:
        print("Error:", e)
