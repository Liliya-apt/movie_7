import tkinter as tk
import random
git_hub="https://github.com/Liliya-apt/movie_7"
facts=[
    "Бананы радиотивны и излучают небольшое количество гамма-излучения.",
    "Человек может обойтись без пищи до 2 месяцев, а без воды - все несколько дней.",
    "Голубые киты ежедневно потребляют около 4 тонн пищи.",
    "Пчелы могут распознавать лица людей.",
    "Cуществует 6000 видов бананов, а не только один."
   
]
def snow_fact():
    # Функция для выбора случайного факта и обновления текста в метке
    random_fact=random.choice(facts)
    # Обновляем  текст в метке(label)
    label_fact.config(text=random_fact)
# Создание главного окна
root=tk.Tk()
root.title("Интересные факты")
root.geometry("500x300")

# Настройка внешнего вида
label_fact=tk.Label(
    root,
    text="Нажмите на кнопку, чтобы узнать интересный факт!",
    wraplength=400,justify="center", font=("Arial",12),
    pady=20 )
label_fact.pack(expand=True)
button_snow=tk.Button(
    root,
    text="Показать факт", command=snow_fact, font=("Arial",10,"bold"  ),
    bg="#4CAF50",fg="white", padx=20,pady=10
)
button_snow.pack(pady=30)
root.mainloop()