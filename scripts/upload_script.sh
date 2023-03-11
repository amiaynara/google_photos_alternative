# upload files to s3 deep storage
aws s3 sync /Users/amiaynarayan/Projects/photos/actual_images/ s3://amiay-photos/test/ --storage-class DEEP_ARCHIVE

# upload thumbnails
aws s3 sync /Users/amiaynarayan/Projects/photos/thumbnails/ s3://amiay-photos/test/
