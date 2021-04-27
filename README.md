# Desafio da Empresa Stone.

Esta pequena api de backend serve para fornecer os dados a api de frontend stone-sword. Sendo responsável pelo armazenamento e gerenciamento dos dados de favoritos do mesmo, ela foi feita de forma a separar as responsabilidades, armazenando apenas os dados essênciais do usuário de forma única. Sendo assim separamos a responsabilidade, mantendo a api de backend responsável pelos dados essênciais (id's e chaves únicas), enquanto a aplicação de frontend se torna responsável pela extração dos dados diretamente da aplicação da marvel.

Para tal foram selecionadas as seguintes técnologias:

* [Python-Falcon](https://falcon.readthedocs.io/en/stable/) Com uma linguagem robusta e de linguagem natural, Python foi selecionado tanto por sua grande versatilidade, quanto facilidade em utilização. O Web Framework Falcon, em especial, é uma ferramenta da linguagem que permite um deploy rápido e eficiente para uma aplicação de backend.

* [ORM - SQLAlchemy](https://www.sqlalchemy.org) Foi utilizado o ORM SQLAlchemy pois permite assim uma abstração melhor quanto a operação do banco de dados, permitindo assim que seja possível migração entre bases, confomre a melhor necessidade.

* [Banco de Dados Postgresql](https://www.postgresql.org) Como dito anteriormente, com o ORM a seleção pelo banco de dados se tornou secundário, neste caso selecionei o postgresql por conta da hospedagem gratuíta utilizada. Caso se tenha acesso a um banco mysql ou de outro baseado em linguagem SQL, basta alterar os dados de conexão do mesmo.

* [Deploy - Heroku](heroku.com) Atualmente esse projeto se encontra para acesso na rede através do endereço abaixo:
 ```stone-shield.herokuapp.com```

Como foi utilizada a opção de conta de desenvolvimento por Hobby (gratuita), isso faz com que possa ter algumas limitações (até 20 acessos simultaneos, 600 Minutos de conexão por dia).


## Requisitos para rodar o projeto de forma Local:

Para rodar o projeto de forma local é necessário se possuir ao menos o Python instalado, em versão 3.8 ou maior, versões inferiores mas acima do 3 podem vir a funcionar, porém pode haver dependencias e falhas nos mesmos.

Atualmente o banco utilizado é uma base PostgreSQL disponível online através do site heroku, porém caso se deseje configurar uma de forma local, basta se instalar a base apropriada e realizar as adequações em seu conector.

Para se baixar o arquivo diretamente do git pode se utilizar o comando abaixo:

 ``` git clone https://github.com/VitorinoAssuncao/stone_shield.git ```

GitHub CLI
 
 ``` gh repo clone VitorinoAssuncao/stone_shield ```

Ou simplesmente acessando  a pagina e selecionando a opção de preferencia para download.

### Instalando os requisitos e acessando o ambiente virtual:

Caso já tenha usado ambientes virtuais, deverá seguir o processo de criação comum ao mesmo, caso nunca tenha feito isso em python é questão de alguns comandos simples:

Em seu terminal python digitar a seguinte linha de comando:

 ``` virtualenv venv ```

Com isso será criada uma nova pasta em seu ambiente com uma estrutura base do python e o instalador pip, após isso é necessário se acionar o ambiente virtual com o seguinte comando:

``` venv\Scripts\activate```

*Note que esse comando deverá ser feito da pasta anterior ao dev_env, seja ela raiz ou não.*

Feito isso, basta rodar o seguinte comando que o instalador do python irá instalar todas as dependências deste projeto:
 ```pip install -r requirements.txt```

## Estruturas Relevantes:

Este projeto consiste em uma aplicação de backend, a qual não possui uma rota raiz (/) atualmente, possuindo apenas 3 estruturas de rotas, conforme a necessidade do usuário:

• users: Referente aos dados de usuários, gerais e individuais. E a partir do ID do usuário que será possível acessar os dados de favoritos únicos ao usuário através das rotas (/users/{id}/characthers ou /users/id/comics).

• characther: Rota responsável pelas listagens de favoritos dos usuários, é a partir dela que podem ser visualizados os dados especificos de alguma entrada na lista ou remover itens específicos da listagem.

• comics: Rota responsável pelas listagens de quadrinhos dos usuários, é a partir dela que podem ser visualizados os dados especificos de alguma entrada na lista ou remover itens específicos da listagem.


## EndPoints

Segue abaixo rotas principais liberadas atualmente no projeto:

``` "/users" : A rota base que retorna uma listagem com os dados de todos os usuários cadastrados.```

``` "/users/login" : A rota responsável pela validação do login e retorno dos dados do usuário logado.```

```"/users/<id>/comics": A rota que permite receber a listagem de quadrinhos favoritos do usuário em formato json.```

```"/comics/{id}": Rota responsável por retornar um item individual da listagem de quadrinhos favoritos (possuem chave primária única). Ela também é a responsável pela remoção de itens da lista de favoritos.```

```"/character/{id}": Rota responsável por retornar um item individual da listagem de personagens favoritos (possuem chave primária única). Ela também é a responsável pela remoção de itens da lista de favoritos.```
