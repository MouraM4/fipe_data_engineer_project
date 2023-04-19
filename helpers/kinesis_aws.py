import boto3

from helpers.logger import logger


class AWSFirehose:

    def __init__(self):
        self.client = boto3.client('firehose', region_name='us-east-1')
    

    def kinesis_firehose_put_record(self, data):
        
        """Send records in batch to kinesis firehose"""
        
        try:

            response = self.client.put_record(
                DeliveryStreamName='kinesis-firehose-fipe-project',
                Record={
                    'Data': data
                }
            )

            logger.info('Data uploaded into firehose')

        except Exception as err:
            logger.error(err)
    