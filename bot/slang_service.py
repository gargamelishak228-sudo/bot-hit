"""Сервис для работы со сленговым словарем из JSON файла."""

import json
import logging
import random
import os
from typing import Dict, List, Tuple, Optional

logger = logging.getLogger(__name__)


class SlangService:
    """Сервис для перевода сленга с помощью JSON словаря."""

    def __init__(self, json_file: str = "slang_dict.json"):
        """
        Инициализация сервиса.

        Args:
            json_file: Путь к JSON файлу со сленговым словарем.
        """
        self.json_file = json_file
        self.slang_dict = self._load_slang_dict()
        logger.info(f"Сленговый словарь загружен из {json_file}. Количество слов: {len(self.slang_dict)}")

    def _load_slang_dict(self) -> Dict[str, Dict[str, str]]:
        """Загружает сленговый словарь из JSON файла."""
        try:
            with open(self.json_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Файл словаря {self.json_file} не найден.")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка при чтении JSON файла {self.json_file}: {e}")
            return {}

    def translate_slang_to_normal(self, text: str) -> Tuple[str, str]:
        """Переводит текст со сленга на обычный язык с объяснением."""
        # Разбиваем текст на слова и пробелы
        import re
        parts = re.findall(r'\b\w+\b|\s+|[^\w\s]', text)
        translated_parts = []
        explanations = []

        for part in parts:
            # Проверяем только слова (не пробелы и знаки препинания)
            if part.isalpha():
                clean_word = part.lower().strip()
                if clean_word in self.slang_dict:
                    entry = self.slang_dict[clean_word]
                    translated_parts.append(entry["normal"])
                    explanations.append(f"'{clean_word}' → '{entry['normal']}': {entry['explanation']}")
                else:
                    translated_parts.append(part)
            else:
                # Пробелы и знаки препинания оставляем как есть
                translated_parts.append(part)

        translation = ''.join(translated_parts)
        explanation = '; '.join(explanations) if explanations else "Сленговые слова не найдены в словаре."

        return translation, explanation

    def get_random_slang(self) -> Optional[Dict[str, str]]:
        """Возвращает случайное сленговое слово из словаря."""
        if not self.slang_dict:
            return None
        slang_word = random.choice(list(self.slang_dict.keys()))
        entry = self.slang_dict[slang_word]
        return {
            "slang": slang_word,
            "normal": entry["normal"],
            "explanation": entry["explanation"]
        }

    def search_slang(self, query: str) -> List[Dict[str, str]]:
        """Ищет сленговые слова по запросу."""
        results = []
        query_lower = query.lower().strip()

        for slang, entry in self.slang_dict.items():
            # Ищем по сленговому слову
            if query_lower in slang.lower():
                results.append({
                    "slang": slang,
                    "normal": entry["normal"],
                    "explanation": entry["explanation"]
                })
            # Ищем по нормальному значению
            elif query_lower in entry["normal"].lower():
                results.append({
                    "slang": slang,
                    "normal": entry["normal"],
                    "explanation": entry["explanation"]
                })
            # Ищем по объяснению
            elif query_lower in entry["explanation"].lower():
                results.append({
                    "slang": slang,
                    "normal": entry["normal"],
                    "explanation": entry["explanation"]
                })
        
        # Убираем дубликаты и возвращаем первые 10 результатов
        seen = set()
        unique_results = []
        for result in results:
            if result["slang"] not in seen:
                seen.add(result["slang"])
                unique_results.append(result)
        
        return unique_results[:10]

    def get_stats(self) -> Dict[str, int]:
        """Возвращает статистику словаря."""
        file_size = os.path.getsize(self.json_file) if os.path.exists(self.json_file) else 0
        return {
            "total_words": len(self.slang_dict),
            "file_size": file_size
        }

    def add_slang_word(self, slang: str, normal: str, explanation: str) -> bool:
        """Добавляет новое сленговое слово в словарь."""
        try:
            self.slang_dict[slang.lower()] = {
                "normal": normal,
                "explanation": explanation
            }
            
            # Сохраняем в файл
            with open(self.json_file, "w", encoding="utf-8") as f:
                json.dump(self.slang_dict, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Добавлено новое слово: {slang}")
            return True
        except Exception as e:
            logger.error(f"Ошибка при добавлении слова {slang}: {e}")
            return False


# Создаем глобальный экземпляр сервиса
slang_service = SlangService()