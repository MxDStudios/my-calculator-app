import math
import PySimpleGUI as sg

class Calculator:
    def __init__(self, num):
        self.num = num

    def calculate(self):
        return {
            'factorial': math.factorial(self.num),
            'sine': math.sin(self.num)
        }

class GUI:
    def __init__(self):
        sg.theme("DarkGrey1")

        button_style = {'font': ('Helvetica', 14), 'size': (15, 2), 'button_color': ('#f0f0f0', '#555555'), 'border_width': 5, 'focus': True}
        input_style = {'font': ('Helvetica', 14), 'background_color': '#333333', 'text_color': '#ffffff'}

        self.layout = [
            [sg.Text("Введіть число, для якого бажаєте обчислити факторіал та синус:", font=('Helvetica', 14), text_color='#ffffff')],
            [sg.InputText(key="input_num", **input_style)],
            [sg.Button("Обчислити", **button_style), sg.Button("Вийти", **button_style)],
            [sg.Text(size=(30, 2), key="output_result", font=('Helvetica', 14), text_color='#ffffff')]
        ]

        self.window = sg.Window("Калькулятор", self.layout, element_justification='c')

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == "Вийти":
                break

            if event == "Обчислити":
                try:
                    num = float(values["input_num"])
                    calculator = Calculator(num)
                    results = calculator.calculate()

                    output_text = f"Факторіал числа {num} дорівнює {results['factorial']}\n" \
                                  f"Синус числа {num} дорівнює {results['sine']}"
                except ValueError:
                    output_text = "Будь ласка, введіть коректне число."

                self.window["output_result"].update(output_text)

        self.window.close()

if __name__ == "__main__":
    gui = GUI()
    gui.run()