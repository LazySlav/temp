X = [float(i) for i in input().split()]
X.append(X[0])
X.append(X[1])
Y = [float(i) for i in input().split()]
Y.append(Y[0])
Y.append(Y[1])
cd = list(zip(X,Y))
tx,ty = [float(i) for i in input().split()]
for k,(x,y) in enumerate(cd):
    if k-3<=len(cd):
        x1,y1 = cd[k+1][0],cd[k+1][1]
        k = (y1-y)/(x1-x)
        b = y-k*x
        x2,y2 = cd[int(k+2)][0],cd[int(k+2)][1]
        print((y2-k*x2-b),(ty-k*tx-b))
        if a:=(y2-k*x2-b)*(ty-k*tx-b)>0:
            continue
        print(0)
        break
    else:
        print(1)
