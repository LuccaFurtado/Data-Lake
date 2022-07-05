import os
import pandas as pd
import logging
from botocore.exceptions import ClientError
from tqdm import tqdm


def save_csv_s3(filename, bucket_name,s3_client, object_name=None):
    if object_name is None:
        object_name = filename
    try:
        response = s3_client.upload_file(filename, bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def save_files_path_s3(path:str, format:str, bucket_name:str, path_name:str, s3_client, complement:str=None):
    for file in tqdm(os.listdir(path)):
        if file.endswith('.'+format):
            save_name = f"{path_name}/{file}"
            if complement is not None:
                save_name = save_name + "/" + complement
            save_csv_s3(os.path.join(path,file), bucket_name=bucket_name, s3_client=s3_client ,object_name=save_name)






