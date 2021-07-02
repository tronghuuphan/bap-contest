def zigzag(string, n):
    if n==1:
        return string
    list_s = list(string)
    thang = []
    cheo = []
    dem = 0
    for i in range(0,len(list_s),n-1):
        if dem==0:
            thang.extend(list_s[i:i+n])
            dem=1
        else:
            cheo.extend(['']+list_s[i+1:i+n-1] [::-1]+[''])
            dem=0
    
    if len(cheo)>len(thang):
        thang.extend(['']*(len(cheo)-len(thang)))
    elif len(cheo)<len(thang):
        cheo.extend(['']*(len(thang)-len(cheo)))
    out_zip = [i for i in zip(thang,cheo)]
    out = []
    for i in range(n):
        for j in range(i, len(out_zip),n):
            out.append(out_zip[j][0])
            out.append(out_zip[j][1])
    return ''.join(out)

if __name__ == '__main__':
    string = 'BEADVANCEDPARTNER'
    n = 3
    print('Result: ', zigzag(string,n))
