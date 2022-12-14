import math
n, k = map(int, input().split())

max_time = math.floor((240-k)/5)
c=0
d=0
f=n
m=0
while d <= f:
	m = math.floor((f+d)/2);
	c = math.ceil((m*(m+1)/2));
	if c < max_time:
		d=m+1;
	elif c==max_time:
		break;
	else:
		f=m-1;
m = (f+d)/2;
print(math.floor(m));


