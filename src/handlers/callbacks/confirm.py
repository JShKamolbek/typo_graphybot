from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.keyboards.default import main_menu_keyboard
from src.keyboards.inline import cancel_keyboard
from src.keyboards.inline.confirm import ConfirmCallbackData
from src.states import DataForm

router = Router()


@router.callback_query(ConfirmCallbackData.filter())
async def confirm_query(callback: types.CallbackQuery, callback_data: ConfirmCallbackData, state: FSMContext):
    msg = callback.message.html_text
    await state.update_data(msg=msg)
    if callback_data.action == "confirm":
        await callback.message.answer(
            text="Буюртма бериш учун ташкилот номи ва исмингизни киритинг",
            reply_markup=cancel_keyboard()
        )
        await state.set_state(DataForm.full_name)
    elif callback_data.action == "cancel":
        await callback.message.delete()
        await callback.message.answer(
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
