import subprocess
import sys
from lib.auto_code import get_code, save_code
from lib.api import generate_response

def fix_code(e):
    print("Erro no código, corrigindo...")
    code = get_code()
    error = str(e)
    response = generate_response(code, error)
    save_code('test.py',response)
    print("Rodando o código corrigido...")
    subprocess.run([sys.executable] + sys.argv)