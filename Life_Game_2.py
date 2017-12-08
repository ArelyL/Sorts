s="""0000000000000000
0000000000000000
0000111111110000
0000101111010000
0000111111110000
0000000000000000
0000000000000000"""
arr=s.split('\n')
print("%s\n%s\n%s\n%s\n%s\n%s\n%s"%(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6]))
print('\n\n\n\n\n')
n=6
m=15
for k in range(0,3):
    for i in range(0,n):
        for j in range(0,m):
            bandera=0
            l=list(arr[i])
            if i==0 and j==0:
                bandera=int(arr[i][j+1])+int(arr[i+1][j])+int(arr[i+1][j+1])
                if arr[i][j]=='0' and bandera==3:
                    l[j]='1'
                    arr[i]="".join(l)
                if arr[i][j]=='1' and (bandera<2 or bandera>3):                    
                    l=list(arr[i])
                    l[j]='0'
                    arr[i]="".join(l)
                   
            if i==n and j==0:
                bandera=int(arr[i][j+1])+int(arr[i-1][j])+int(arr[i-1][j+1])
                if arr[i][j]=='0' and bandera==3:
                    l[j]='1'
                    arr[i]="".join(l)                    
                if arr[i][j]=='1' and (bandera<2 or bandera>3):
                    l[j]='0'
                    arr[i]="".join(l)
                    
            if i==0 and j==m:
                bandera=int(arr[i][j-1])+int(arr[i+1][j])+int(arr[i+1][j-1])
                if arr[i][j]=='0' and bandera==3:
                    l[j]='1'
                    arr[i]="".join(l)                    
                if arr[i][j]=='1' and (bandera<2 or bandera>3):
                    l[j]='0'
                    arr[i]="".join(l)
                    
            if i==n and j==m:
                bandera=int(arr[i][j-1])+int(arr[i-1][j])+int(arr[i-1][j-1])
                if arr[i][j]=='0' and bandera==3:
                    l[j]='1'
                    arr[i]="".join(l)                    
                if arr[i][j]=='1' and (bandera<2 or bandera>3):
                    l[j]='0'
                    arr[i]="".join(l)
                    
            if i==0 and (j!=0 and j!=m):
                bandera=int(arr[i][j+1])+int(arr[i][j-1])+int(arr[i+1][j-1])+int(arr[i+1][j])+int(arr[i+1][j+1])
                if arr[i][j]=='0' and bandera==3:
                    l[j]='1'
                    arr[i]="".join(l)
                    
                if arr[i][j]=='1' and (bandera<2 or bandera>3):
                    l[j]='0'
                    arr[i]="".join(l)
                    
            if i==n and (j!=0 and j!=m):
                bandera=int(arr[i][j+1])+int(arr[i][j-1])+int(arr[i-1][j-1])+int(arr[i-1][j])+int(arr[i-1][j+1])
                if arr[i][j]=='0' and bandera==3:
                    l[j]='1'
                    arr[i]="".join(l)
                   
                if arr[i][j]=='1' and (bandera<2 or bandera>3):
                    l[j]='0'
                    arr[i]="".join(l)
                    
            if (i>0 and i<m) and (j>0 and j<m):
                bandera=int(arr[i][j+1])+int(arr[i][j-1])+int(arr[i-1][j-1])+int(arr[i-1][j])+int(arr[i-1][j+1])+int(arr[i+1][j-1])+int(arr[i+1][j])+int(arr[i+1][j+1])
                if arr[i][j]=='0' and bandera==3:
                    l[j]='1'
                    arr[i]="".join(l)
                    
                if arr[i][j]=='1' and (bandera<2 or bandera>3):
                    l[j]='0'
                    arr[i]="".join(l)
                    
    print("%s\n%s\n%s\n%s\n%s\n%s\n%s"%(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6]))
    print('\n\n\n\n\n')
