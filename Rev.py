df = open('NSE-TCS.csv','r')
rev = open('Rev.csv','a+')

app = []
for lines in df:
    app.append(lines)

rev.write(app[0])

for i in range(len(app)-1,0,-1):
    rev.write(app[i])
    
rev.close()
df.close()
