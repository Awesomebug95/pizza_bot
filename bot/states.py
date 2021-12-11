from transitions import Machine


class Matter(object):
    def __init__(self):
        self.set_size()
        self.set_payment_method()

    def set_size(self, size=''):
        self.size = size

    def set_payment_method(self, payment=''):
        self.payment = payment

    def __str__(self):
        return f"Вы хотите {self.size} пиццу, оплата - {self.payment}?"


lump = Matter()
machine = Machine(lump, ['none', 'get_size', 'get_payment', 'get_confirm'], initial='none')
machine.add_transition('pizza_size', 'none', 'get_size', before='set_size')
machine.add_transition('payment_method', 'get_size', 'get_payment', before='set_payment_method')
machine.add_transition('confirm_order', 'get_payment', 'get_confirm', before=None)
