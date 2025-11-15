# 🚀 meuclaude

> Um gerenciador de tarefas CLI inteligente, escrito em Python

**meuclaude** (português para "my Claude") é um gerenciador de tarefas via linha de comando, simples, rápido e eficiente. Perfeito para desenvolvedores que vivem no terminal!

## ✨ Funcionalidades

- ✅ Adicionar, listar, atualizar e remover tarefas
- 🏷️ Organizar tarefas com tags
- 📊 Visualizar estatísticas das suas tarefas
- 🎨 Interface colorida e amigável
- 💾 Persistência automática em JSON
- 🔍 Filtrar tarefas por status ou tags
- 🧪 Totalmente testado com pytest

## 📋 Requisitos

- Python >= 3.8
- pip

## 🛠️ Instalação

### Instalação para Desenvolvimento

```bash
# Clone o repositório
git clone http://local_proxy@127.0.0.1:34416/git/vitrine-show/meuclaude
cd meuclaude

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Instale em modo desenvolvimento
pip install -e .
```

### Instalação Rápida (Usuário)

```bash
pip install -e .
```

## 🎯 Uso

### Comandos Disponíveis

#### Adicionar uma tarefa

```bash
# Tarefa simples
meuclaude add "Estudar Python"

# Tarefa com descrição
meuclaude add "Implementar API" --desc "Criar endpoints REST"

# Tarefa com tags
meuclaude add "Revisar PR" -t urgente -t trabalho
```

#### Listar tarefas

```bash
# Listar todas
meuclaude list

# Filtrar por status
meuclaude list --status pendente
meuclaude list --status concluída

# Filtrar por tag
meuclaude list --tag urgente
```

#### Ver detalhes de uma tarefa

```bash
meuclaude show 1
```

#### Atualizar status

```bash
# Atualizar manualmente
meuclaude update 1 em_progresso
meuclaude update 1 concluída

# Atalho para marcar como concluída
meuclaude complete 1
```

#### Remover tarefa

```bash
meuclaude delete 1
```

#### Ver estatísticas

```bash
meuclaude stats
```

#### Limpar tarefas concluídas

```bash
meuclaude clear
```

#### Ajuda

```bash
meuclaude --help
meuclaude add --help  # Ajuda específica de um comando
```

## 📖 Exemplos de Uso

```bash
# Fluxo completo de trabalho
$ meuclaude add "Criar testes unitários" -t desenvolvimento -t testes
✅ Tarefa adicionada: ⏳ [1] Criar testes unitários [desenvolvimento, testes]

$ meuclaude add "Documentar API" --desc "Adicionar docstrings em todas as funções"
✅ Tarefa adicionada: ⏳ [2] Documentar API

$ meuclaude list

📋 Tarefas (2):

  ⏳ [1] Criar testes unitários [desenvolvimento, testes]
  ⏳ [2] Documentar API
     💬 Adicionar docstrings em todas as funções

$ meuclaude update 1 em_progresso
✅ Status atualizado: 🔄 [1] Criar testes unitários [desenvolvimento, testes]

$ meuclaude complete 1
🎉 Tarefa concluída: ✅ [1] Criar testes unitários [desenvolvimento, testes]

$ meuclaude stats

📊 Estatísticas:

   Total de tarefas: 2
   ⏳ Pendentes: 1
   🔄 Em progresso: 0
   ✅ Concluídas: 1
   ❌ Canceladas: 0
```

## 🧪 Executando Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=src --cov-report=html

# Executar testes específicos
pytest tests/test_todo_manager.py

# Ver relatório de cobertura no navegador
open htmlcov/index.html
```

## 📁 Estrutura do Projeto

```
meuclaude/
├── src/                      # Código fonte
│   ├── __init__.py
│   ├── todo_manager.py       # Lógica principal do gerenciador
│   └── cli.py                # Interface de linha de comando
├── tests/                    # Testes unitários
│   ├── __init__.py
│   └── test_todo_manager.py
├── docs/                     # Documentação adicional
├── .gitignore
├── CLAUDE.md                 # Guia para assistentes de IA
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências
└── pyproject.toml           # Configuração do projeto
```

## 🏗️ Arquitetura

### Componentes Principais

1. **Task**: Classe que representa uma tarefa individual
   - Armazena: título, descrição, status, tags, timestamps
   - Métodos: conversão para/de dict, atualização de status

2. **TaskStatus**: Enum com os status possíveis
   - `PENDING` (pendente)
   - `IN_PROGRESS` (em_progresso)
   - `COMPLETED` (concluída)
   - `CANCELLED` (cancelada)

3. **TodoManager**: Gerenciador central de tarefas
   - CRUD completo de tarefas
   - Persistência em JSON
   - Filtragem e estatísticas

4. **CLI**: Interface de linha de comando usando Click
   - Comandos intuitivos
   - Validação de entrada
   - Feedback visual com emojis

## 🔧 Desenvolvimento

### Adicionando Novos Recursos

1. Implemente a funcionalidade em `src/todo_manager.py`
2. Adicione testes em `tests/test_todo_manager.py`
3. Crie o comando CLI em `src/cli.py`
4. Atualize a documentação

### Convenções de Código

- Siga PEP 8
- Use type hints
- Docstrings em todos os métodos públicos
- Mantenha cobertura de testes > 80%

### Commits

Use conventional commits:

```bash
git commit -m "feat: adicionar suporte para prioridades"
git commit -m "fix: corrigir bug ao deletar tarefa"
git commit -m "docs: atualizar README com exemplos"
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'feat: adicionar MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🙏 Agradecimentos

Criado como exemplo de boas práticas de desenvolvimento Python para demonstrar:
- Estrutura de projeto organizada
- Testes automatizados
- Interface CLI profissional
- Documentação completa
- Integração com assistentes de IA (via CLAUDE.md)

## 📞 Contato

Para dúvidas, sugestões ou feedback, abra uma issue no repositório!

---

**Feito com ❤️ usando Python e Click**
