import sys
import platform

def testar_instalacao():
    print("=" * 40)
    print("TESTE DE INSTALAÇÃO DO PYTHON")
    print("=" * 40)

    # Informações do ambiente
    print(f"Versão do Python: {sys.version}")
    print(f"Sistema operacional: {platform.system()} ({platform.release()})")

    # Estruturas de dados básicas
    lista = [1, 2, 3, 4, 5]
    dicionario = {"linguagem": "Python", "curso": "Estrutura de Dados"}
    tupla = ("WSL2", "VS Code", "Ubuntu")

    print("\n--- Testando estruturas de dados ---")
    print(f"Lista: {lista}")
    print(f"Soma da lista: {sum(lista)}")
    print(f"Dicionário: {dicionario}")
    print(f"Tupla: {tupla}")

    # Laço simples
    print("\n--- Testando laço de repetição ---")
    for item in tupla:
        print(f"Ferramenta configurada: {item}")

    print("\n✅ Python instalado e funcionando corretamente!")

if __name__ == "__main__":
    testar_instalacao()