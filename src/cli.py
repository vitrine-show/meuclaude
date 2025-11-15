"""Interface de linha de comando para o meuclaude."""

import click
from pathlib import Path
from .todo_manager import TodoManager, TaskStatus


def get_manager() -> TodoManager:
    """Retorna uma instância do gerenciador de tarefas."""
    storage_path = Path.home() / ".meuclaude" / "todos.json"
    storage_path.parent.mkdir(parents=True, exist_ok=True)
    return TodoManager(str(storage_path))


@click.group()
@click.version_option(version="0.1.0")
def main():
    """
    🚀 meuclaude - Um gerenciador de tarefas CLI inteligente

    Gerencie suas tarefas diretamente do terminal!
    """
    pass


@main.command()
@click.argument('title')
@click.option('--desc', '-d', default="", help='Descrição da tarefa')
@click.option('--tags', '-t', multiple=True, help='Tags para a tarefa')
def add(title: str, desc: str, tags: tuple):
    """Adiciona uma nova tarefa."""
    manager = get_manager()
    task = manager.add_task(title, desc, list(tags))
    click.echo(f"✅ Tarefa adicionada: {task}")


@main.command()
@click.option('--status', '-s', type=click.Choice(['pendente', 'em_progresso', 'concluída', 'cancelada']),
              help='Filtrar por status')
@click.option('--tag', '-t', help='Filtrar por tag')
def list(status: str, tag: str):
    """Lista todas as tarefas."""
    manager = get_manager()

    status_filter = None
    if status:
        status_filter = TaskStatus(status)

    tasks = manager.list_tasks(status_filter=status_filter, tag_filter=tag)

    if not tasks:
        click.echo("📭 Nenhuma tarefa encontrada.")
        return

    click.echo(f"\n📋 Tarefas ({len(tasks)}):\n")
    for task in tasks:
        click.echo(f"  {task}")
        if task.description:
            click.echo(f"     💬 {task.description}")
    click.echo()


@main.command()
@click.argument('task_id', type=int)
def show(task_id: int):
    """Mostra detalhes de uma tarefa específica."""
    manager = get_manager()
    task = manager.get_task(task_id)

    if not task:
        click.echo(f"❌ Tarefa #{task_id} não encontrada.")
        return

    click.echo(f"\n📌 Tarefa #{task.id}")
    click.echo(f"   Título: {task.title}")
    click.echo(f"   Status: {task.status.value}")
    click.echo(f"   Criada em: {task.created_at}")
    click.echo(f"   Atualizada em: {task.updated_at}")
    if task.description:
        click.echo(f"   Descrição: {task.description}")
    if task.tags:
        click.echo(f"   Tags: {', '.join(task.tags)}")
    click.echo()


@main.command()
@click.argument('task_id', type=int)
@click.argument('status', type=click.Choice(['pendente', 'em_progresso', 'concluída', 'cancelada']))
def update(task_id: int, status: str):
    """Atualiza o status de uma tarefa."""
    manager = get_manager()
    new_status = TaskStatus(status)

    if manager.update_task_status(task_id, new_status):
        task = manager.get_task(task_id)
        click.echo(f"✅ Status atualizado: {task}")
    else:
        click.echo(f"❌ Tarefa #{task_id} não encontrada.")


@main.command()
@click.argument('task_id', type=int)
def complete(task_id: int):
    """Marca uma tarefa como concluída."""
    manager = get_manager()

    if manager.update_task_status(task_id, TaskStatus.COMPLETED):
        task = manager.get_task(task_id)
        click.echo(f"🎉 Tarefa concluída: {task}")
    else:
        click.echo(f"❌ Tarefa #{task_id} não encontrada.")


@main.command()
@click.argument('task_id', type=int)
@click.confirmation_option(prompt='Tem certeza que deseja deletar esta tarefa?')
def delete(task_id: int):
    """Remove uma tarefa."""
    manager = get_manager()

    if manager.delete_task(task_id):
        click.echo(f"🗑️  Tarefa #{task_id} removida.")
    else:
        click.echo(f"❌ Tarefa #{task_id} não encontrada.")


@main.command()
def stats():
    """Mostra estatísticas das tarefas."""
    manager = get_manager()
    statistics = manager.get_statistics()

    click.echo("\n📊 Estatísticas:\n")
    click.echo(f"   Total de tarefas: {statistics['total']}")
    click.echo(f"   ⏳ Pendentes: {statistics['pendente']}")
    click.echo(f"   🔄 Em progresso: {statistics['em_progresso']}")
    click.echo(f"   ✅ Concluídas: {statistics['concluída']}")
    click.echo(f"   ❌ Canceladas: {statistics['cancelada']}")
    click.echo()


@main.command()
def clear():
    """Limpa todas as tarefas concluídas."""
    manager = get_manager()
    completed_tasks = [t for t in manager.tasks if t.status == TaskStatus.COMPLETED]

    if not completed_tasks:
        click.echo("📭 Nenhuma tarefa concluída para limpar.")
        return

    if click.confirm(f'🗑️  Remover {len(completed_tasks)} tarefa(s) concluída(s)?'):
        for task in completed_tasks:
            manager.delete_task(task.id)
        click.echo(f"✅ {len(completed_tasks)} tarefa(s) removida(s).")


if __name__ == '__main__':
    main()
