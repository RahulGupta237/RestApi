stg="Rahul Gupta"
output=""
for i in stg:
    if i=="a":
        i="d"
        output+=i
    else:
        output+=i
print(output)
list2=[1,1,1,2,2,3,5,7,9,0,0,0,0,0,6,6,4]
out_put={}

setlist=set(list2)
for i in setlist:
    
    if list2.count(i)>1:
       out_put[i]=list2.count(i)
print(out_put)
 
        


