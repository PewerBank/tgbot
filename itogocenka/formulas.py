from datetime import datetime

FORMULAS = {
    "1": {
        "Математический анализ": {
            "components": [
                {"name": "КР1", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                {"name": "КР2", "type": "list", "input_prompt": "Введи оценку за контрольную работу №2"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.3*КР1 + 0.3*КР2 + 0.4*Экзамен"
        },
        "Линейная алгебра и геометрия": {
            "components": [
                {"name": "Накоп", "type": "list", "input_prompt": "Введи все оценки за модуль через пробел"},
                {"name": "КР", "type": "grade", "input_prompt": "Введи оценку за контрольную работу"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.2*Накоп + 0.3*КР + 0.5*Экзамен"
        },
        "Дискретная математика": {
            "components": [
                {"name": "КР1", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "1/3*КР1 + 2/3*Экзамен"
        },
        "Технологии программирования": {
            "components": [
                {"name": "Интересность", "type": "list", "input_prompt": "Введи оценку за интересность проекта"},
                {"name": "Реализация", "type": "list", "input_prompt": "Введи оценку за реализацию проекта"},
                {"name": "ДЗ", "type": "list", "input_prompt": "Введи оценку за домашнее задание"},
                {"name": "Тест", "type": "grade", "input_prompt": "Введи оценку за тестовый экзамен"},
                {"name": "Посещаемость", "type": "grade", "input_prompt": "Введи количество посещений"},
                {"name": "Бонусы", "type": "grade", "input_prompt": "Введи бонусы, если их нет, ставь '0'"}
            ],
            "formula": "0.2*Интересность + 0.2*Реализация + 0.2*ДЗ + 0.2*Тест + 0.1*Посещаемость + 0.1*Бонусы"
        },
        "Программирование C/C++": {
            "components": [
                {"name": "Накоп", "type": "list", "input_prompt": "Введи все оценки за модуль через пробел"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.5*Накоп + 0.5*Экзамен"
        },
        "ОРГ": {
            "components": [
                {"name": "Семинары", "type": "list", "input_prompt": "Введи все оценки за семинары"},
                {"name": "Проект", "type": "grade", "input_prompt": "Введи оценку за проект"},
                {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.6*Семинары + 0.15*Проект + 0.15*LMS + 0.1*Экзамен"
        },
        "История России": {
            "semester_1": {
                "components": [
                    {"name": "Семинары1", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                    {"name": "Семинары2", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                    {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}   
                ],
                "formula": "0.29*Семинары1 + 0.29*Семинары2 + 0.21*LMS + 0.21*Экзамен"
            },
            "semester_2": {
                "components": [
                    {"name": "Семинары3", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                    {"name": "Семинары4", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                    {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                    {"name": "Проект", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}   
                ],
                "formula": "0.25*Семинары3 + 0.25*Семинары4 + 0.15*LMS + 0.2*Проект + 0.15*Экзамен"
            }
        },
        "БЖД": {
            "components": [
                {"name": "Тест1", "type": "list", "input_prompt": "Введи оценку за тест №1"},
                {"name": "Тест2", "type": "grade", "input_prompt": "Введи оценку за тест №2"},
                {"name": "Тест3", "type": "grade", "input_prompt": "Введи оценку за тест №3"},
                {"name": "Тест4", "type": "grade", "input_prompt": "Введи оценку за тест №4"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.1*Тест1 + 0.1*Тест2 + 0.1*Тест3 + 0.1*Тест4 + 0.6*Экзамен"
        },
        "Цифровая грамотность": {
            "components": [
                {"name": "Доклад", "type": "list", "input_prompt": "Введи оценку за доклад"},
                {"name": "Прогон1", "type": "list", "input_prompt": "Введи оценку за первый прогон экзамена"},
                {"name": "Прогон2", "type": "list", "input_prompt": "Введи оценку за второй прогон экзамена"},
                {"name": "Word", "type": "grade", "input_prompt": "Введи оценку за дз по Word"},
                {"name": "Excel", "type": "grade", "input_prompt": "Введи оценку за дз по Excel"},
                {"name": "PowerPoint", "type": "grade", "input_prompt": "Введи оценку за дз по PowerPoint"},
                {"name": "Посещаемость", "type": "grade", "input_prompt": "Введи количество посещений"}
            ],
            "formula": "0.1*Доклад + 0.1*Прогон1 + 0.1*Прогон2 + 0.2*Word + 0.2*Excel + 0.2*PowerPoint + 0.1*Посещаемость"
        }
    },

    "2": {
        "Математический анализ": {
            "components": [
                {"name": "КР1", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                {"name": "КР2", "type": "list", "input_prompt": "Введи оценку за контрольную работу №2"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.3*КР1 + 0.3*КР2 + 0.4*Экзамен"
        },
        "Линейная алгебра и геометрия": {
            "components": [
                {"name": "Накоп", "type": "list", "input_prompt": "Введи все оценки за модуль через пробел"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.4*Накоп + 0.6*Экзамен"
        },
        "Дискретная математика": {
            "semester_1":{
                "components": [
                    {"name": "КР1", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
                ],
                "formula": "1/3*КР2 + 2/3*Экзамен"
            },
            "semester_2":{
                "components": [
                    {"name": "КР2", "type": "list", "input_prompt": "Введи оценку за контрольную работу №2"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
                ],
                "formula": "1/3*КР1 + 2/3*Экзамен"
            }
        },
        "Технологии программирования": {
            "components": [
                {"name": "Интересность", "type": "list", "input_prompt": "Введи оценку за интересность проекта"},
                {"name": "Реализация", "type": "list", "input_prompt": "Введи оценку за реализацию проекта"},
                {"name": "ДЗ", "type": "list", "input_prompt": "Введи оценку за домашнее задание"},
                {"name": "Тест", "type": "grade", "input_prompt": "Введи оценку за тестовый экзамен"},
                {"name": "Посещаемость", "type": "grade", "input_prompt": "Введи количество посещений"},
                {"name": "Бонусы", "type": "grade", "input_prompt": "Введи бонусы, если их нет, ставь '0'"}
            ],
            "formula": "0.2*Интересность + 0.2*Реализация + 0.2*ДЗ + 0.2*Тест + 0.1*Посещаемость + 0.1*Бонусы"
        },
        "Программирование C/C++": {
            "components": [
                {"name": "Накоп", "type": "list", "input_prompt": "Введи все оценки за модуль через пробел"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.5*Накоп + 0.5*Экзамен"
        },
        "ОРГ": {
            "components": [
                {"name": "Семинары", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                {"name": "Проект", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.6*Семинары + 0.15*Проект + 0.15*LMS + 0.1*Экзамен"
        },
        "История России": {
            "semester_1": {
                "components": [
                    {"name": "Семинары1", "type": "list", "input_prompt": "Введи все оценки за семинары 1 модуля"},
                    {"name": "Семинары2", "type": "grade", "input_prompt": "Введи все оценки за семинары 2 модуля"},
                    {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за работу в SmartLMS"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}   
                ],
                "formula": "0.29*Семинары1 + 0.29*Семинары2 + 0.21*LMS + 0.21*Экзамен"
            },
            "semester_2": {
                "components": [
                    {"name": "Семинары3", "type": "list", "input_prompt": "Введи все оценки за семинары 3 модуля"},
                    {"name": "Семинары4", "type": "grade", "input_prompt": "Введи все оценки за семинары 4 модуля"},
                    {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за работу в SmartLMS"},
                    {"name": "Проект", "type": "grade", "input_prompt": "Введи оценку за проект"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}   
                ],
                "formula": "0.25*Семинары3 + 0.25*Семинары4 + 0.15*LMS + 0.2*Проект + 0.15*Экзамен"
            }
        },
        "БЖД": {
            "components": [
                {"name": "Тест1", "type": "list", "input_prompt": "Введи оценку за тест №1"},
                {"name": "Тест2", "type": "grade", "input_prompt": "Введи оценку за тест №2"},
                {"name": "Тест3", "type": "grade", "input_prompt": "Введи оценку за тест №3"},
                {"name": "Тест4", "type": "grade", "input_prompt": "Введи оценку за тест №4"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.1*Тест1 + 0.1*Тест2 + 0.1*Тест3 + 0.1*Тест4 + 0.6*Экзамен"
        },
        "Цифровая грамотность": {
            "components": [
                {"name": "Доклад", "type": "list", "input_prompt": "Введи оценку за доклад"},
                {"name": "Прогон1", "type": "list", "input_prompt": "Введи оценку за первый прогон экзамена"},
                {"name": "Прогон2", "type": "list", "input_prompt": "Введи оценку за второй прогон экзамена"},
                {"name": "Word", "type": "grade", "input_prompt": "Введи оценку за дз по Word"},
                {"name": "Excel", "type": "grade", "input_prompt": "Введи оценку за дз по Excel"},
                {"name": "PowerPoint", "type": "grade", "input_prompt": "Введи оценку за дз по PowerPoint"},
                {"name": "Посещаемость", "type": "grade", "input_prompt": "Введи количество посещений"}
            ],
            "formula": "0.1*Доклад + 0.1*Прогон1 + 0.1*Прогон2 + 0.2*Word + 0.2*Excel + 0.2*PowerPoint + 0.1*Посещаемость"
        }
    },
    "3": {
        "Математический анализ": {
            "components": [
                {"name": "КР1", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                {"name": "КР2", "type": "list", "input_prompt": "Введи оценку за контрольную работу №2"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.3*КР1 + 0.3*КР2 + 0.4*Экзамен"
        },
        "Линейная алгебра и геометрия": {
            "components": [
                {"name": "Накоп", "type": "list", "input_prompt": "Введи все оценки за модуль через пробел"},
                {"name": "КР", "type": "grade", "input_prompt": "Введи оценку за контрольную работу"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.2*Накоп + 0.3*КР + 0.5*Экзамен"
        },
        "Дискретная математика": {
            "components": [
                {"name": "КР1", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "1/3*КР1 + 2/3*Экзамен"
        },
        "Технологии программирования": {
            "components": [
                {"name": "Интересность", "type": "list", "input_prompt": "Введи оценку за интересность проекта"},
                {"name": "Реализация", "type": "list", "input_prompt": "Введи оценку за реализацию проекта"},
                {"name": "ДЗ", "type": "list", "input_prompt": "Введи оценку за домашнее задание"},
                {"name": "Тест", "type": "grade", "input_prompt": "Введи оценку за тестовый экзамен"},
                {"name": "Посещаемость", "type": "grade", "input_prompt": "Введи количество посещений"},
                {"name": "Бонусы", "type": "grade", "input_prompt": "Введи бонусы, если их нет, ставь '0'"}
            ],
            "formula": "0.2*Интересность + 0.2*Реализация + 0.2*ДЗ + 0.2*Тест + 0.1*Посещаемость + 0.1*Бонусы"
        },
        "Программирование C/C++": {
            "components": [
                {"name": "Накоп", "type": "list", "input_prompt": "Введи все оценки за модуль через пробел"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.5*Накоп + 0.5*Экзамен"
        },
        "ОРГ": {
            "components": [
                {"name": "Семинары", "type": "list", "input_prompt": "Введи оценку за контрольную работу №1"},
                {"name": "Проект", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за экзамен"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.6*Семинары + 0.15*Проект + 0.15*LMS + 0.1*Экзамен"
        },
        "История России": {
            "semester_1": {
                "components": [
                    {"name": "Семинары1", "type": "list", "input_prompt": "Введи все оценки за семинары 1 модуля"},
                    {"name": "Семинары2", "type": "grade", "input_prompt": "Введи все оценки за семинары 2 модуля"},
                    {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за работу в SmartLMS"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}   
                ],
                "formula": "0.29*Семинары1 + 0.29*Семинары2 + 0.21*LMS + 0.21*Экзамен"
            },
            "semester_2": {
                "components": [
                    {"name": "Семинары3", "type": "list", "input_prompt": "Введи все оценки за семинары 3 модуля"},
                    {"name": "Семинары4", "type": "grade", "input_prompt": "Введи все оценки за семинары 4 модуля"},
                    {"name": "LMS", "type": "grade", "input_prompt": "Введи оценку за работу в SmartLMS"},
                    {"name": "Проект", "type": "grade", "input_prompt": "Введи оценку за проект"},
                    {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}   
                ],
                "formula": "0.25*Семинары3 + 0.25*Семинары4 + 0.15*LMS + 0.2*Проект + 0.15*Экзамен"
            }
        },
        "БЖД": {
            "components": [
                {"name": "Тест1", "type": "list", "input_prompt": "Введи оценку за тест №1"},
                {"name": "Тест2", "type": "grade", "input_prompt": "Введи оценку за тест №2"},
                {"name": "Тест3", "type": "grade", "input_prompt": "Введи оценку за тест №3"},
                {"name": "Тест4", "type": "grade", "input_prompt": "Введи оценку за тест №4"},
                {"name": "Экзамен", "type": "grade", "input_prompt": "Введи оценку за экзамен"}
            ],
            "formula": "0.1*Тест1 + 0.1*Тест2 + 0.1*Тест3 + 0.1*Тест4 + 0.6*Экзамен"
        },
        "Цифровая грамотность": {
            "components": [
                {"name": "Доклад", "type": "list", "input_prompt": "Введи оценку за доклад"},
                {"name": "Прогон1", "type": "list", "input_prompt": "Введи оценку за первый прогон экзамена"},
                {"name": "Прогон2", "type": "list", "input_prompt": "Введи оценку за второй прогон экзамена"},
                {"name": "Word", "type": "grade", "input_prompt": "Введи оценку за дз по Word"},
                {"name": "Excel", "type": "grade", "input_prompt": "Введи оценку за дз по Excel"},
                {"name": "PowerPoint", "type": "grade", "input_prompt": "Введи оценку за дз по PowerPoint"},
                {"name": "Посещаемость", "type": "grade", "input_prompt": "Введи количество посещений"}
            ],
            "formula": "0.1*Доклад + 0.1*Прогон1 + 0.1*Прогон2 + 0.2*Word + 0.2*Excel + 0.2*PowerPoint + 0.1*Посещаемость"
        }
    }
}

def calculate_subject_score(formula_str: str, grades: dict) -> float:

    try:
        eval_loc = {key: float(val) for key, val in grades.items()}
        result = eval(formula_str, {"__builtins__": None}, eval_loc)
        return round(float(result), 2)
    except Exception:
        return 0.0



def get_subject(stream_id):
    stream = FORMULAS.get(stream_id,{})
    subj = []
    for sub in stream:
        subj.append(sub)
    return subj


def get_formula(stream_id, subj):
    stream = FORMULAS.get(stream_id, {})
    subj_data = stream.get(subj, {})
    
    if not subj_data:
        return {}
    if "semester_1" in subj_data:
        current_month = datetime.now().month
        if 1 <= current_month <= 6:
            return subj_data["semester_2"]
        return subj_data["semester_1"]
        
    return subj_data