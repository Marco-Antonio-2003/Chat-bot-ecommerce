import os
import openai
import dotenv


def analise_sentimento(nome_do_produto):
    prompt_sistema = """
    Você é um analisador de sentimentos de avaliações de produtos.
    Escreva um parágrafo com até 50 palavras resumindo as avaliações e depois atribua qual o sentimento geral para o produto.
    Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

    #### Formato de saída

    Nome do produto: 
    Resumo das avaliações:
    Sentimento geral: [aqui deve ser: NEGATIVO, NEUTRO OU POSITIVO.]
    Pontos fortes: [3 bullet points]
    Pontos fracos: [3 bullet points]
    """

    prompt_usuario = carrega(f"./dados/avaliacoes-{nome_do_produto}.txt")
    print(f"Iniciando a análise do produto: {nome_do_produto}")

    tentativas = 0
    while tentativas <3:
        tentativas +=1 
        print(f"Tentativas {tentativas}")
        try:
            #TESTE DE ERRO
            raise openai.error.APIError
            """
            resposta = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {
                        "role": "system",
                        "content": prompt_sistema
                    },
                    {
                        "role": "user",
                        "content": prompt_usuario
                    }
                ]
            )
            """
            salva(f"./dados/analise-{nome_do_produto}", resposta.choices[0].message.content)
            print("Análise concluida")
        except openai.error.AuthenticationError as e:
            print(f"Erro de autenticação: {e}")
        except openai.error.APIError as e:
            print(f"Erro de API: {e}")

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro no carregamento de arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

dotenv.load_dotenv()
openai.api_key = os.getenv("OPEN_API_KEY")

lista_de_produto = ["Tapete de yoga", "Tabuleiro de xadrez de madeira"]
for nome_do_produto in lista_de_produto:
    analise_sentimento(nome_do_produto)
