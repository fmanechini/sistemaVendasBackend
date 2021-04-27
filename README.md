# Sistema de Vendas

Esse projeto representa um sistema de vendas para um estabelecimento qualquer

O projeto foi desenvolvido utilizando Python, Django e Django Rest Framework com 
banco de dados PostgreSQL. A configuração e preparação do Ambiente utiliza
Docker e Docker Compose.

## O sistema permite:
  - Cadastro e consulta de Clientes
  - Cadastro e consulta de Vendedores
  - Cadastro e consulta de Produtos ou Serviços com seus preços e comissões
  - Cadastro e consolta de Vendas com Data da venda, vendedor e cliente associados, produtos e quantidades
  - Consulta do valor de comissão total que um vendedor recebeu dentro de um determinado período

## Algumas particularidades do sistema:
  - As comissões de um Produto ou serviço devem ter entre 0 e 10% de comissão
  - Vendas ocorridas entre 00:00 e 12:00 a comissão de cada item deve ser no máximo 5%
  - Vendas ocorridas entre 12:00:01 e 23:59:59 a comissão de cada item deve ser no mínimo 4%

# Instruções para utilização do Projeto:

Será necessário a utilização do Docker e Docker Composer. Para instalá-los seguir instruções:

### Instalação Docker

https://docs.docker.com/engine/install/

### Instalação Docker Compose

https://docs.docker.com/compose/install/

### Preparação do ambiente

Executar o docker compose build

``` docker-compose build ```

Fazer as migrações do Banco de dados:

```docker-compose run app sh -c "python manage.py makemigrations sales ```

```docker-compose run app sh -c "python manage.py migrate ```

Para utilizar o sistema:

```docker-compose up ```

Para executar os testes unitários:

```docker-compose run app sh -c "python -m pytest ```