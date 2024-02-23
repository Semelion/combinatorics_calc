import flet as ft
import re

import backend

last_valid_value = ["","","","","","","","",""]

regex = "^[0-9,]+$"
pattern = re.compile(regex)
regex_int = "^[0-9]+$"
pattern_int = re.compile(regex)

def validate_numbers(field, pagee, id): # функция для проверки текстовых полей
    global last_valid_value

    digits = field.value
    if digits == "":
        last_valid_value[id] = ""
    else:
        if(pattern.search(digits) is not None):
            last_valid_value[id] = digits
        else:
            field.value = last_valid_value[id]
            pagee.update()

def validate_int(field, pagee, id): # функция для проверки текстовых полей
    global last_valid_value

    digits = field.value
    if digits == "":
        last_valid_value[id] = ""
    else:
        if(pattern_int.search(digits) is not None):
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
        # print(input_list)
        res_1.value = "Ответ: " + str(backend.rule_of_sum(input_list))
        page.update()



    num1 = ft.TextField(label="Все количества вариантов через запятую",  on_change=lambda e: validate_numbers(num1, page, id=0), border_radius=10)
    calculate1 = ft.FilledButton("Посчитать", on_click=get_result_1)
    res_1 = ft.Text("",size=50)

    tab_sum_rule = ft.Column([num1, calculate1, res_1])

    ###TAB 2####
    def get_result_2(e):
        input_list = []
        # print(input_list)
        for i in num2.value.split(','):
            if i != '':
                input_list.append(int(i))
        # print(backend.rule_of_multiplication(input_list))
        res_2.value = "Ответ: " + str(backend.rule_of_multiplication(input_list))
        page.update()

    num2 = ft.TextField(label="Все количества вариантов через запятую",  on_change=lambda e: validate_numbers(num2, page, id=1), border_radius=10)
    calculate2 = ft.FilledButton("Посчитать", on_click=get_result_2)
    res_2 = ft.Text("",size=50)

    tab_product_rule = ft.Column([num2, calculate2, res_2])

    ###TAB 3####
    def get_result_3(e):
        res_3.value = "Ответ: " + str(backend.arrangements_with_replacement(num3_choices.value.split(','), int(num3_length.value)))
        page.update()
    num3_choices = ft.TextField(label="Все элементы через запятую", border_radius=10)
    num3_length = ft.TextField(label="Количество мест размещения",  on_change=lambda e: validate_numbers(num3_length, page, id=2), border_radius=10)
    res_3 = ft.Text("",size=50)
    calculate3 = ft.FilledButton("Посчитать", on_click=get_result_3)

    tab_placements_with_repetitions = ft.Column([num3_choices, num3_length, calculate3, res_3])


    ###TAB 4####
    def get_result_4(e):
        res_4.value = "Ответ: " + str(backend.arrangements_without_replacement(num4_choices.value.split(','), int(num4_length.value)))
        page.update()
    num4_choices = ft.TextField(label="Все элементы через запятую", border_radius=10)
    num4_length = ft.TextField(label="Количество мест размещения",  on_change=lambda e: validate_numbers(num4_length, page, id=3), border_radius=10)
    res_4 = ft.Text("",size=50)
    calculate4 = ft.FilledButton("Посчитать", on_click=get_result_4)

    tab_placements_without_repetitions = ft.Column([num4_choices, num4_length, calculate4, res_4])

    ###TAB 5####
    def get_result_5(e):
        res_5.value = "Ответ: " + str(backend.sequence_combination_generator(num5_combination.value.split(','), int(num5.value)))
        page.update()
    num5_combination = ft.TextField(label="Все элементы через запятую", border_radius=10)
    num5 = ft.TextField(label="Количество мест размещения",  on_change=lambda e: validate_numbers(num5, page, id=4), border_radius=10)
    res_5 = ft.Text("",size=50)
    calculate5 = ft.FilledButton("Посчитать", on_click=get_result_5)

    tab_combinations_with_repetitions = ft.Column([num5_combination, num5, calculate5, res_5])

    ###TAB 6####
    def get_result_6(e):
        res_6.value = "Ответ: " + str(backend.count_combinations(len(num6_combination.value.split(',')), int(num6.value)))
        page.update()
    num6_combination = ft.TextField(label="Все элементы через запятую", border_radius=10)
    num6 = ft.TextField(label="Количество мест размещения",  on_change=lambda e: validate_numbers(num6, page, id=5), border_radius=10)
    res_6 = ft.Text("",size=50)
    calculate6 = ft.FilledButton("Посчитать", on_click=get_result_6)

    tab_combinations_without_repetitions = ft.Column([num6_combination, num6, calculate6, res_6])

    ###TAB 7####
    def get_result_7(e):
        res_7.value = "Ответ: " + str(backend.count_permutations(len(num7_combination.value.split(',')), int(num7.value)))
        page.update()
    num7_combination = ft.TextField(label="Все элементы через запятую", border_radius=10)
    num7 = ft.TextField(label="Количество мест размещения",  on_change=lambda e: validate_numbers(num7, page, id=6), border_radius=10)
    res_7 = ft.Text("",size=50)
    calculate7 = ft.FilledButton("Посчитать", on_click=get_result_7)

    tab_permutations_with_repetitions = ft.Column([num7_combination, num7, calculate7, res_7])



    ###TAB 8####
    def get_result_8(e):
        res_8.value = "Ответ: " + str(backend.k_permutation_of_n(int(num8.value), num8_combination.value.split(',') ))
        page.update()
    num8_combination = ft.TextField(label="Все элементы через запятую", border_radius=10)
    num8 = ft.TextField(label="Количество мест размещения",  on_change=lambda e: validate_numbers(num8, page, id=7), border_radius=10)
    res_8 = ft.Text("",size=50)
    calculate8 = ft.FilledButton("Посчитать", on_click=get_result_8)

    tab_permutations_without_repetitions = ft.Column([num8_combination, num8, calculate8, res_8])



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
