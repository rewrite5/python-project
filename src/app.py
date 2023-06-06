from rickandmorty import Rickandmorty

import flet as ft

def main(page: ft.Page):

    page.title = "Images RickAndMorty"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50
    page.update()
    etiquetas = Rickandmorty()
    images = ft.Row(expand=1, wrap=False, scroll="always")
    page.add(images)

    for imagen in etiquetas.get_images():
        images.controls.append(
            ft.Image(
                src=imagen,
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()

# ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER)