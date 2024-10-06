#Number Format
print('Number |Square\t|Cube\t |Quad')
for i in range(1,11):
    print(' {0:2d}\t{1:3d}\t{2:4d}\t{3:5d}'.format(i, i*i, i*i*i, i*i*i*i))
#   print('{0:02}:{1:02}:{2:02}'.format(hh,mm,ss),end='\r')