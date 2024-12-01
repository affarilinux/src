from flet import (NavigationDrawer, NavigationDrawerDestination, Container, Icons,
                  Icon, Divider)


class NavegationDrawer:

    def criar_drawer(self):

        from front_exe import Pagina

        Pagina.PAGE.drawer = NavigationDrawer(

            controls=[
                Container(height=12),
                NavigationDrawerDestination(
                    label="Item 1",
                    icon=Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=Icon(Icons.DOOR_BACK_DOOR),
                ),
                Divider(thickness=2),
                NavigationDrawerDestination(
                    icon=Icon(Icons.MAIL_OUTLINED),
                    label="Item 2",
                    selected_icon=Icons.MAIL,
                ),
                NavigationDrawerDestination(
                    icon=Icon(Icons.PHONE_OUTLINED),
                    label="Item 3",
                    selected_icon=Icons.PHONE,
                ),
            ],
        )

        Pagina.PAGE.drawer.open = False
