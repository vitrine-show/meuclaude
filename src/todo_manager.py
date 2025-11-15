"""Módulo principal do gerenciador de tarefas."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from enum import Enum


class TaskStatus(Enum):
    """Status possíveis para uma tarefa."""
    PENDING = "pendente"
    IN_PROGRESS = "em_progresso"
    COMPLETED = "concluída"
    CANCELLED = "cancelada"


class Task:
    """Representa uma tarefa individual."""

    def __init__(
        self,
        title: str,
        description: str = "",
        status: TaskStatus = TaskStatus.PENDING,
        task_id: Optional[int] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        tags: Optional[List[str]] = None
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status if isinstance(status, TaskStatus) else TaskStatus(status)
        self.created_at = created_at or datetime.now().isoformat()
        self.updated_at = updated_at or datetime.now().isoformat()
        self.tags = tags or []

    def to_dict(self) -> Dict:
        """Converte a tarefa para dicionário."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Cria uma tarefa a partir de um dicionário."""
        return cls(
            title=data["title"],
            description=data.get("description", ""),
            status=data.get("status", TaskStatus.PENDING.value),
            task_id=data.get("id"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
            tags=data.get("tags", [])
        )

    def update_status(self, new_status: TaskStatus):
        """Atualiza o status da tarefa."""
        self.status = new_status
        self.updated_at = datetime.now().isoformat()

    def __str__(self) -> str:
        """Representação em string da tarefa."""
        status_icon = {
            TaskStatus.PENDING: "⏳",
            TaskStatus.IN_PROGRESS: "🔄",
            TaskStatus.COMPLETED: "✅",
            TaskStatus.CANCELLED: "❌"
        }
        tags_str = f" [{', '.join(self.tags)}]" if self.tags else ""
        return f"{status_icon[self.status]} [{self.id}] {self.title}{tags_str}"


class TodoManager:
    """Gerenciador de tarefas."""

    def __init__(self, storage_path: str = "todos.json"):
        self.storage_path = Path(storage_path)
        self.tasks: List[Task] = []
        self._next_id = 1
        self.load_tasks()

    def load_tasks(self):
        """Carrega as tarefas do arquivo de armazenamento."""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
                    self._next_id = data.get("next_id", 1)
            except (json.JSONDecodeError, IOError) as e:
                print(f"⚠️  Erro ao carregar tarefas: {e}")
                self.tasks = []
                self._next_id = 1

    def save_tasks(self):
        """Salva as tarefas no arquivo de armazenamento."""
        try:
            data = {
                "tasks": [task.to_dict() for task in self.tasks],
                "next_id": self._next_id
            }
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"⚠️  Erro ao salvar tarefas: {e}")

    def add_task(self, title: str, description: str = "", tags: Optional[List[str]] = None) -> Task:
        """Adiciona uma nova tarefa."""
        task = Task(
            title=title,
            description=description,
            task_id=self._next_id,
            tags=tags or []
        )
        self.tasks.append(task)
        self._next_id += 1
        self.save_tasks()
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Obtém uma tarefa pelo ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task_status(self, task_id: int, new_status: TaskStatus) -> bool:
        """Atualiza o status de uma tarefa."""
        task = self.get_task(task_id)
        if task:
            task.update_status(new_status)
            self.save_tasks()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Remove uma tarefa."""
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False

    def list_tasks(
        self,
        status_filter: Optional[TaskStatus] = None,
        tag_filter: Optional[str] = None
    ) -> List[Task]:
        """Lista tarefas com filtros opcionais."""
        filtered_tasks = self.tasks

        if status_filter:
            filtered_tasks = [t for t in filtered_tasks if t.status == status_filter]

        if tag_filter:
            filtered_tasks = [t for t in filtered_tasks if tag_filter in t.tags]

        return filtered_tasks

    def get_statistics(self) -> Dict[str, int]:
        """Retorna estatísticas sobre as tarefas."""
        stats = {
            "total": len(self.tasks),
            "pendente": sum(1 for t in self.tasks if t.status == TaskStatus.PENDING),
            "em_progresso": sum(1 for t in self.tasks if t.status == TaskStatus.IN_PROGRESS),
            "concluída": sum(1 for t in self.tasks if t.status == TaskStatus.COMPLETED),
            "cancelada": sum(1 for t in self.tasks if t.status == TaskStatus.CANCELLED)
        }
        return stats
