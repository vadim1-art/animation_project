import math
import tkinter as tk


class FractalTreeApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Фрактальное дерево (Tkinter)")

    self.width = 800
    self.height = 600

    # Создание холста для рисования
    self.canvas = tk.Canvas(
        root, width=self.width, height=self.height, bg="white"
    )
    self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Панель управления 
    control_frame = tk.Frame(root, bg="#f0f0f0", padx=10, pady=10)
    control_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # 1. Слайдер для угла ветвления
    tk.Label(
        control_frame, text="Угол ветвления (°):", bg="#f0f0f0", font=("Arial", 10)
    ).pack(side=tk.LEFT, padx=5)
    self.angle_slider = tk.Scale(
        control_frame,
        from_=0,
        to=90,
        orient=tk.HORIZONTAL,
        command=self.update_tree,
    )
    self.angle_slider.set(25)  # Начальный угол по умолчанию
    self.angle_slider.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    # Слайдер для количества итераций
    tk.Label(
        control_frame, text="Итерации:", bg="#f0f0f0", font=("Arial", 10)
    ).pack(side=tk.LEFT, padx=5)
    self.depth_slider = tk.Scale(
        control_frame,
        from_=1,
        to=10,
        orient=tk.HORIZONTAL,
        command=self.update_tree,
    )
    self.depth_slider.set(
        8
    )  # 8 итераций оптимально для производительности в реальном времени
    self.depth_slider.pack(side=tk.LEFT, padx=5)

    # Первичная отрисовка дерева
    self.update_tree()

  def draw_branch(self, x, y, length, angle, depth):
    if depth == 0 or length < 2:
      return

    # Вычисляем координаты конца текущей ветки
    x_end = x + length * math.cos(angle)
    y_end = y + length * math.sin(angle)

    color = "#8B4513" if depth > 3 else "#228B22"
    width = max(1, depth // 2)

    # Рисуем линию ветки
    self.canvas.create_line(x, y, x_end, y_end, fill=color, width=width)

    # Получаем угол из слайдера и переводим в радианы
    branch_angle = math.radians(self.angle_slider.get())

    length_scale = 0.75

    # Рекурсивный вызов для двух дочерних ветвей (влево и вправо)
    self.draw_branch(
        x_end, y_end, length * length_scale, angle - branch_angle, depth - 1
    )
    self.draw_branch(
        x_end, y_end, length * length_scale, angle + branch_angle, depth - 1
    )

  def update_tree(self, event=None):
    self.canvas.delete("all")

    depth = self.depth_slider.get()

    start_x = self.width // 2
    start_y = self.height - 40
    initial_length = 140

    self.draw_branch(start_x, start_y, initial_length, -math.pi / 2, depth)


if __name__ == "__main__":
  root = tk.Tk()
  app = FractalTreeApp(root)
  root.mainloop()
