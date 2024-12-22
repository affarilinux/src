from flet import SnackBar, Text, FontWeight


class Menor:

    def snack_bar_floating_button(self, frase):

        from front_exe import Pagina

        Pagina.PAGE.open(SnackBar(Text(
            frase,
            color="#4F4F4F",  # Grey
            size=20,
            weight=FontWeight.W_900
        )))
