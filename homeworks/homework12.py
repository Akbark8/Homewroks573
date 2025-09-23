import flet as ft

def main(page: ft.Page):
    page.title = "Список задач"

    task_input = ft.TextField(label="Новая задача", width=300)

    def add_task(e):
        if task_input.value.strip():
            add_task_row(task_input.value)
            task_input.value = ""
            page.update()

    def add_task_row(task_text):
        task_label = ft.Text(task_text)

        edit_button = ft.ElevatedButton("Редактировать", icon=ft.Icons.EDIT)
        save_button = ft.ElevatedButton("Сохранить", icon=ft.Icons.SAVE)

        def delete_task(e):
            page.controls.remove(task_row)
            page.update()

        delete_button = ft.ElevatedButton(
            "Удалить",
            icon=ft.Icons.DELETE,
            bgcolor=ft.Colors.RED,
            color=ft.Colors.WHITE,
            on_click=delete_task
        )

        task_row = ft.Row(
            controls=[task_label, edit_button, save_button, delete_button],
            spacing=10
        )
        page.controls.append(task_row)

    add_button = ft.ElevatedButton("Добавить задачу", on_click=add_task)

    page.add(ft.Row([task_input, add_button]))

ft.app(target=main)
