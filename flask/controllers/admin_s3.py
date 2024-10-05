import boto3
from keys import ACCESS_KEY, SECRET_KEY

bucket_name = "bucket-project-cloud"
def connectionS3():
    session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    print("succesfull connection to s3")
    return session_s3

def save_file(photo, ID):
    photo_name = ID + ".jpg"
    photo_path = "/tmp/" + photo_name
    photo.save(photo_path)
    print("Photo saved")
    return photo_path, photo_name

def upload_file(photo_path, photo_name):
    session_s3 = connectionS3()
    session_s3.meta.client.upload_file(photo_path, bucket_name, photo_name)
    print("Uploaded photo")
    
    
def get_files():
    session_s3 = connectionS3()
    bucket_project = session_s3.Bucket(bucket_name)
    all_obj = bucket_project.objects.all()
    for obj in all_obj:
        print(obj.key)

get_files()