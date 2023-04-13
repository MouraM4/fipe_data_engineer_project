import json

import pandas as pd

from datetime import datetime
from helpers.fipe_functions import FipeIntegration
from helpers.kinesis_aws import AWSFirehose
from helpers.logger import logger


if __name__ == '__main__':

    fipe_integration = FipeIntegration()

    # Get all car brand
    all_brand_list = fipe_integration.get_all_car_brands()
    brand_cars_info = []

    for brand in all_brand_list:

        # Get all cars info from all Car Brands
        brand_list = fipe_integration.get_all_car_models(brand.get('Value')) 
        brand_name = brand.get('Label')
        brand_code = brand.get('Value')
        
        brand_models = brand_list.get('Modelos')

        for model in brand_models:
            model_code = model.get('Value')
            car_model_year_list = fipe_integration.get_car_model_year(brand_code, model_code)

            for model_year in car_model_year_list:
                year_model = model_year.get('Value')
                year = year_model.split("-")[0]
                fuel_type = year_model.split("-")[1]
                car_info = fipe_integration.get_price_with_all_params(year_model, year, fuel_type)
                
                brand_cars_info.append(car_info)
                logger.info(f"Brand: {brand_name} - Model: {car_info.get('Modelo')} - Price: {car_info.get('Valor')} - Year: {year}")
            
    with open('car_brands.json', 'w') as f:
        json.dumps(brand_cars_info, f)


    # Send data to firehose
    aws_firehose = AWSFirehose()
    aws_firehose.kinesis_firehose_put_record(json.dumps(brand_cars_info).replace('[','').replace(']',''))
   
    cars_brand_df = pd.DataFrame(brand_cars_info)
