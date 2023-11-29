import matplotlib.pyplot as plt
x =[5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y =[99, 86, 87, 88, 100, 86, 103, 87, 94, 78, 77, 85, 86]
plt.scatter(x, y, c =&quot;blue&quot;)
# To show the plot
plt.show()
12.b.
import matplotlib.pyplot as plt
# dataset-1
x1 = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20]
y1 = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10]
# dataset2
x2 = [26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y2 = [26, 34, 90, 33, 38, 20, 56, 2, 47, 15]
plt.scatter(x1, y1, c =&quot;pink&quot;,linewidths = 2,marker =&quot;s&quot;,edgecolor 
=&quot;green&quot;,s = 50)
plt.scatter(x2, y2, c =&quot;yellow&quot;,linewidths = 2,marker =&quot;^&quot;,edgecolor 
=&quot;red&quot;,s = 200)
plt.xlabel(&quot;X-axis&quot;)
plt.ylabel(&quot;Y-axis&quot;)
plt.show()