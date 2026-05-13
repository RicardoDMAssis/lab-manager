# LabManager - Sistema de Gestão de Inventário

O LabManager é uma API REST desenvolvida para o controle de equipamentos e reservas em laboratórios. O sistema permite o cadastro de itens, o monitoramento de disponibilidade e a gestão de empréstimos vinculados a usuários.

## Tecnologias Utilizadas

* **Python 3.11**
* **Django 5.x**
* **Django REST Framework**
* **PostgreSQL**
* **Docker e Docker Compose**

## Arquitetura do Sistema

O projeto utiliza o padrão de arquitetura do Django REST Framework para separar a lógica de banco de dados da camada de apresentação da API.

* **Models:** Define a estrutura de Laboratórios, Equipamentos e Reservas.
* **Serializers:** Realiza a conversão de modelos em JSON e valida os dados de entrada.
* **Views:** Implementa a lógica de negócio, como a atualização automática de status do equipamento durante reservas e devoluções.

## Funcionalidades da API

### Equipamentos
* Listagem de equipamentos com suporte a filtros por status (ex: disponivel, emprestado).
* CRUD completo (Criação, Leitura, Atualização e Deleção) via endpoints dedicados.

### Reservas
* **Criação de reservas:** Valida se o item está disponível e altera seu status para "emprestado".
* **Listagem:** Exibe as reservas ativas, incluindo o nome do equipamento via ReadOnlyField no Serializer.
* **Devolução:** Endpoint que remove a reserva e retorna o status do equipamento para "disponivel".

## Como Executar o Projeto

### Pré-requisitos
* Docker
* Docker Compose

### Instalação e Execução

1. Clone o repositório:
```bash
git clone git@github.com:RicardoDMAssis/lab-manager.git
cd lab-manager
