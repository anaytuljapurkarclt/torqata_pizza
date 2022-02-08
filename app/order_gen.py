from datetime import datetime, timedelta
from faker import Faker
import time, random, requests
from app.schemas.orderBase import orderBase
from app.create_tables_if_not_exists import create_table_if_not_exists
from app.models.orders import orders

fake = Faker()


def randdatereturn(start_date, end_date):
    tbd = end_date - start_date
    dbd = tbd.days

    randdays = random.randrange(dbd)
    randhours = random.randrange(0, 24)
    randmins = random.randrange(0, 60)
    randsecs = random.randrange(0, 60)

    retTime = start_date + timedelta(days=randdays, hours=randhours, minutes=randmins, seconds=randsecs)

    timetup = time.mktime(retTime.timetuple()) # Convert the time into a time tuple for utcfromtimestamp to consume

    return datetime.utcfromtimestamp(timetup)


def price_eval(pt, price):
    if pt == "cheese":
        return price[0]
    elif pt == "pepperoni":
        return price[1]
    elif pt == "supreme":
        return price[2]
    elif pt == "meat lover":
        return price[3]
    else:
        return price[4]


def order_base_gen(customer_base_size):
    cbs = customer_base_size
    order_data = {}
    pizza_type = ["cheese", "pepperoni", "supreme", "meat lover", "veggie"]
    pizza_price = [12.99, 13.99, 15.99, 14.99, 12]
    max_qty = 5
    start_date = datetime(2018, 1, 1)
    end_date = datetime.now().replace(microsecond=0)

    order_data['customer_id'] = random.choice(range(1, cbs+1))
    order_data['type'] = random.choice(pizza_type)
    order_data['qty'] = random.choice(range(1, max_qty+1))
    order_data['untaxed_retail_price'] = order_data['qty']*round(price_eval(order_data['type'], pizza_price), 2)
    order_data['retail_price'] = round((order_data['untaxed_retail_price']*5.09)/100 + order_data['untaxed_retail_price'], 2)
    order_data['order_date'] = randdatereturn(start_date, end_date)
    order_data['load_ts'] = order_data['order_date']
    order_base = orderBase(**order_data)
    return order_base


def post_order_data(customer_base_size):
    order_det_ip = order_base_gen(customer_base_size)
    # print(order_det_ip.json())
    r = requests.post("http://127.0.0.1:8000/createOrdersRecords/", data=order_det_ip.json())


create_table_if_not_exists(orders, orders.__table__.name)

for i in range(1, 25001):
    post_order_data(1000)