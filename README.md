# 🚀 Automação de Downloads com Python

Fala! Este é um projeto que criei para resolver um problema que todo mundo tem: a bagunça infinita na pasta de Downloads. Como estou cursando **Engenharia de Software** e trabalhando na área de **Infraestrutura de TI**, decidi unir o útil ao agradável e automatizar essa tarefa chata usando Python.

## 💡 O que esse script faz?
Basicamente, ele atua como um "robô organizador". Toda vez que eu rodo o script, ele olha a data em que cada arquivo foi baixado e o move para uma pasta específica do mês correspondente (ex: `01_Janeiro`, `02_Fevereiro`).

## 🛠️ O que usei para construir:
* **Python** (Linguagem principal)
* **Biblioteca `os`**: Para navegar entre as pastas do Windows.
* **Biblioteca `shutil`**: Para fazer o trabalho pesado de mover os arquivos.
* **Biblioteca `datetime`**: Para o script entender "quando" o arquivo chegou ali.

## 🔧 Como rodar na sua máquina:
1. Tenha o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/tanaka2306/organizador-downloads-python.git](https://github.com/tanaka2306/organizador-downloads-python.git)
