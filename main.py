import flet as ft


def main(page):

    title = ft.Text("ChatZap")

    def msg_tunel(message):
        text = ft.Text(message)
        chat.controls.append(text)

        page.update()

    page.pubsub.subscribe(msg_tunel)

    def send_message(event):

        name_user = box_chat.value
        text_dig = box_message.value

        message = f"{name_user}: {text_dig}"
        page.pubsub.send_all(message)

        box_message.value = ""
        page.update()

    box_message = ft.TextField(
        label="Digite sua mensagem aqui...", on_submit=send_message)

    button_send = ft.ElevatedButton(
        "Enviar", on_click=send_message)

    chat = ft.Column([])
    row_send = ft.Row([box_message, button_send])

    def on_chat(evento):
        popup.open = False
        page.remove(title)
        page.remove(button_init)

        page.add(chat)
        page.add(row_send)

        box_name = box_chat.value
        message = f"{box_name} entro no chat!"
        page.pubsub.send_all(message)
        page.update()

    title_popup = ft.Text("Bem Vindo ao ChatZap.")
    box_chat = ft.TextField(label="Digite seu nome.", on_submit=on_chat)
    button_popup = ft.ElevatedButton(
        "Entra no Chat", on_click=on_chat)

    popup = ft.AlertDialog(
        title=title_popup, content=box_chat, actions=[button_popup])

    def open_popup(event):
        page.dialog = popup
        popup.open = True
        page.update()

    button_init = ft.ElevatedButton(
        "Iniciar Chat", on_click=open_popup)

    page.add(title)
    page.add(button_init)


ft.app(target=main, view="web_browser")
