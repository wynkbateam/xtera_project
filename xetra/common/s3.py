# Connector to deal with S3 Buckets

import os
import boto3

class s3BucketConnector():
    def __init__(self,access_key: str, secret_key: str, end_point_url: str, bucket: str):
        self.endpoint_url =end_point_url
        self.session = boto3.Session()






