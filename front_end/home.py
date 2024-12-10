from flet import (Text, Tabs, Tab, Icons, Container, Icon, alignment)


class Home:

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

    def home_criar_pagina(self):

        self.home_criar_tabs()

        from front_exe import Pagina

        Pagina.PAGE.update()

    def home_remover_pagina(self):

        from front_exe import Pagina

        if hasattr(self, 'tabs') and self.tabs in Pagina.PAGE.controls:
            Pagina.PAGE.controls.remove(self.tabs)

        Pagina.PAGE.update()
