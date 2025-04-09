import google.generativeai as genai
import re

GOOGLE_API_KEY = "x"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def normalize_response(response: str) -> str:
    """
    Extrai o conteúdo entre os delimitadores de bloco de código (```python ... ```)
    e retorna apenas o código, sem qualquer texto adicional.
    Se não encontrar os delimitadores, retorna o texto original sem espaços
    extras nas extremidades.
    """
    # Procura por um bloco de código com ou sem a indicação "python"
    pattern = r"```(?:python)?\n(.*?)```"
    match = re.search(pattern, response, re.DOTALL)
    if match:
        code = match.group(1)
    else:
        code = response
    # Remove espaços vazios ou quebras de linha no início e fim
    return code.strip()

def generate_response(code: str, error: str) -> str:
    """Generate a response using the Gemini model."""
    
    prompt = f"""
    Você é um assistente de programação. Sua tarefa é analisar um código Python e o erro que ele gerou, e retornar APENAS o código corrigido, sem qualquer explicação adicional ou comentários, porem tenha certesa de arrumar o codigo da melhor maneira possivel, e ATENÇÃO, NÃO REMOVA O TRY EXEPT COM A FUNÇÃO 'fix_code(e)' caso precise fazer outros except faça de um modo que caso de um erro diferente do que você arrumou ira cair no fix_code, ou seja um erro ja arrumado usando um 'raise' não deve cair no fix_code.

    Exemplo:
    Código: print("Hello, world!)
    Erro: SyntaxError: EOL while scanning string literal
    Resposta: print("Hello, world!")

    Agora, analise o código e o erro abaixo e retorne somente o código corrigido:
    Código: {code}
    Erro: {error}
    """
    
    try:
        response = model.generate_content(prompt)
        
        normalize_responsed_response = normalize_response(response.text)
        
        return normalize_responsed_response
    except Exception as e:
        return f"Error: {str(e)}"