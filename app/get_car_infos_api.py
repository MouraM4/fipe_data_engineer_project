import json
import re
import ujson

from helpers.fipe_functions import FipeIntegration
from helpers.kinesis_aws import AWSFirehose
from helpers.logger import logger


if __name__ == '__main__':

    aws_firehose = AWSFirehose()
    fipe_integration = FipeIntegration()

    # Get all car brand
    all_brand_list = fipe_integration.get_all_car_brands()
    brand_cars_info = []
    batch_size = 100

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
                
                if car_info and not isinstance(car_info, str) and len(brand_cars_info) < batch_size:
                    brand_cars_info.append(car_info)
                    logger.info('\n%s\n', car_info)

                elif len(brand_cars_info) >= batch_size:
                    print(len(brand_cars_info))
                    regex_pattern = r'(?:\[|\])|},\s*'
                    output = re.sub(regex_pattern, lambda x: '}' if x.group() == '},' else '', ujson.dumps(brand_cars_info))
                    aws_firehose.kinesis_firehose_put_record(output)
                    brand_cars_info = []

                else:
                    logger.info('None Value')
