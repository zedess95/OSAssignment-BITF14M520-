total = 0
sort = 0
avg_wait = 0
avg_ta = 0
b_time = []
p = []
wait = []
ta_time = []
priority = []


print "Number of process? "
num = input()


for x in range(num):
	print "For Process P",(x+1)
	print "Burst Time: "
	b_time.append(input())
	print "Priority: "
	priority.append(input())
	process.append(x+1)
	
for y in range(1, num):
	wait.append(0)
	for z in range(y):
		wait[y] = wait[y] + b_time[z]

	total = total + wait[y]

avg_wait = total / num
total = 0

for y in range(num):
	sort=y
	for z in range((y+1) , num):
		if priority[z] < priority[sort]:
			sort = z

	priority[y] , priority[sort] = priority[sort] , priority[y]
	b_time[y] , b_time[sort] = b_time[sort] , b_time[y]
	p[y] , p[sort] = p[sort] , p[y]

wait.append(0)



print "\nProcess \tBurst Time \tWaiting Time \tTurnAround Time"

for a in range(num):
	ta_time.append(b_time[a] + wait[a])
	total = total + ta_time[a]
	print "\nP", p[a], "\t\t", b_time[a], "\t\t", wait[a], "\t\t", ta_time[a]

avg_ta = total/num
print "\n\nAverage Waiting Time = " , avg_wait
print "\nAverage Turn Around Time = " , avg_ta

