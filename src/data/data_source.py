from src.helpers import query_helper, uri_parse

def load_data():
	raw_data = query_helper.get_pizza_list()['results']['bindings']
	if raw_data:
		return {
            "AmericanaPizza": {
                'description': "Americana Pizza it's the authentic american\'s favorite pizza",
                'cc':"767",
                'ingredients': """
                    - Mozarella 
                    - Tomato
                    - Pepperoni
                """,
                'image':"https://placeralplato.com/files/2016/01/Pizza-con-pepperoni-640x480.jpg?width=1200&enable=upscale",
                'small_price': "$8.00",
                "medium_price": "$16.00",
                "large_price": "$20.00"
            },
            "MargheritaPizza": {
                'description': "Margherita it's the authentic italian\'s favorite pizza",
                'cc':"263",
                'ingredients': """
                    - Mozarella 
                    - Tomato
                """,
                'image':"https://placeralplato.com/files/2015/06/pizza-Margarita-640x480.jpg?width=1200&enable=upscale",
                'small_price': "$8.00",
                "medium_price": "$16.00",
                "large_price": "$20.00"
            },
            "SohoPizza": {
                'description': "SohoPizza it's the best pizza for cheesy pizza lovers",
                'cc': "342",
                'ingredients': """
                    - Parmesan
                    - Tomato
                    - Mozarella
                    - Olive
                """,
                'image':"https://media-cdn.tripadvisor.com/media/photo-s/18/fa/f3/ef/roasted-mushroom-ny-pizza.jpg",
                'small_price': "$8.00",
                "medium_price": "$16.00",
                "large_price": "$20.00"
            },
            "AmericanaHotPizza": {
                'description': "Americana Pizza it's the authentic american\'s favorite pizza with extra spicy ingredients",
                'cc':"767",
                'ingredients': """
                    - Mozarella 
                    - Tomato
                    - Pepperoni
                    - Jalapeno
                """,
                'image':"https://www.charbroil.com/media/ctm//H/o/How_To_How_to_Grill_Pizza.jpg.jpeg",
                'small_price': "$8.00",
                "medium_price": "$16.00",
                "large_price": "$20.00"
            }
        }
	# else:
	# 	menu = dict(uri_parse.get_resource_name(item['pizza']['value']) for item in raw_data)
    #     for item in menu:
    #         raw_info = query_helper.get_pizza_info(item)['results']['bindings']
    #         if raw_info:
    #             menu[item]['cc'] = raw_info['caloricContent']['value']
    #             splited_ingredients = raw_info['igroup']['value'].split(',')
    #             menu[item]['ingredients'] =  "- \n".join([uri_parse.get_resource_name(uri) for uri in splited_ingredients])
    #             menu[item]['image'] = raw_info['image']['value']
    #             menu[item]['small_price'] = raw_info['sp']['value']
    #             menu[item]['medium_price'] = raw_info['mp']['value']
    #             menu[item]['large_price'] = raw_info['lp']['value']
    #     return menu

pizza_list = load_data()
size_list = ['S', 'M', 'L']


text_messages = {
	'welcome':
		u'Please welcome {name}!\n\n'
		u'My Name is PizzaBot.\n'
		u'Nice to meet you, How could I help you \n'
		u' Use the command /info to get more information \n'
		u' Use the command /menu to see our menu \n'
		u' Use the command /recommendation to help you with recommendations \n'
		u' Or use the menu below to interact with me',
	'info':
		u'My name is PizzaBot \n'
		u'I am a bot that assist you to order pizza and make recommendations based on your requirements',

	'fallback':
		u'Sorry I could not understand that!',
}

