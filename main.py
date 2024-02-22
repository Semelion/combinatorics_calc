import flet as ft
import re

last_valid_value = [""]

regex = "^[0-9,]+$"
pattern = re.compile(regex)

def validate_numbers(field, pagee, id): # функция для проверки текстовых полей
    global last_valid_value

    digits = field.value
    if digits == "":
        last_valid_value[id] = ""
    else:
        if(pattern.search(digits) is not None): # проверка для обычных с.с.
            last_valid_value[id] = digits
        else:
            field.value = last_valid_value[id]
            pagee.update()

def main(page: ft.Page): # функция отрисовки окна
    ####PAGE SETTINGS#####
    page.title = "Калькулятор комбинаторных схем"
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.GREEN,
            primary_container=ft.colors.GREEN_200
        ),
    )
    # page.window_width = 350
    page.window_height = 700
    # page.window_resizable = False

    ######################
    # page.update()
    # ####function##### функции
    # def close_banner(e): # реакция на кнопку ок в банере для его закрытия
    #     page.banner.open = False
    #     page.update()
    #
    #
    # def changetab(e): # функция смены вкладок
    #     # GET INDEX TAB
    #     my_index = e.control.selected_index
    #     tab_1.visible = True if my_index == 0 else False
    #     tab_2.visible = True if my_index == 1 else False
    #     page.update()
    #
    # ####visible components#### Сами визуальные компоненты
    # page.title = "Калькулятор комбинаторных схем"
    # page.theme = ft.Theme(
    #     color_scheme=ft.ColorScheme(
    #         primary=ft.colors.GREEN,
    #         primary_container=ft.colors.GREEN_200
    #     ),
    # )
    # page.window_width = 350
    # page.window_height = 500
    # page.window_resizable = False
    #
    #
    # ########## добавление компонентов на страницу приложения
    #
    # tab_1 = ft.Text("TAB 1")
    # tab_2 = ft.Text("TAB 2")
    # tab_2.visible = False
    # page.add(tab_1, tab_2)
    ####FUNCTIONS#######
    def changetab(e): # функция смены вкладок
        # GET INDEX TAB
        # print(e.control.selected_index)
        my_index = e.control.selected_index

        tab_sum_rule.visible = True if my_index == 0 else False
        tab_product_rule.visible = True if my_index == 1 else False
        tab_placements_with_repetitions.visible = True if my_index == 2 else False
        tab_placements_without_repetitions.visible = True if my_index == 3 else False
        tab_combinations_with_repetitions.visible = True if my_index == 4 else False
        tab_combinations_without_repetitions.visible = True if my_index == 5 else False
        tab_permutations_with_repetitions.visible = True if my_index == 6 else False
        tab_permutations_without_repetitions.visible = True if my_index == 7 else False
        page.update()

    ####################


    rail = ft.NavigationRail(
        indicator_color=ft.colors.GREEN,
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        # leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"sum2.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"sum2.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Правило\nсуммы",text_align=ft.TextAlign.CENTER)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"multiply.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"multiply.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Правило\nпроизведения",text_align=ft.TextAlign.CENTER)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"tab3.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"tab3.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Размещения\nс повторениями",text_align=ft.TextAlign.CENTER)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"tab4_2.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"tab4_2.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Размещение\nбез повторений",text_align=ft.TextAlign.CENTER)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"tab5.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"tab5.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Сочетания\nс повторениями",text_align=ft.TextAlign.CENTER)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"solution.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"solution.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Сочетания\nбез повторений",text_align=ft.TextAlign.CENTER)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"Rearrangements.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"Rearrangements.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Перестановки\nс повторениями",text_align=ft.TextAlign.CENTER)
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Image(src=f"shuffle.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                selected_icon_content=ft.Image(src=f"shuffle.png", width=32, height=32,fit=ft.ImageFit.CONTAIN),
                label_content=ft.Text("Перестановки\nбез повторений",text_align=ft.TextAlign.CENTER)
            )
        ],
        on_change=changetab)
    ###TAB 1####
    def get_result_1(e):
        input_list = []
        # print(input_list)
        for i in num1.value.split(','):
            if i != '':
                input_list.append(int(i))
        print(input_list)


    num1 = ft.TextField(label="Все количкства вариантов через запятую",  on_change=lambda e: validate_numbers(num1, page, id=0), border_radius=10)
    calculate1 = ft.FilledButton("Посчитать", on_click=get_result_1)
    res_1 = ft.Text("")

    tab_sum_rule = ft.Column([ft.Text("TAB 1"), num1,calculate1])

    ###
    tab_product_rule = ft.Text("TAB 2")
    tab_placements_with_repetitions = ft.Text("TAB 3")
    tab_placements_without_repetitions = ft.Text("TAB 4")
    tab_combinations_with_repetitions = ft.Text("TAB 5")
    tab_combinations_without_repetitions = ft.Text("TAB 6")
    tab_permutations_with_repetitions = ft.Text("TAB 7")
    tab_permutations_without_repetitions = ft.Text("TAB 8")

    tab_product_rule.visible = False
    tab_placements_with_repetitions.visible = False
    tab_placements_without_repetitions.visible = False
    tab_combinations_with_repetitions.visible = False
    tab_combinations_without_repetitions.visible = False
    tab_permutations_with_repetitions.visible = False
    tab_permutations_without_repetitions.visible = False


    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([tab_sum_rule, tab_product_rule, tab_placements_with_repetitions,
                    tab_placements_without_repetitions, tab_combinations_with_repetitions,
                    tab_combinations_without_repetitions, tab_permutations_with_repetitions, tab_permutations_without_repetitions],
                    alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )


ft.app(target=main,  assets_dir="icons")
