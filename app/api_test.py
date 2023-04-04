import json
import requests

from helpers.logger import logger


# 1 - Define JSON to get car infos

car_info_json = {
    "codigoTipoVeiculo": "",
    "codigoTabelaReferencia": "",
    "codigoMarca": "",
    "codigoModelo": "",
    "ano": "",
    "codigoTipoCombustivel": "",
    "anoModelo": "",
    "tipoVeiculo": "",
    "tipoConsulta": ""
}

# 2 - Get all car brand

def get_all_car_brands() -> list:
    """Get a list of car Brands"""

    brand_endpoint = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarMarcas'

    brand_payload = {
        "codigoTabelaReferencia": 296,
        "codigoTipoVeiculo": 1
    }

    try:
        get_brands_request = requests.post(
            brand_endpoint,
            data=brand_payload
        )        
        
        if get_brands_request.status_code == 200:
            brands_list = get_brands_request.json()
            return brands_list

        else:
            raise Exception('It was not possible to get all brands!')
        
    except Exception as err:
        logger.error(err)



def get_all_car_models(brand_code: str) -> dict:
    """Get a list of car models from a brand"""

    models_endpoint = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos'

    model_payload = {
        "codigoTabelaReferencia": 296,
        "codigoTipoVeiculo": 1,
        "codigoMarca": brand_code
    }

    try:
        get_models_request = requests.post(
            models_endpoint,
            data=model_payload
        )        
        
        if get_models_request.status_code == 200:
            models = get_models_request.json()
            return models

        else:
            raise Exception(
                'It was not possible to get all models for brand code: ', brand_code
            )
        
    except Exception as err:
        logger.error(err)



def get_car_model_year(brand_code: str, model_code: str) -> list:
    """Get a list of car model and year"""

    year_model_endpoint = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModelo'

    year_model_payload = {
        "codigoTabelaReferencia": 296,
        "codigoTipoVeiculo": 1,
        "codigoMarca": brand_code,
        "codigoModelo": model_code
    }

    try:
        get_year_model_request = requests.post(
            year_model_endpoint,
            data=year_model_payload
        )        
        
        if get_year_model_request.status_code == 200:
            year_model_list = get_year_model_request.json()
            return year_model_list

        else:
            raise Exception(
                'It was not possible to get all models and year for model code: ', model_code
            )
        
    except Exception as err:
        logger.error(err)
 

def get_model_by_year():
    """Get a list of car Brands"""

def get_price_with_all_params():
    """Get a list of car Brands"""



brand_list = get_all_car_brands()
brand_list[0]

models_list = get_all_car_models(brand_list[0].get('Value'))
 