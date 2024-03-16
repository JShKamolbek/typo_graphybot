from aiogram import Router, types
from aiogram.filters import CommandStart

from src.infrastructure.database.dao import HolderDao
from src.keyboards.default import main_menu_keyboard

router = Router()


@router.message(CommandStart())
async def on_cmd_start(message: types.Message, dao: HolderDao):
    await message.answer(
        text=(
            "Буюртмангиз ўлчамлари ва тираж сонини киритиб, "
            "сотув менеджерига мурожаат қилмасдан буюртма нархини ҳисоблашингиз мумкин.\n\n"
            "<b>Офсет машина модели: Komori 644-L</b>\n"
            "▪️<b>Максимал қоғоз ўлчами: 112 х 82 см</b>\n"
            "▪️<b>Минимал қоғоз ўлчами: 62 х 46 см</b>\n"
            "▪️<b>Максимал босиш майдони: 112 х 81 см </b>"
        ),
        reply_markup=main_menu_keyboard()
    )
