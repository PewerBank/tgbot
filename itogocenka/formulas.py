
FORMULAS = {
    "potok_1": {
        "name": "1 поток",
        "items": {
            "Матэкан": "Итог = 0.3 * Накоп + 0.3 * КР + 0.4 * Экзамен",
            "Алгоритмы": "Итог = 0.4 * ДЗ + 0.2 * Колл + 0.4 * Экзамен"
        }
    },
    "potok_2": {
        "name": "2 поток",
        "items": {
            "Язык Python": "Итог = 0.5 * Проекты + 0.5 * Экзамен",
            "Дискретная математика": "Итог = 0.3 * КР1 + 0.3 * КР2 + 0.4 * Экз"
        }
    },
    "potok_3": {
        "name": "3 поток",
        "items": {
            "Базы данных": "Итог = 0.6 * Лабы + 0.4 * Экзамен"
        }
    },
    "potok_4": {
        "name": "4 поток",
        "items": {
            "Введение в ТП": "Итог = 0.7 * Накоп + 0.3 * Защита"
        }
    }
}


# Изолированный калькулятор, который считает оценки в зависимости от потока и предмета
def calculate_grade(potok_id: str, subj_name: str, scores: list[float]) -> dict:
    exam = scores[-1]       # Последняя оценка — всегда экзамен
    kr2 = scores[-2]  # Предпоследняя — КР2
    kr1 = scores[-3]
    
    if len(scores)>3:
        nakop_list = scores[:-2]
        nakop_avg = sum(nakop_list) / len(nakop_list) if nakop_list else 0.0

    final_score = 0.0
    details = {}

    # Вычисления по конкретным потокам и предметам
    if potok_id == "potok_1":
        if subj_name == "Мат. анализ":
            if len(scores) == 3:
                exam = scores[-1]       # Последняя оценка — всегда экзамен
                kr2 = scores[-2]  # Предпоследняя — КР2
                kr1 = scores[-3]
                final_score = (0.3 * kr1) + (0.3 * kr2) + (0.4 * exam)
                details = {"КР1": kr1, "КР2": kr2, "Экзамен": exam}
            
        elif subj_name == "Линейная алгебра и аналитическая геометрия":
            final_score = (0.4 * nakop_avg) + (0.2 * kr_or_kp2) + (0.4 * exam)
            details = {"ДЗ (ср. накоп)": nakop_avg, "Коллоквиум": kr_or_kp2, "Экзамен": exam}

        elif subj_name == "Дискретная математика":   
            final_score = (0.4 * nakop_avg) + (0.2 * kr_or_kp2) + (0.4 * exam)
            details = {"ДЗ (ср. накоп)": nakop_avg, "Коллоквиум": kr_or_kp2, "Экзамен": exam}

        elif subj_name == "Программирование C/C++":   
            final_score = (0.4 * nakop_avg) + (0.2 * kr_or_kp2) + (0.4 * exam)
            details = {"ДЗ (ср. накоп)": nakop_avg, "Коллоквиум": kr_or_kp2, "Экзамен": exam}

        elif subj_name == "Технологии Программирования":   
            final_score = (0.4 * nakop_avg) + (0.2 * kr_or_kp2) + (0.4 * exam)
            details = {"ДЗ (ср. накоп)": nakop_avg, "Коллоквиум": kr_or_kp2, "Экзамен": exam}
            
        elif subj_name == "Программирование C/C++":   
            final_score = (0.4 * nakop_avg) + (0.2 * kr_or_kp2) + (0.4 * exam)
            details = {"ДЗ (ср. накоп)": nakop_avg, "Коллоквиум": kr_or_kp2, "Экзамен": exam}

    elif potok_id == "potok_2":
        if subj_name == "Язык Python":
            # Итог = 0.5 * Проекты + 0.5 * Экзамен. Проекты — это всё до экзамена.
            projects_avg = sum(scores[:-1]) / len(scores[:-1]) if scores[:-1] else 0.0
            final_score = (0.5 * projects_avg) + (0.5 * exam)
            details = {"Проекты (ср.)": projects_avg, "Экзамен": exam}
            
        elif subj_name == "Дискретная математика":
            # Итог = 0.3 * KP1 + 0.3 * KP2 + 0.4 * Экз
            kp1 = scores[-3] if len(scores) >= 3 else 0.0
            final_score = (0.3 * kp1) + (0.3 * kr_or_kp2) + (0.4 * exam)
            details = {"КР 1": kp1, "КР 2": kr_or_kp2, "Экзамен": exam}

    elif potok_id == "potok_3":
        if subj_name == "Базы данных":
            # Итог = 0.6 * Лабы + 0.4 * Экзамен
            labs_avg = sum(scores[:-1]) / len(scores[:-1]) if scores[:-1] else 0.0
            final_score = (0.6 * labs_avg) + (0.4 * exam)
            details = {"Лабораторные (ср.)": labs_avg, "Экзамен": exam}

    # Если предмет не найден в условиях, вернем просто среднее арифметическое
    if final_score == 0.0:
        final_score = sum(scores) / len(scores)
        details = {"Все оценки (ср.)": final_score}

    final_score = round(final_score, 2)

    # Генерация текстовой рекомендации
    if final_score >= 7.5:
        rec = "🎉 Отличный результат! Вы уверенно идете на Отлично (8-10 баллов). Так держать!"
    elif final_score >= 5.5:
        rec = "👍 Хороший средний балл (6-7 баллов). Если хотите оценку выше, поднажмите!"
    elif final_score >= 3.5:
        rec = "⚠️ Вы близки к порогу (4-5 баллов). Будьте аккуратны, не допускайте долгов."
    else:
        rec = "🚨 Прогноз балла неудовлетворительный (меньше 4). Срочно сдайте хвосты!"

    return {
        "final_score": final_score,
        "details": details,
        "recommendation": rec
    }
