import yaml

d1=[{'host':'192.168.0.1',
    'port':'22',
    'user':'root',
    'password':'redhat'}]

with open("/mnt/Data2/prod.yaml","w") as f:
    yaml.safe_dump(d1,f)


