# python-minio

## MinIOサーバーの起動

```shell
$ docker run -p 9000:9000 
    -e MINIO_ACCESS_KEY=hoge \
    -e MINIO_SECRET_KEY=fuga \
    minio/minio server /data

 You are running an older version of MinIO released 5 months ago
 Update: Run `mc admin update`


Attempting encryption of all config, IAM users and policies on MinIO backend
Endpoint:  http://172.17.0.2:9000  http://127.0.0.1:9000

Browser Access:
   http://172.17.0.2:9000  http://127.0.0.1:9000

Object API (Amazon S3 compatible):
   Go:         https://docs.min.io/docs/golang-client-quickstart-guide
   Java:       https://docs.min.io/docs/java-client-quickstart-guide
   Python:     https://docs.min.io/docs/python-client-quickstart-guide
   JavaScript: https://docs.min.io/docs/javascript-client-quickstart-guide
   .NET:       https://docs.min.io/docs/dotnet-client-quickstart-guide
```

## 画像について

images配下の画像ファイルは[いらすとや](https://www.irasutoya.com/)からお借りしています。
