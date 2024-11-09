import ollama
import re
from datetime import datetime, timedelta
from typing import List, Tuple, Dict

def get_current_date():
    """Возвращает текущую дату в формате ГГГГ-ММ-ДД."""
    return datetime.now().strftime("%Y-%m-%d")

def analyze_user_intent(input_text: str, cycle_num: int) -> str:
    """
    Анализирует намерение пользователя на основе введенного текста.
    Разные подходы для разных циклов.
    
    :param input_text: Текст пользователя
    :param cycle_num: Номер цикла (1, 2 или 3)
    :return: Строка с намерением пользователя
    """
    prompts = {
        1: f"""
        Проанализируй текст пользователя и определи его основное намерение.
        Фокусируйся на базовой цели запроса.
        
        Основные шаги:
        1. Найди ключевые слова
        2. Определи тип запроса (информационный, аналитический, творческий)
        3. Определи основную тему
        4. Сформулируй цель одним предложением
        
        Не повторяй текст запроса, создай новую формулировку намерения.
        
        Текст пользователя: {input_text}
        Намерение:
        """,
        
        2: f"""
        Рассмотри следующий текст пользователя с точки зрения эксперта
        и определи глубинное намерение запроса.
        
        При анализе учитывай:
        1. Контекст запроса
        2. Возможные неявные цели
        3. Ожидаемый формат ответа
        4. Уровень детализации
        5. Потенциальные смежные интересы
        
        Сформулируй намерение иначе, чем в явном запросе.
        
        Текст пользователя: {input_text}
        Глубинное намерение:
        """,
        
        3: f"""
        Проведи комплексный анализ запроса пользователя.
        Определи максимально широкий контекст запроса.
        
        Рассмотри:
        1. Явные и неявные цели
        2. Возможные предпосылки запроса
        3. Сопутствующие темы
        4. Потенциальные последующие вопросы
        5. Практическое применение информации
        
        Дай расширенную интерпретацию намерения пользователя.
        
        Текст пользователя: {input_text}
        Расширенное намерение:
        """
    }
    
    try:
        intent_response = ollama.generate(
            model='gemma2:27b', 
            prompt=prompts[cycle_num]
        )
        return intent_response['response'].strip()
    except Exception:
        return None

def generate_llm_prompt(input_text: str, user_intent: str, cycle_num: int) -> str:
    """
    Генерирует эффективный промпт для LLM.
    Разные подходы к генерации для разных циклов.
    
    :param input_text: Текст пользователя
    :param user_intent: Намерение пользователя
    :param cycle_num: Номер цикла (1, 2 или 3)
    :return: Сгенерированный промпт
    """
    current_date = datetime.now()
    
    templates = {
        1: f"""
        Создай базовый промпт для получения прямого ответа на запрос пользователя.
        
        Правила:
        1. Чёткая формулировка основного вопроса
        2. Указание желаемого формата ответа
        3. Минимум необходимых уточнений
        
        Текст: {input_text}
        Намерение: {user_intent}
        Дата: {current_date.strftime("%Y-%m-%d")}
        
        Сгенерируй промпт:
        """,
        
        2: f"""
        Создай детальный промпт для получения развёрнутого ответа.
        
        Требования:
        1. Структурирование информации
        2. Запрос дополнительного контекста
        3. Уточнение связанных аспектов
        4. Указание на необходимость пояснений
        
        Текст: {input_text}
        Намерение: {user_intent}
        Дата: {current_date.strftime("%Y-%m-%d")}
        
        Сгенерируй промпт:
        """,
        
        3: f"""
        Создай комплексный промпт для получения полного анализа темы.
        
        Включи требования:
        1. Охват всех аспектов темы
        2. Примеры и иллюстрации
        3. Практическое применение
        4. Связь с другими темами
        5. Перспективы и тенденции
        
        Текст: {input_text}
        Намерение: {user_intent}
        Дата: {current_date.strftime("%Y-%m-%d")}
        
        Сгенерируй промпт:
        """
    }
    
    try:
        prompt_response = ollama.generate(
            model='gemma2:27b',
            prompt=templates[cycle_num]
        )
        return prompt_response['response'].strip()
    except Exception:
        return None

def get_llm_response(prompt: str, cycle_num: int) -> str:
    """
    Получает ответ от языковой модели.
    Разные подходы для разных циклов.
    
    :param prompt: Подготовленный промпт
    :param cycle_num: Номер цикла
    :return: Ответ модели
    """
    try:
        # Добавляем специфические инструкции в зависимости от цикла
        cycle_instructions = {
            1: "Дай прямой и краткий ответ на вопрос.",
            2: "Предоставь развёрнутый ответ с пояснениями.",
            3: "Создай полный анализ темы с примерами и контекстом."
        }
        
        full_prompt = f"{cycle_instructions[cycle_num]}\n\n{prompt}"
        
        response = ollama.generate(
            model='gemma2:27b',
            prompt=full_prompt
        )
        return response['response'].strip()
    except Exception as e:
        return f"Ошибка при получении ответа от модели: {str(e)}"

def post_process_prompt(prompt: str) -> str:
    """Обрабатывает полученный промпт."""
    prompt = prompt.strip('"').strip("'")
    prompt = re.sub(r'^(промпт:|prompt:)\s*', '', prompt, flags=re.IGNORECASE)
    prompt = re.sub(r'\s+', ' ', prompt)
    return prompt.strip()

