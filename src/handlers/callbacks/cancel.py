from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from src.keyboards.default import main_menu_keyboard

router = Router()


@router.callback_query(F.data == "cancel_actions")
async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()
    await callback.message.answer(
        text=(
            "Буюртмангиз ўлчамлари ва тираж сонини киритиб, "
            "сотув менеджерига мурожаат қилмасдан буюртма нархини ҳисоблашингиз мумкин.\n\n"
            "<b>Офсет машина модели: Komori 644-L</b>\n"
            "▪️<b>Максимал қоғоз ўлчами: 112 х 82 см</b>n"
            "▪️<b>Минимал қоғоз ўлчами: 62 х 46 см</b>\n"
            "▪️<b>Максимал босиш майдони: 112 х 81 см </b>"
        ),
        reply_markup=main_menu_keyboard()
    )