from app import db_conn
from faker import Faker
import re
from app.models.customer import customer

fake = Faker()


def customer_base_gen(num):
    customer_data = {}
    customer_data2 = {}
    customer_data_fin = []
    excl_list = ['\nAPO', '\nFPO', '\nDPO']
    for i in range(0, num):
        customer_data[i] = {}
        customer_data[i]['name'] = fake.name()
        customer_data[i]['complete_address'] = re.sub(r"({})".format('|'.join(excl_list)), '\\1,', fake.address())
        customer_data[i]['address'] = customer_data[i]['complete_address'].split('\n')[0]
        customer_data[i]['city'] = customer_data[i]['complete_address'].split('\n')[1].split(',')[0]
        customer_data[i]['state'] = re.sub(r"(\s)", "", customer_data[i]['complete_address'].split('\n')[1].split(',')[1], 1).split(' ')[0]
        customer_data[i]['zipcode'] = re.sub(r"(\s)", "", customer_data[i]['complete_address'].split('\n')[1].split(',')[1], 1).split(' ')[1]

    for k, v in customer_data.items():
        for key in v:
            customer_data2 = v
        customer_data_fin.append(customer_data2)

    return customer_data_fin


def main(customer_base_size):

    cust = customer_base_gen(customer_base_size)

    s = next(db_conn.session_conn())

    ############################################ Create mock data for customers ###################################

    for i in cust:
        np = customer(name=i["name"], address=i["address"], city=i["city"], state=i["state"], zip_code=i["zipcode"])
        s.add(np)
    s.commit()
    ###############################################################################################################


