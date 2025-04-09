from lib.fixcode import fix_code

try:
    with open('test.txt', 'r') as file:
        lines = file.readlines()

except Exception as e:
    fix_code(e)
# Teste