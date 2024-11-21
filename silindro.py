import cv2
import numpy as np


class Figure:
    def __init__(self, name):
        self.name = name

    def draw(self, img, T, H, scale=50):
        # Dependiendo de la figura, se dibuja y se actualizan T y H
        if self.name == 'b':
            return self.draw_arc_down(img, T, H, scale)
        elif self.name == 't':
            return self.draw_arc_up(img, T, H, scale)
        elif self.name == 'u':
            return self.draw_vertical_line(img, T, H, scale)
        elif self.name == 'o':
            return self.draw_horizontal_line(img, T, H, scale)
        elif self.name == 's1':
            return self.draw_diagonal_line_up_left_to_right(img, T, H, scale)
        elif self.name == 's2':
            return self.draw_diagonal_line_up_right_to_left(img, T, H, scale)
        elif self.name == '-t':
            return self.draw_arc_down_reverse(img, T, H, scale)
        elif self.name == '-b':
            return self.draw_arc_up_reverse(img, T, H, scale)
        elif self.name == '-u':
            return self.draw_vertical_line_reverse(img, T, H, scale)
        elif self.name == '-o':
            return self.draw_horizontal_line_reverse(img, T, H, scale)
        elif self.name == '-s1':
            return self.draw_diagonal_line_up_left_to_right_reverse(img, T, H, scale)
        elif self.name == '-s2':
            return self.draw_diagonal_line_up_right_to_left_reverse(img, T, H, scale)

    def draw_arc_down(self, img, T, H, scale):
        center = (T[0] + scale, T[1])
        axes = (scale, scale // 2)
        cv2.ellipse(img, center, axes, 0, 0, 180, (255, 255, 255), 2)
        H = (T[0] + 2 * scale, T[1])
        return T, H

    def draw_arc_up(self, img, T, H, scale):
        center = (T[0] + scale, T[1])
        axes = (scale, scale // 2)
        cv2.ellipse(img, center, axes, 0, 180, 360, (255, 255, 255), 2)
        H = (T[0] + 2 * scale, T[1])
        return T, H

    def draw_horizontal_line(self, img, T, H, scale):
        H = (T[0] + 2 * scale, T[1])
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H

    def draw_vertical_line(self, img, T, H, scale):
        H = (T[0], T[1] - 2 * scale)
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H

    def draw_diagonal_line_up_left_to_right(self, img, T, H, scale):
        # Línea diagonal de izquierda a derecha con ángulo de 45 grados
        H = (T[0] + scale, T[1] - scale)
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H

    def draw_diagonal_line_up_right_to_left(self, img, T, H, scale):
        # Línea diagonal de derecha a izquierda con ángulo de 45 grados
        H = (T[0] - scale, T[1] - scale)
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H

    def draw_arc_down_reverse(self, img, T, H, scale):
        center = (T[0] + scale, T[1])
        axes = (scale, scale // 2)
        cv2.ellipse(img, center, axes, 0, 180, 360, (255, 255, 255), 2)
        H = (T[0] + 2 * scale, T[1])
        return T, H

    def draw_arc_up_reverse(self, img, T, H, scale):
        center = (T[0] + scale, T[1])
        axes = (scale, scale // 2)
        cv2.ellipse(img, center, axes, 0, 0, 180, (255, 255, 255), 2)
        H = (T[0] + 2 * scale, T[1])
        return T, H

    def draw_vertical_line_reverse(self, img, T, H, scale):
        H = (T[0], T[1] + 2 * scale)
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H

    def draw_horizontal_line_reverse(self, img, T, H, scale):
        H = (T[0] - 2 * scale, T[1])
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H

    def draw_diagonal_line_up_left_to_right_reverse(self, img, T, H, scale):
        # Línea diagonal invertida de izquierda a derecha con ángulo de 45 grados
        H = (T[0] - scale, T[1] + scale)
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H

    def draw_diagonal_line_up_right_to_left_reverse(self, img, T, H, scale):
        # Línea diagonal invertida de derecha a izquierda con ángulo de 45 grados
        H = (T[0] + scale, T[1] + scale)
        cv2.line(img, T, H, (255, 255, 255), 2)
        return T, H


def parse_input(input_str):
    tokens = input_str.split()
    img = np.zeros((600, 1000, 3), dtype=np.uint8)
    T = (50, 300)  # Posición inicial de T
    H = None  # H será actualizado con cada figura
    scale = 50

    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Verificamos si es un operador (+ o *)
        if token == "+" or token == "*":
            operator = token
            i += 1
            token = tokens[i]
        else:
            operator = None

        if token in shapes:  # Si es una figura válida
            if operator is None:  # Si no hay operador, se usa T
                if H is None:
                    T, H = Figure(token).draw(img, T, T, scale)
                else:
                    T, H = Figure(token).draw(img, T, H, scale)
            elif operator == "*":  # Si el operador es +, usar T
                T, H = Figure(token).draw(img, T, H, scale)
            elif operator == "+":  # Si el operador es *, usar H
                T, H = Figure(token).draw(img, H, H, scale)
        else:
            print(f"Advertencia: Token desconocido '{token}'. Ignorando...")

        i += 1

    cv2.imshow("Figura", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Lista de figuras primitivas
shapes = ['t', 'b', 'u', 'o', 's1', 's2', '-t', '-b', '-u', '-o', '-s1', '-s2']

# Solicitar secuencia de entrada al usuario
user_input = input("Ingrese la secuencia de figuras y operaciones (por ejemplo, 't * b + o'): ")
parse_input(user_input)
