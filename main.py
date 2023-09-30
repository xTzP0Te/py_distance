import flet as ft
from playsound import playsound


def main(page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    distance = ft.Ref[ft.TextField]()

    sounds_dir = "sounds"
    # distance = int(input())
    hundred_list = ["100.mp3", "200.mp3", "300.mp3"]
    tens_list = ["10.mp3", "20.mp3", "30.mp3", "40.mp3", "50.mp3", "60.mp3", "70.mp3", "80.mp3", "90.mp3"]
    numbers_list = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3", "6.mp3", "7.mp3", "8.mp3", "9.mp3"]

    def distance_to_voice(source_distance, digit_capacity: int, target_number_list):
        # if (count := source_distance // digit_capacity) > 0 and count <= len(target_number_list):
        if digit_capacity == 100:
            count = source_distance // digit_capacity
        elif digit_capacity == 10:
            count = (source_distance // 10) % 10
        else:
            count = source_distance % 10
        if count > 0 and count <= len(target_number_list):
            playsound(sounds_dir + "/" + target_number_list[count - 1])


    def voice_souns(e):
        distance_to_voice(int(distance.current.value), 100, hundred_list)
        distance_to_voice(int(distance.current.value), 10, tens_list)
        distance_to_voice(int(distance.current.value), 1, numbers_list)

        print(type(e))
        print(e)


    page.add(
            ft.TextField(ref=distance, label="Введите дистанцию (м)", autofocus=True),
            ft.ElevatedButton("Сказать голосом", on_click=voice_souns),
        )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
# ft.app(target=main)
