import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

s3_client = boto3.client('s3')


for bucket in s3.buckets.all():
    print(bucket.name)

#data = open('cka-ckad-gcp.png', 'rb')
#s3.Bucket('akil-test').put_object(Key='cka.png', Body=data)

response = s3_client.get_object(Bucket="akil-test",Key="akilan.png")

#print(response)

s3.meta.client.download_file('akil-test', 'akilan.png', 'profile.png')