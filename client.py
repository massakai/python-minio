import logging

import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)


def main():
    endpoint_url = 'http://127.0.0.1:9000'
    access_key_id = 'hoge'
    secret_access_key = 'fugafuga'

    s3 = boto3.resource(
        service_name='s3',
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key)
    try:
        # バケットを作成する
        bucket = s3.create_bucket(Bucket='images')
        logging.info(f'Bucket "images" was created.')
    except ClientError as e:
        if e.response['Error']['Code'] in (
                'BucketAlreadyExists', 'BucketAlreadyOwnedByYou'):
            logging.info(f'Bucket "images" already exists.')
            bucket = s3.Bucket('images')
        else:
            logging.exception('Unknown exception.')
            raise

    # 画像をアップロードする
    for filename in ('cat01.png', 'cat02.png'):
        bucket.upload_file(f'images/{filename}', filename)
        logging.info(f'Object "{filename}" was uploaded to bucket "images".')

    # 確認
    for obj in bucket.objects.filter():
        logging.info(f'Object "{obj.key}" exists in bucket "{obj.bucket_name}".')


if __name__ == '__main__':
    main()
