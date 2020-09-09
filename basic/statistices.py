import statistics
list_number=[2,9,11,12,15,20,28,70,10,13,60]
x=statistics.mean(list_number)
y=statistics.variance(list_number)
z=statistics.median(list_number)
w=statistics.stdev(list_number)
print(' mean: ',x,'\n','variance: ',y,'\n','median: ',z,'\n','stdev',w)