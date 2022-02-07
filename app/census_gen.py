import pandas as pd
from app.db_conn import engine
from app.create_tables_if_not_exists import create_table_if_not_exists
from app.models.census import CensusAdultPopByState


df = pd.read_excel(r'/c/Users/anayk/OneDrive/Torqata/SCPRC-EST2019-18+POP-RES.xlsx'
                   , sheet_name='SCPRC'
                   , skiprows=range(1,9)
                   , nrows=52
                   , usecols="A:D")

df = df.rename(columns= {list(df)[0]: 'geographic_area'
                        , list(df)[1]: 'total_resident_population'
                        , list(df)[2]: 'total_resident_18yr_and_older'
                        , list(df)[3]: 'percentage_population'})

df = df.replace('[^a-zA-Z0-9 ]', '', regex=True)

def gen_census_data():
    create_table_if_not_exists(CensusAdultPopByState, CensusAdultPopByState.__table__.name)
    df.to_sql(CensusAdultPopByState.__table__.name, con=engine, if_exists='append', schema='torqata_data_ip', index=False)
