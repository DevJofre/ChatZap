import flet as ft


def main(page):

    title = ft.Text("ChatZap")
    button_init = ft.ElevatedButton("Iniciar Chat")

    send_message = ft.TextField(label="Digite sua mensagem aqui...")
    button_send = ft.ElevatedButton("Enviar")

    def on_chat(evento):
        popup.open = False
        page.remove(title)
        page.remove(button_init)

        page.add(send_message)
        page.add(button_send)

        page.update()

    title_popup = ft.Text("Bem Vindo ao ChatZap.")
    box_chat = ft.TextField(label="Digite seu nome.")
    button_popup = ft.ElevatedButton("Entra no Chat", on_click=on_chat)

    popup = ft.AlertDialog(
        title=title_popup, content=box_chat, actions=[button_popup])

    def open_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    button_init.on_click = open_popup

    page.add(title)
    page.add(button_init)


ft.app(main)
