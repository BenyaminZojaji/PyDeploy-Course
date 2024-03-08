import flet as ft
from api import Weather_api


def main(page: ft.Page):
    page.title = 'Weather Forecast'
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.update()
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def get_weather(e):
        weather = Weather_api(search_text.value)

        mode = weather.get_weather()['desc']
        img = ft.Image(
            src=f"{mode}.gif",
            width=100,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        )
        today_text = ft.Text()
        today_text.value = f"Today\nTemperature: {weather.get_weather()['temp']}\nWind: {weather.get_weather()['wind']}"

        day1forecast_text = ft.Text()
        day1forecast_text.value = f"Tomorrow\nTemperature: {weather.get_day1forecast()['temperature']}\nWind: {weather.get_day1forecast()['wind']}"

        day2forecast_text = ft.Text()
        day2forecast_text.value = f"The day after tomorrow\nTemperature: {weather.get_day2forecast()['temperature']}\nWind: {weather.get_day2forecast()['wind']}"

        day3forecast_text = ft.Text()
        day3forecast_text.value = f"Two days later\nTemperature: {weather.get_day3forecast()['temperature']}\nWind: {weather.get_day3forecast()['wind']}"

        tasks_view = ft.Column()
        view=ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        img,
                        today_text
                    ],
                ),
                ft.Row(
                    controls=[
                        day1forecast_text,
                        day2forecast_text,
                        day3forecast_text,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=95,
                ),
                tasks_view,
            ],
        )
        page.add(view)
        page.update()

    search_text = ft.TextField(label="City:", hint_text="ex: Sydney", expand=True)
    tasks_view = ft.Column()
    main_view=ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    search_text,
                    ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=get_weather),
                ],
            ),
            
            tasks_view,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(main_view)
    page.update()


ft.app(main)
