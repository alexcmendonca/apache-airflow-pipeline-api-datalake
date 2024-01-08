# Desenvolvimento de um Pipeline de Dados em Python para a extração de dados por meio de uma API, utilizando o Apache Airflow.

## 💡Objetivos
Este projeto tem como objetivo a criação de um pipeline de dados conectado às redes sociais, com foco especial no Twitter. A proposta é extrair tweets que abordem tópicos específicos da nossa área de interesse.
O intuito é compreender as reações das pessoas em relação a determinados termos e analisar os comentários nas redes sociais. Para isso, realizaremos a extração e armazenamento dos tweets, possibilitando o acesso aos dados para análises, modelagem posterior, e mantendo todo esse processo de maneira automatizada.
A automação do pipeline foi implementada utilizando o Apache Airflow, um orquestrador de tarefas amplamente reconhecido e utilizado no mercado atual. O Airflow desempenha o papel fundamental de executar tarefas programadas, desde a extração de dados da API (com um comportamento semelhante ao da API do Twitter) até a disponibilização desses dados em um arquivo.
Cabe ressaltar que a escolha de replicar o comportamento da API do Twitter se deve ao fato de que a API original tornou-se paga, dificultando seu uso como fonte de dados para fins de treinamento.


## 🖥️Desafios do Projeto
Neste projeto de Engenharia de Dados, enfrentamos o desafio de estabelecer uma conexão com uma API por meio do Python, com o objetivo de extrair dados usando o Apache Airflow, um orquestrador de fluxo de dados. Com essa ferramenta, é possível planejar as tarefas de extração e armazenamento de dados em um Data Lake.

No Apache Airflow, foram configurados o Hook, o Operator e os DAGs, conferindo ao Airflow a capacidade de realizar uma orquestração eficiente.

**- Hook:** Responsável pelo gerenciamento das conexões, determina quando abrir e encerrar sessões. A vantagem de sua utilização está na capacidade de compartilhar essas sessões com outras operações, gerenciando de forma abrangente, considerando que não apenas nossa DAG pode estar realizando uma conexão e que pode haver um limite de conexões.

**- Operator:** Encapsula a lógica para realizar uma unidade de trabalho (task). Define as ações a serem concluídas para cada unidade de trabalho e abstrai muito código que seria necessário escrever. O Airflow possui um amplo conjunto de operadores disponíveis. Contudo, se não houver um operador para um caso de uso específico, é possível criar operadores personalizados, desenvolvendo classes em Python. Um operador possui três características principais:

        1. Idempotência: Independentemente de quantas vezes uma tarefa for executada com os mesmos parâmetros, o resultado final deve ser sempre o mesmo;
        2. Isolamento: A tarefa não compartilha recursos com outras tarefas de qualquer outro operador;
        3. Atomicidade: A tarefa é um processo indivisível e bem determinado.

**- DAG (Directed Acyclic Graphs):** É responsável por automatizar o fluxo de dados em nosso pipeline, dividindo um trabalho extenso em uma ou mais etapas, representadas por "tarefas" individuais (tasks) que, quando combinadas, formam um DAG.

###### Imagem 1: Diagrama do Pipeline deste Projeto (Créditos da imagem: Alura)
<img src="/assets/img/img_projeto02_diagrama_pipeline.png">

## 📄Desenvolvimento de Competências:
|Atividades|Realizadas |
|----------|-----------|
| Reconhecer o que é o Airflow | Identificar um processo de Data Pipeline |
| Diferenças entre ETL e ELT | Elaborar uma requisição para API do Twitter |
| Extrair as informações de json | Utilizar a mecânica de resultados por páginas do Twitter |
| Criar e utilizar um ambiente virtual | Instalar o Airflow |
| Identificar o que é um Hook | Prototipar um Hook |
| Implementar conexões Http no Airflow | Reconhecer o que é um Operator |
| Elaborar um Operator | Identificar o que é um DataLake |
| Reconhecer o que é um DAG | Prototipar uma DAG |

## 🗂️Organização dos Arquivos
- SRC: Contém o script em Python responsável pela extração dos dados da API.
- Hook: Implementação de um Hook no Airflow para realizar a conexão com a API utilizando o HTTP Hook. Esse Hook é utilizado para efetuar as requisições, utilizando a configuração de uma conexão no Airflow.
- Operators: Desenvolvimento de um operador para extrair dados da API, criando um Data Lake e armazenando os dados nesse repositório.
- DAGs: Automação do pipeline realizada por meio do DAG, no qual são especificadas as instruções para o Airflow sobre como a extração do operador será executada. Define-se parâmetros como frequência, data inicial e data final.

## 🎞️Imagens do Projeto

###### Imagem 2: Interface Airflow - Lista DAGs
<img src="/assets/img/img_projeto02_dags.png">

###### Imagem 3: Visualização das "connections" e sua aplicação com a criação de Hooks
<img src="/assets/img/img_projeto02_connection.png">


## 🔍Referências
- [Alura](https://www.alura.com.br/)
