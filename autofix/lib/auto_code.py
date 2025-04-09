import inspect

def get_code():
    # Captura o frame do chamador dois níveis acima (índice 2) para obter o arquivo do main
    frame = inspect.stack()[2]
    # Obtém o módulo do chamador
    module = inspect.getmodule(frame[0])
    # Recupera o caminho do arquivo do módulo chamador
    filename = module.__file__
    with open(filename, 'r', encoding='utf-8') as f:
         code = f.read()
    return code

def save_code(filename, code):
    # Abre (ou cria) o arquivo filename em modo de escrita e salva o código
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code)
