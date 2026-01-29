# Integração de Dados: Python + SQL Server (Automação de Update)

## 📌 Descrição do Projeto
Este projeto consiste em um script de automação desenvolvido em **Python** para realizar a atualização massiva de registros em um banco de dados **SQL Server**. 

O script lê um arquivo `.csv` contendo informações de CPFs processados, realiza o tratamento dos dados utilizando a biblioteca **Pandas** e executa comandos de `UPDATE` no banco de dados através do **SQLAlchemy**, garantindo que o status de comunicação (SMS Enviado) seja refletido corretamente no sistema.

## 🛠️ Tecnologias e Ferramentas
* **Python 3.x**: Linguagem principal.
* **Pandas**: Manipulação e filtragem de dados de forma eficiente.
* **SQLAlchemy**: Abstração e conexão com o banco de dados.
* **PyODBC**: Driver de conexão para SQL Server.
* **T-SQL**: Linguagem de consulta para atualização dos registros.

## ⚙️ Funcionalidades
* **Leitura de Base Externa**: Importação de dados de arquivos CSV com codificação `utf-8`.
* **Data Cleaning**: Seleção de colunas específicas e preparação de variáveis para o banco.
* **Segurança de Dados**: Uso de `bind parameters` (parâmetros nomeados) na query SQL para prevenir ataques de SQL Injection e erros de sintaxe.
* **Conexão Segura**: Utilização de `Trusted_Connection` para autenticação via Windows.

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)

   Instale as dependências:

Bash
pip install pandas sqlalchemy pyodbc
Configure sua string de conexão no arquivo .py.

Execute o script:

Bash
python nome_do_arquivo.py
📝 Estrutura do Código
O fluxo do código segue três pilares principais:

Conexão: Criação do engine via SQLAlchemy.

Preparação: Filtragem do DataFrame para conter apenas o CPF e o novo status.

Execução: Loop otimizado com engine.begin() para garantir a integridade da transação no banco de dados.

⭐ Este projeto faz parte do meu portfólio de automação e engenharia de dados.


---

### Dica para o GitHub:
Se você quiser que o seu GitHub fique ainda mais bonito, recomendo criar um arquivo chamado `.gitignore` na mesma pasta e escrever apenas isto dentro dele:
`*.csv`

Isso vai impedir que o seu arquivo de dados (o CSV com os CPFs) suba para a internet, mantendo a privacidade dos dados.

**Posso te ajudar a configurar esse arquivo `.gitignore` ou você já sabe como faz
