import redis
import uuid
import json

r = redis.Redis(host='localhost', port=6379, db=0)

# States
# init
# asking_menu
# still_in_order
# payed
# cancel

def storeUserSession(user_id):
    r.set(user_id, "init")

def getUserState(user_id):
    return r.get(user_id)

def updateUserState(user_id, state):
    r.set(user_id, state)

# Order details, state, total
def storeUserOrder(user_id, item):
    orderId = '{0}.{1}'.format(user_id, uuid.uuid1())
    r.set(orderId, json.dumps(item))

# Get user Orders then parse to Dict
def getUserOrder(user_id):
    orderPattern = '{0}.*'.format(user_id)
    orders = r.keys(pattern=orderPattern)
    receipt = []
    total = 0

    for item in orders:
        order = r.get(str(item))
        #item = json.loads(item)
        print(order)
        #orderDetail = """
         #   Item: .............. {0}
          #  Precio: ............ {1}
        #"""
        #receipt.append(orderDetail.format(item['item'], item['price']))
        #total += item['price']

    if len(receipt) == 0:
        return "No tienes ordenes activas..."
    else:
        return "-----------------------------------------\n".join(receipt) + total