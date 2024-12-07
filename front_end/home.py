from flet import (AppBar, Text, Tabs, Tab, IconButton,
                  icons, Icons, Container, Icon, alignment)


class Home:

    def home_criar_appbar(self):
        from front_exe import Pagina

        def ativar_drawer(e):

            Pagina.PAGE.drawer.open = True
            Pagina.PAGE.update()
        
        Pagina.PAGE.appbar = AppBar(
            leading=IconButton(
                icons.ARROW_CIRCLE_RIGHT_SHARP,
                on_click=ativar_drawer,  # Adicione o callback aqui
                icon_color="#FFFF00"  # Yellow
            ),
            leading_width=40,
            title=Text(
                "HOME",
                color="#FFFF00"  # Yellow
            ),
            center_title=True,
            bgcolor="#4F4F4F"  # grey31
        )

    def home_criar_tabs(self):
        from front_exe import Pagina

        self.tabs = Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                Tab(
                    text="Tab 1",
                    content=Container(
                        content=Text("This is Tab 1"),
                        alignment=alignment.center,
                    ),
                ),
                Tab(
                    tab_content=Icon(Icons.SEARCH),
                    content=Text("This is Tab 2"),
                ),
                Tab(
                    text="Tab 3",
                    icon=Icons.SETTINGS,
                    content=Text("This is Tab 3"),
                ),
            ],
            expand=1,
        )

        Pagina.PAGE.add(self.tabs)

    def criar_pagina(self):
        self.home_criar_appbar()
        self.home_criar_tabs()

        from front_exe import Pagina
        Pagina.PAGE.update()

    def remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.appbar = None  # Remove AppBar

        if hasattr(self, 'tabs') and self.tabs in Pagina.PAGE.controls:
            Pagina.PAGE.controls.remove(self.tabs)

        Pagina.PAGE.update()
