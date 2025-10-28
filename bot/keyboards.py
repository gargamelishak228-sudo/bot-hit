"""Клавиатуры для бота."""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Главное меню бота."""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="Перевод текста",
        callback_data="translation_menu"
    ))
    builder.add(InlineKeyboardButton(
        text="История поиска",
        callback_data="history_menu"
    ))
    builder.add(InlineKeyboardButton(
        text="Случайное слово",
        callback_data="random_word"
    ))
    builder.add(InlineKeyboardButton(
        text="Поиск по словарю",
        callback_data="search_menu"
    ))
    builder.add(InlineKeyboardButton(
        text="Помощь",
        callback_data="help_menu"
    ))
    
    builder.adjust(1)
    return builder.as_markup()


def get_translation_type_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура выбора типа перевода."""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="Со сленга на обычный",
        callback_data="translate_slang_to_normal"
    ))
    builder.add(InlineKeyboardButton(
        text="С обычного на сленг",
        callback_data="translate_normal_to_slang"
    ))
    builder.add(InlineKeyboardButton(
        text="Назад в меню",
        callback_data="back_to_main"
    ))
    
    builder.adjust(1)
    return builder.as_markup()


def get_share_keyboard(text: str) -> InlineKeyboardMarkup:
    """Клавиатура для поделиться результатом."""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="Перевести еще",
        callback_data="translate_again"
    ))
    builder.add(InlineKeyboardButton(
        text="Главное меню",
        callback_data="back_to_main"
    ))
    
    builder.adjust(1)
    return builder.as_markup()


def get_history_keyboard(history_items: list) -> InlineKeyboardMarkup:
    """Клавиатура истории поиска."""
    builder = InlineKeyboardBuilder()
    
    for i, item in enumerate(history_items[:10]):
        builder.add(InlineKeyboardButton(
            text=f"{i+1}. {item['original'][:30]}...",
            callback_data=f"history_item_{i}"
        ))
    
    builder.add(InlineKeyboardButton(
        text="Назад в меню",
        callback_data="back_to_main"
    ))
    
    builder.adjust(1)
    return builder.as_markup()


def get_cancel_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура отмены."""
    builder = InlineKeyboardBuilder()
    
    builder.add(InlineKeyboardButton(
        text="Отмена",
        callback_data="cancel"
    ))
    
    return builder.as_markup()
