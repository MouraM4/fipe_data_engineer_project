import json
import requests


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

def get_all_car_brand():
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
            get_brands_request.json()

        else:
            raise Exception('It was not possible to get all brands!')
        
    except Exception as err:
        print(err)
 