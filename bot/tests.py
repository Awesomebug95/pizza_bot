import unittest

from main import logic_of_order_pizza
from states import lump


ORDER_ERR_1 = 'order_pizza(), ошибка при получении размера.'
ORDER_ERR_2 = 'order_pizza(), ошибка при выборе оплаты.'
ORDER_ERR_3 = 'order_pizza(), ошибка при подтверждении заказа.'

FSM_ERR_1 = 'FSM - ошибка изменения состояния. Шаг - pizza_size()'
FSM_ERR_2 = 'FSM - ошибка изменения состояния. Шаг - payment_method()'
FSM_ERR_3 = 'FSM - ошибка изменения состояния. Шаг - confirm_order()'

RESULT_1 = 'Как вы будете платить?'
RESULT_2 = 'Вы хотите большую пиццу, оплата - наличкой?'
RESULT_3 = 'Спасибо за заказ'

FSM_STATE_1 = 'get_size'
FSM_STATE_2 = 'get_payment'
FSM_STATE_3 = 'get_confirm'

CALL_SIZE = 'БоЛьШуЮ'
CALL_PAYMENT = 'НаЛиЧкОй'
CALL_CONFIRM = 'ДА'


class TestDialogBot(unittest.TestCase):
    """
    Тестируем основную логику бота: logic_of_order_pizza().
    """

    def test_dialog_and_fsm(self):
        call = logic_of_order_pizza(CALL_SIZE)
        self.assertEqual(
            call, RESULT_1, ORDER_ERR_1
        )
        self.assertEqual(
            str(lump.state), FSM_STATE_1, FSM_ERR_1
        )
        call_2 = logic_of_order_pizza(CALL_PAYMENT)
        self.assertEqual(
            call_2, RESULT_2, ORDER_ERR_2
        )
        self.assertEqual(
            str(lump.state), FSM_STATE_2, FSM_ERR_2
        )
        call_3 = logic_of_order_pizza(CALL_CONFIRM)
        self.assertEqual(
            call_3, RESULT_3, ORDER_ERR_3
        )
        self.assertEqual(
            str(lump.state), FSM_STATE_3, FSM_ERR_3
        )


if __name__ == '__main__':
    unittest.main()
