import requests

from helpers.logger import logger

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
        
        if get_year_model_request.status_code == 200: # Refatorar esse código, usar status_code != 200
            year_model_list = get_year_model_request.json()
            return year_model_list

        else:
            raise Exception(
                'It was not possible to get all models and year for model code: ', model_code
            )
        
    except Exception as err:
        logger.error(err)
 

def get_model_by_year(brand_code, model_code, year_model, year):
    """Get a list of car models by year"""

    model_by_year_endpoint = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarModelosAtravesDoAno'

    model_by_year_payload = {
        "codigoTabelaReferencia": 296,
        "codigoTipoVeiculo": 1,
        "codigoMarca": brand_code,
        "codigoModelo": model_code,
        "ano": year_model,
        "anoModelo": year
    }

    try:
        get_model_by_year_request = requests.post(
            model_by_year_endpoint,
            data=model_by_year_payload
        )        
        
        if get_model_by_year_request.status_code == 200: # Refatorar esse código, usar status_code != 200
            models_by_year_list = get_model_by_year_request.json()
            return models_by_year_list

        else:
            raise Exception(
                'It was not possible to get all models BY year for model code: ', model_code
            )
        
    except Exception as err:
        logger.error(err)


def get_price_with_all_params(brand_code, model_code, year_model, year):
    """Get price given all car parameters"""
    price_endpoint = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'

    price_payload = {
        "codigoTabelaReferencia": 296,
        "codigoTipoVeiculo": 1,
        "codigoMarca": brand_code,
        "codigoModelo": model_code,
        "ano": year_model,
        "anoModelo": year,
        "tipoVeiculo": 'carro',
        "tipoConsulta": 'tradicional',
        "codigoTipoCombustivel": 1
    }

    try:
        get_price_request = requests.post(
            price_endpoint,
            data=price_payload
        )        
        
        if get_price_request.status_code == 200: # Refatorar esse código, usar status_code != 200
            car_infos = get_price_request.json()
            return car_infos

        else:
            raise Exception(
                'It was not possible to get car infos for model code: ', model_code
            )
        
    except Exception as err:
        logger.error(err)
