data=[]
count=0
sum=0
with open ('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count+=1
        sum+=len(line)
        if count %1000==0:
            print(count)
avg=sum/count       
print('檔案讀取完了，總共有',len(data),'筆資料')
print('留言的平均長度為',avg)
new=[]
for d in data:
    if len(d) <100:
        new.append(d)
print('一共有',len(new),'筆留言長度小於100')