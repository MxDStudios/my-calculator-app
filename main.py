import math
import PySimpleGUI as sg

# Функція для обчислення факторіалу числа з використанням рекурсії
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Функція для обчислення синусу числа
def calculate_sine(x):
    return math.sin(x)

def main():
    # Розміщення елементів на вікні
    layout = [
        [sg.Text("Введіть число, для якого бажаєте обчислити факторіал та синус:")],
        [sg.Text("Число:"), sg.InputText(key="input_num")],
        [sg.Button("Обчислити"), sg.Button("Вийти")],
        [sg.Text(size=(30, 2), key="output_result")]
    ]

    # Створення вікна
    window = sg.Window("Калькулятор", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вийти":
            break

        if event == "Обчислити":
            try:
                num = float(values["input_num"])
                fact_result = factorial(int(num))
                sine_result = calculate_sine(num)

                output_text = f"Факторіал числа {num} дорівнює {fact_result}\n" \
                              f"Синус числа {num} дорівнює {sine_result}"
            except ValueError:
                output_text = "Будь ласка, введіть коректне число."

            window["output_result"].update(output_text)

    window.close()

if __name__ == "__main__":
    main()