def validate_prompt(prompt: str) -> bool:
    """Проверяет корректность промпта."""
    return bool(prompt) and len(prompt.split()) >= 3

def process_single_cycle(user_input: str, cycle_num: int) -> Dict[str, str]:
    """
    Выполняет один полный цикл обработки запроса.
    
    :param user_input: Текст пользователя
    :param cycle_num: Номер цикла
    :return: Словарь с результатами цикла
    """
    print(f"\nЦикл {cycle_num}:")
    
    # Анализ намерения с учетом номера цикла
    print("Анализ намерения...")
    intent = analyze_user_intent(user_input, cycle_num)
    if not intent:
        raise Exception("Не удалось определить намерение пользователя")
    print(f"Намерение: {intent}")

    # Генерация промпта
    print("Генерация промпта...")
    llm_prompt = generate_llm_prompt(user_input, intent, cycle_num)
    if not llm_prompt:
        raise Exception("Не удалось сгенерировать промпт")
    final_prompt = post_process_prompt(llm_prompt)
    if not validate_prompt(final_prompt):
        raise Exception("Сгенерированный промпт некорректен")
    print(f"Промпт: {final_prompt}")

    # Получение ответа
    print("Получение ответа...")
    response = get_llm_response(final_prompt, cycle_num)
    if not response:
        raise Exception("Не удалось получить ответ от модели")
    print(f"Ответ: {response}")

    return {
        "intent": intent,
        "prompt": final_prompt,
        "response": response
    }

def synthesize_final_answer(cycles: List[Dict[str, str]], original_query: str) -> str:
    """
    Создает финальный синтезированный ответ на основе трех циклов.
    
    :param cycles: Список словарей с результатами каждого цикла
    :param original_query: Исходный запрос пользователя
    :return: Синтезированный ответ
    """
    synthesis_prompt = f"""
    На основе предоставленной информации создай полный, но хорошо структурированный ответ 
    на вопрос пользователя: "{original_query}"

    Правила создания ответа:
    1. Начни с краткого, прямого ответа на вопрос (основные цифры/факты)
    2. Структурируй информацию по разделам:
       - Основная информация
       - Хронология и эволюция
         * Ранний период
         * Период развития
         * Современный этап
       - Значимые работы и достижения
       - Влияние и значение
       - Интересные факты и детали
    3. В каждом разделе предоставь детальную информацию
    4. Используй подзаголовки для лучшей навигации
    5. Включи все значимые аспекты из предоставленных источников
    
    Информация из источников:
    ---
    Базовый ответ:
    {cycles[0]['response']}
    ---
    Развёрнутый ответ:
    {cycles[1]['response']}
    ---
    Полный анализ:
    {cycles[2]['response']}
    ---

    Требования к ответу:
    - Используй форматирование markdown для лучшей читаемости
    - Сохраняй всю важную информацию из источников
    - Организуй информацию логически
    - Используй списки и подзаголовки
    - Выделяй ключевые моменты
    
    Не упоминай о процессе анализа или источниках информации - 
    просто предоставь полный, хорошо организованный ответ.
    """

    try:
        synthesis_response = ollama.generate(model='gemma2:27b', prompt=synthesis_prompt)
        return synthesis_response['response'].strip()
    except Exception as e:
        return f"Ошибка при синтезе финального ответа: {str(e)}"

def process_user_input(user_input: str) -> Tuple[List[Dict[str, str]], str]:
    """
    Обрабатывает ввод пользователя с получением трех ответов и финального синтеза.
    
    :param user_input: Текст пользователя
    :return: Tuple[список результатов циклов, синтезированный ответ]
    """
    if not user_input:
        return [], "Пожалуйста, введите текст для создания промпта."

    # Выполняем три независимых цикла
    cycles = []
    for i in range(3):
        cycle_results = process_single_cycle(user_input, i + 1)
        cycles.append(cycle_results)

    # Создаем финальный синтез
    final_synthesis = synthesize_final_answer(cycles, user_input)

    return cycles, final_synthesis

def main():
    """Основная функция программы."""
    print("\nDeepChain Refinement LLM v1.0.0:")
    print("Using chain-of-thought, multi-step prompting,")
    print("progressive refinement and response synthesis")
    print("Built on Ollama architecture. Powered by 'Gemma2:9B'\n")
    
    while True:
        try:
            user_input = input("\nВведите текст для создания промпта (или 'выход' для завершения): ").strip()
            if user_input.lower() == 'выход':
                print("Завершение работы.")
                break
                
            # Получаем результаты циклов и финальный синтез
            cycles, final_synthesis = process_user_input(user_input)
            
            # Выводим результаты каждого цикла
            for i, cycle in enumerate(cycles, 1):
                print(f"\nЦикл {i}:")
                print(f"Намерение: {cycle['intent']}")
                print(f"Промпт: {cycle['prompt']}")
                print(f"Ответ: {cycle['response']}")
            
            # Выводим финальный синтез
            print("\nФинальный синтезированный ответ:\n")
            print(final_synthesis)
                
        except KeyboardInterrupt:
            print("\nЗавершение работы.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()