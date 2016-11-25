"""Custom S3 storage backends to store files in subfolders."""
from local_settings import CLOUDFRONT_URL
from storages.backends.s3boto import S3BotoStorage

# MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')
# StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
class StaticRootS3BotoStorage(S3BotoStorage):
    """
    Storage for static files.
    """
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'static'
        super(StaticRootS3BotoStorage, self).__init__(*args, **kwargs)


class MediaRootS3BotoStorage(S3BotoStorage):
    """
    Storage for uploaded media files.
    """
    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        super(MediaRootS3BotoStorage, self).__init__(*args, **kwargs)
