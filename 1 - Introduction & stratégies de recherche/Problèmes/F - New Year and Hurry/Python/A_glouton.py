n, k = map(int, input().split())

max_time = 240-k
c=0
cur_t=0
while ((c < n) and ((c+1)*5+cur_t <= max_time)):
	c+=1;
	cur_t+=5*c;

print(c);

