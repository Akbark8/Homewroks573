import flet as ft

MAX_LENGTH = 100

def main(page: ft.Page):
    page.title = "Ограничение ввода"

    info_text = ft.Text("Введите текст (до 100 символов):")
    text_field = ft.TextField(width=400)

    def on_change(e: ft.ControlEvent):
        if len(text_field.value) > MAX_LENGTH:
            text_field.value = text_field.value[:MAX_LENGTH]
            page.snack_bar = ft.SnackBar(ft.Text(f"Вы ввели больше {MAX_LENGTH} символов!"))
            page.snack_bar.open = True
            page.update()

    text_field.on_change = on_change

    page.add(
        info_text,
        text_field
    )

ft.app(target=main)
