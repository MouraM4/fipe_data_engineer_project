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

def get_all_car_brands():
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


def get_all_car_models():
    """Get a list of car Brands"""

def get_car_model_year():
    """Get a list of car Brands"""
 

def get_model_by_year():
    """Get a list of car Brands"""

def get_price_with_all_params():
    """Get a list of car Brands"""
 