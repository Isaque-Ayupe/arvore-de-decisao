🩺 Sistema de Classificação de Risco Cardíaco — ID3 (Árvore de Decisão)

Este projeto implementa um sistema completo de classificação de pacientes em Baixo, Médio ou Alto Risco de doença cardíaca usando o algoritmo ID3 (entropia + ganho de informação).
Inclui interface gráfica em Tkinter, CRUD de registros, salvamento em CSV e visualização da árvore treinada.

🚀 Funcionalidades
✅ Dataset

Estrutura em CSV: Nome, Idade, Pressao, Colesterol, Fumante, Risco

Suporte a carregamento e salvamento.

✅ CRUD

Inserir novos registros

Listar dados atuais

Salvar dataset

Carregar dataset existente

✅ Algoritmo ID3

Cálculo de entropia

Cálculo de ganho de informação

Construção recursiva da árvore

Predição para novos pacientes

✅ Interface Tkinter

Tela inicial organizada com botões

Formulário para inserir paciente

Tabela simples de visualização

Botão para treinar árvore

Botão para visualizar árvore em texto (hierarquia indentada)

🧠 Como o sistema funciona

O usuário insere registros pelo GUI

O dataset é salvo em data.csv

Ao clicar em Treinar Árvore, o ID3 constrói a árvore com base nos atributos

A árvore treinada pode ser visualizada (formato textual indentado)

O usuário pode classificar novos pacientes usando os mesmos atributos

O sistema percorre a árvore até encontrar o nó folha correspondente

📁 Estrutura do projeto
/
├── data.csv             # Dataset de exemplo
├── dataset.py           # CRUD, leitura e escrita de CSV
├── id3.py               # Implementação do algoritmo ID3
├── tree_print.py        # Função para imprimir a árvore
├── gui.py               # Interface Tkinter (arquivo principal)
└── README.md            # Este arquivo

▶️ Como executar

Certifique-se de ter Python 3.10+ instalado.

Instale dependências (não tem libs externas):

pip install tk


(em Windows geralmente já vem incluso)

Rode a interface:

python gui.py

🛠 Tecnologias

Python 3

Tkinter

CSV (padrão da lib csv)

Algoritmo ID3 implementado manualmente

✨ Próximas melhorias (versão BETA)

Visualização gráfica da árvore

Interface modernizada com ttkbootstrap

Avaliação do modelo (acurácia, matriz de confusão)

Exportar árvore em JSON

Gerar .exe para Windows (PyInstaller)

👨‍💻 Autor
Isaque Ayupe
Projeto desenvolvido como estudo de caso para disciplina acadêmica, visando entendimento prático de árvores de decisão e o algoritmo ID3.
