import requests
import urllib3

from helpers.logger import logger


class FipeIntegration:

    def __init__(self):

        self.car_info_json = {
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

    def fipe_endpoint_request(self, endpoint_to_request: str):
        """Request infos from FIPE endpoints"""

        url = "https://veiculos.fipe.org.br/api/veiculos/" + endpoint_to_request

        try:
            get_brands_request = requests.post(
                url,
                data=self.car_info_json
            )        
            
            if get_brands_request.status_code == 200:
                brands_list = get_brands_request.json()
                return brands_list

            else:
                raise Exception(
                    'It was not possible to consult endpoint: ', 
                    url
                )
            
        except Exception as err:
            logger.info('Error: %s', err)
            return 'Error'


    def get_all_car_brands(self) -> list:
        """Get a list of car Brands"""


        brand_endpoint = 'ConsultarMarcas'

        self.car_info_json.update({
            "codigoTabelaReferencia": 296,
            "codigoTipoVeiculo": 1
        })

        return self.fipe_endpoint_request(brand_endpoint)    


    def get_all_car_models(self, brand_code: str) -> dict:
        """Get a list of car models from a brand"""


        models_endpoint = 'ConsultarModelos'

        self.car_info_json.update({
            "codigoMarca": brand_code
        })

        return self.fipe_endpoint_request(models_endpoint) 
    

    def get_car_model_year(self, brand_code: str, model_code: str) -> list:
        """Get a list of car model and year"""


        year_model_endpoint = 'ConsultarAnoModelo'

        self.car_info_json.update({
            "codigoMarca": brand_code,
            "codigoModelo": model_code
        })

        return self.fipe_endpoint_request(year_model_endpoint)
    

    def get_price_with_all_params(self, year_model, year, fuel_type):
        """Get price given all car parameters"""


        price_endpoint = 'ConsultarValorComTodosParametros'

        self.car_info_json.update({
            "ano": year_model,
            "anoModelo": year,
            "tipoVeiculo": 'carro',
            "tipoConsulta": 'tradicional',
            "codigoTipoCombustivel": fuel_type
        })

        return self.fipe_endpoint_request(price_endpoint) 
