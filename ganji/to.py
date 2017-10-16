import codecs
with codecs.open('data2.txt','r') as f:
    dates=f.read()
    out='"ipaddr":'+dates
    with codecs.open('data3.txt','a') as d:
        d.write(out)
