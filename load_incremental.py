
import os
from os import getenv
from dotenv import load_dotenv
import boto3
from utils import save_files_path_s3, save_csv_s3



s3_client = boto3.client(
    's3',
    aws_access_key_id=getenv('ID') ,
    aws_secret_access_key=getenv('KEY'),
    )

save_files_path_s3('data/incremental','csv', 'csgo-datalake', 'raw/cs/inc' , s3_client)


