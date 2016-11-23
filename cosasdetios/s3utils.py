"""Custom S3 storage backends to store files in subfolders."""
from local_settings import S3_URL
from storages.backends.s3boto import S3BotoStorage

MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')
StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
