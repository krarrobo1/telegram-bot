from telebot import types


def create_keyboard_menu(data):
    keyboard = []
    for item in data:
        opt = [types.InlineKeyboardButton(text=item, callback_data=item)]
        keyboard.append(opt)
    return types.InlineKeyboardMarkup(keyboard)


def create_card(name, data):
    template = """
    -------------------------{0}-------------------------------
    {1}
    
    Ingredients:
    {2}
    
    Prices
    - S (4 slices) {3}
    - M (8 slices) {4}
    - L (12 slices) {5}
    
    Health facts
    Caloric Content {6}
    
    Image: 
    {7}
    
    Choice your ideal size below...
    """
    return template.format(name, data['description'], data['ingredients'], data['small_price'], data['medium_price'], data['large_price'], data['cc'], data['image'])



def create_payment():
    markup = types.InlineKeyboardMarkup()
    btn_cancelar = types.InlineKeyboardButton(text='Cancel', callback_data="Cancel")
    markup.add(btn_cancelar)
    btn_continuar = types.InlineKeyboardButton(text='Continue order', callback_data="Show me the menu")
    markup.add(btn_continuar)
    btn_pagar = types.InlineKeyboardButton(text='Payment check', url='https://ricardoarrobo.me/')
    markup.add(btn_pagar)

    return markup

