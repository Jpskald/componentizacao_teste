# 📦 Laboratório de Componentização & DRY em Django

Este projeto é uma **Prova de Conceito (PoC) / Projeto Experimental** voltado a testar padrões avançados de **componentização**, **reutilização de código** e o princípio **DRY (Don't Repeat Yourself)** utilizando o framework [Django](https://www.djangoproject.com/) e [Bootstrap 5](https://getbootstrap.com/).

O domínio escolhido para o teste prático foi um **Sistema de Controle de Estoque** (Gestão de Categorias, Produtos e Movimentações de Entrada e Saída).

---

## 🎯 Objetivo do Experimento

Em aplicações tradicionais, a criação de módulos CRUD (Create, Read, Update, Delete) costuma gerar código redundante: múltiplas views com a mesma estrutura de formulário e listagem, e dezenas de templates HTML quase idênticos espalhados pelo repositório.

O objetivo deste projeto foi explorar o limite da componentização em duas frentes:
1. **Frontend**: Centralizar o design e as telas em templates universais e dinâmicos.
2. **Backend**: Unificar o processamento de CRUDs em views genéricas configuradas dinamicamente via injeção de parâmetros nas rotas (`urls.py`).
3. **Equilíbrio Arquitetural**: Demonstrar quando vale a pena generalizar (cadastros simples) e quando isolar regras de negócio específicas (movimentações financeiras e de estoque com *Fat Models*).

---

## 🧩 Arquitetura de Componentização

### 1. Templates Genéricos (`app/templates/comum/`)
Em vez de ter um `listar.html` e `form.html` para cada entidade do sistema, o projeto utiliza templates mestres que se adaptam aos dados recebidos:

- **[`base.html`]: Layout base com Navbar responsiva, suporte a Bootstrap 5 e container principal.
- **[`listar_generico.html`]: Tabela universal que itera dinamicamente sobre cabeçalhos e campos configurados, com botões contextuais de Novo Registro, Edição e Exclusão.
- **[`form_generico.html`]: Formulário unificado de criação e edição com tratamento de campos CSRF e botões de ação e cancelamento.
- **[`confirmar_exclusao_generico.html`]: Tela de confirmação e alerta de exclusão segura de registros.

### 2. Views Universais no Backend (`app/views.py`)
Foram criadas funções de view genéricas para lidar com as operações comuns:
- `view_generica_listar`
- `view_generica_criar`
- `view_generica_editar`
- `view_generica_excluir`

Essas funções recebem metadados injetados via `urls.py` (`modelo`, `form_class`, `titulo`, `campos`, `cabecalhos`, `nome_url_sucesso`, etc.), permitindo que novos modelos sejam expostos no sistema com zero linhas adicionais de views.

### 3. Injeção Dinâmica em Rotas (`config/urls.py`)
As rotas do sistema atuam como orquestradoras declarativas:

```python
# Exemplo de configuração declarativa para Produtos
path('produtos/', view_generica_listar, {
    'modelo': Produto,
    'template_name': 'comum/listar_generico.html',
    'titulo': 'Listagem de Produtos',
    'campos': ['id', 'nome', 'categoria', 'preco', 'quantidade_estoque'],
    'cabecalhos': ['#', 'Nome', 'Categoria', 'Preço (R$)', 'Qtd. em Estoque'],
    'nome_url_criar': 'produto_criar',
    'nome_url_editar': 'produto_editar',
    'nome_url_excluir': 'produto_excluir',
}, name='produto_listar'),
```

### 4. Regras de Negócio Críticas & Fat Models
Nem tudo deve ser 100% genérico. Operações com regras de domínio sensíveis (como **Entrada (Compra)** e **Saída (Venda)** de produtos) foram mantidas em views dedicadas (`registrar_compra`, `registrar_venda`) com integridade assegurada diretamente no Model:
- **`clean()` & `save()`**: Validações de estoque negativo e cálculo automático de saldo e preço unitário garantem consistência antes de qualquer persistência.

---

## 📁 Estrutura do Projeto

```text
componentizacao_teste/
│
├── config/                  # Configurações do projeto Django
│   ├── settings.py          # Configurações gerais e apps instalados
│   ├── urls.py              # Injeção de dependências e mapeamento de rotas
│   └── wsgi.py
│
├── app/                     # Aplicação de estoque e componentes
│   ├── models.py            # Modelos: Categoria, Produto, Movimentacao
│   ├── forms.py             # ModelForms estilizados
│   ├── views.py             # Views Genéricas + Views Especializadas
│   └── templates/
│       ├── home.html        # Dashboard inicial com atalhos rápidos
│       ├── comum/           # 💡 Componentes universais reutilizáveis
│       │   ├── base.html
│       │   ├── listar_generico.html
│       │   ├── form_generico.html
│       │   └── confirmar_exclusao_generico.html
│       └── movimentacoes/   # Telas específicas com lógica dedicada
│
├── db.sqlite3               # Banco de dados local (SQLite)
├── manage.py                # Utilitário CLI do Django
└── README.md
```

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10+ instalado

### Passo a Passo

1. **Acessar a pasta do projeto:**
   ```bash
   cd componentizacao_teste
   ```

2. **Criar e ativar o ambiente virtual:**
   ```bash
   # Windows (PowerShell):
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instalar o Django:**
   ```bash
   pip install django
   ```

4. **Executar as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Iniciar o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

6. **Acessar no navegador:**
   Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para navegar pelo dashboard e testar as telas componentizadas.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework Web:** Django 5.x
- **Estilização / UI:** Bootstrap 5 (via CDN)
- **Banco de Dados:** SQLite
