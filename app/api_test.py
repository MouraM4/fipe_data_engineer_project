import json
import requests
import time

from helpers.logger import logger
from helpers.fipe_functions import *


# Get all car brand
brand_list = get_all_car_brands()


# Get all cars info from Ferrari
ferrari_list = get_all_car_models(brand_list[27].get('Value')) 
ferrari_brand_code = brand_list[27].get('Value')

ferrari_cars_info = []
ferrari_models = ferrari_list.get('Modelos')

for model in ferrari_models:
    model_code = model.get('Value')
    car_model_year_list = get_car_model_year(ferrari_brand_code, model_code)

    # time.sleep(3)

    for model_year in car_model_year_list:
        year_model = model_year.get('Value')
        year = year_model.split("-")[0]
        car_info = get_price_with_all_params(ferrari_brand_code, model_code, year_model, year)
        ferrari_cars_info.append(car_info)
        print(f"Model: {car_info.get('Modelo')} - Price: {car_info.get('Valor')} - Year: {year}")

import pandas as pd

ferrari_df = pd.DataFrame(ferrari_cars_info)
