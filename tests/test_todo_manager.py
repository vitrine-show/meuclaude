"""Testes para o módulo todo_manager."""

import pytest
import tempfile
import os
from pathlib import Path
from src.todo_manager import TodoManager, Task, TaskStatus


@pytest.fixture
def temp_storage():
    """Cria um arquivo temporário para armazenamento de testes."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        temp_path = f.name
    yield temp_path
    # Cleanup
    if os.path.exists(temp_path):
        os.unlink(temp_path)


@pytest.fixture
def manager(temp_storage):
    """Cria uma instância do TodoManager para testes."""
    return TodoManager(temp_storage)


class TestTask:
    """Testes para a classe Task."""

    def test_task_creation(self):
        """Testa a criação de uma tarefa."""
        task = Task(title="Teste", description="Descrição de teste")
        assert task.title == "Teste"
        assert task.description == "Descrição de teste"
        assert task.status == TaskStatus.PENDING
        assert task.tags == []

    def test_task_with_tags(self):
        """Testa criação de tarefa com tags."""
        task = Task(title="Teste", tags=["urgente", "trabalho"])
        assert "urgente" in task.tags
        assert "trabalho" in task.tags

    def test_task_to_dict(self):
        """Testa conversão de tarefa para dicionário."""
        task = Task(title="Teste", task_id=1)
        task_dict = task.to_dict()
        assert task_dict["title"] == "Teste"
        assert task_dict["id"] == 1
        assert "status" in task_dict

    def test_task_from_dict(self):
        """Testa criação de tarefa a partir de dicionário."""
        data = {
            "id": 1,
            "title": "Teste",
            "description": "Desc",
            "status": "pendente",
            "tags": ["test"]
        }
        task = Task.from_dict(data)
        assert task.id == 1
        assert task.title == "Teste"
        assert task.tags == ["test"]

    def test_update_status(self):
        """Testa atualização de status."""
        task = Task(title="Teste")
        old_updated_at = task.updated_at
        task.update_status(TaskStatus.COMPLETED)
        assert task.status == TaskStatus.COMPLETED
        assert task.updated_at != old_updated_at


class TestTodoManager:
    """Testes para a classe TodoManager."""

    def test_manager_initialization(self, manager):
        """Testa inicialização do gerenciador."""
        assert manager.tasks == []
        assert manager._next_id == 1

    def test_add_task(self, manager):
        """Testa adição de tarefa."""
        task = manager.add_task("Minha primeira tarefa")
        assert task.title == "Minha primeira tarefa"
        assert task.id == 1
        assert len(manager.tasks) == 1

    def test_add_multiple_tasks(self, manager):
        """Testa adição de múltiplas tarefas."""
        task1 = manager.add_task("Tarefa 1")
        task2 = manager.add_task("Tarefa 2")
        assert task1.id == 1
        assert task2.id == 2
        assert len(manager.tasks) == 2

    def test_get_task(self, manager):
        """Testa obtenção de tarefa por ID."""
        manager.add_task("Tarefa teste")
        task = manager.get_task(1)
        assert task is not None
        assert task.title == "Tarefa teste"

    def test_get_nonexistent_task(self, manager):
        """Testa obtenção de tarefa inexistente."""
        task = manager.get_task(999)
        assert task is None

    def test_update_task_status(self, manager):
        """Testa atualização de status de tarefa."""
        manager.add_task("Tarefa teste")
        result = manager.update_task_status(1, TaskStatus.COMPLETED)
        assert result is True
        task = manager.get_task(1)
        assert task.status == TaskStatus.COMPLETED

    def test_update_nonexistent_task_status(self, manager):
        """Testa atualização de status de tarefa inexistente."""
        result = manager.update_task_status(999, TaskStatus.COMPLETED)
        assert result is False

    def test_delete_task(self, manager):
        """Testa remoção de tarefa."""
        manager.add_task("Tarefa teste")
        assert len(manager.tasks) == 1
        result = manager.delete_task(1)
        assert result is True
        assert len(manager.tasks) == 0

    def test_delete_nonexistent_task(self, manager):
        """Testa remoção de tarefa inexistente."""
        result = manager.delete_task(999)
        assert result is False

    def test_list_all_tasks(self, manager):
        """Testa listagem de todas as tarefas."""
        manager.add_task("Tarefa 1")
        manager.add_task("Tarefa 2")
        manager.add_task("Tarefa 3")
        tasks = manager.list_tasks()
        assert len(tasks) == 3

    def test_list_tasks_by_status(self, manager):
        """Testa filtragem de tarefas por status."""
        manager.add_task("Tarefa 1")
        manager.add_task("Tarefa 2")
        manager.update_task_status(1, TaskStatus.COMPLETED)

        pending_tasks = manager.list_tasks(status_filter=TaskStatus.PENDING)
        completed_tasks = manager.list_tasks(status_filter=TaskStatus.COMPLETED)

        assert len(pending_tasks) == 1
        assert len(completed_tasks) == 1

    def test_list_tasks_by_tag(self, manager):
        """Testa filtragem de tarefas por tag."""
        manager.add_task("Tarefa 1", tags=["urgente"])
        manager.add_task("Tarefa 2", tags=["normal"])
        manager.add_task("Tarefa 3", tags=["urgente", "trabalho"])

        urgent_tasks = manager.list_tasks(tag_filter="urgente")
        assert len(urgent_tasks) == 2

    def test_get_statistics(self, manager):
        """Testa obtenção de estatísticas."""
        manager.add_task("Tarefa 1")
        manager.add_task("Tarefa 2")
        manager.add_task("Tarefa 3")
        manager.update_task_status(1, TaskStatus.COMPLETED)
        manager.update_task_status(2, TaskStatus.IN_PROGRESS)

        stats = manager.get_statistics()
        assert stats["total"] == 3
        assert stats["pendente"] == 1
        assert stats["em_progresso"] == 1
        assert stats["concluída"] == 1

    def test_persistence(self, temp_storage):
        """Testa persistência de dados."""
        # Criar gerenciador e adicionar tarefas
        manager1 = TodoManager(temp_storage)
        manager1.add_task("Tarefa persistente")

        # Criar novo gerenciador com mesmo storage
        manager2 = TodoManager(temp_storage)
        assert len(manager2.tasks) == 1
        assert manager2.tasks[0].title == "Tarefa persistente"

    def test_add_task_with_description_and_tags(self, manager):
        """Testa adição de tarefa com descrição e tags."""
        task = manager.add_task(
            "Tarefa completa",
            description="Uma descrição detalhada",
            tags=["importante", "urgente"]
        )
        assert task.description == "Uma descrição detalhada"
        assert len(task.tags) == 2
        assert "importante" in task.tags
