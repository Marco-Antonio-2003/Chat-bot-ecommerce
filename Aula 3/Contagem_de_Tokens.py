import tiktoken

codificador = tiktoken.encoding_for_model("gpt-3.5-turbo")
lista_de_tokens = codificador.encode("Você é um catagorizador de produtos.")
print(lista_de_tokens)
print(len(lista_de_tokens))