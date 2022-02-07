from app.customer_gen import main
from app.census_gen import gen_census_data
from app.models.customer import customer
from app.create_tables_if_not_exists import create_table_if_not_exists


# define customer base size
customer_base_size = 1000

# Create the table if it doesn't exist
create_table_if_not_exists(customer, customer.__table__.name)

# Used for one time insert
main(customer_base_size)

# Generate census data
gen_census_data()


