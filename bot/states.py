"""Состояния FSM для бота."""

from aiogram.fsm.state import State, StatesGroup


class TranslationStates(StatesGroup):
    """Состояния для перевода текста."""
    waiting_for_text = State()
    waiting_for_search = State()
