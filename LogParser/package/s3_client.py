import boto3
from package.config import AWS_CONFIG
import os


class S3Worker(object):

    def __init__(self, obj=None, source_file=None, bucket=AWS_CONFIG['bucket']):

        self.obj = obj
        self.source_file = source_file
        self.local_path = os.getcwd() + f'/tmp'
        self.bucket = bucket

    def download_file(self):

        target_file = self.local_path + "/" + self.source_file
        s3 = boto3.resource('s3')
        s3.Object(self.bucket, self.source_file).download_file(target_file)

        return target_file

