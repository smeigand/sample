import boto3
session = boto3.Session()

session.profile_name

'default'

credentials = session.get_credentials() 
access_key = credentials.access_key
secret_key = credentials.secret_key 
 

token = credentials.token 

print(access_key)
print(secret_key)
print(token)


f = open("creds.aws_creds", "a")
L = ["default \n","aws_access_key_id="+access_key+"\n","aws_secret_access_key="+secret_key+"\n"]
f.writelines(L)
f.close()
