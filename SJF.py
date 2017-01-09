b_time = []
wait = []
ta_time = []
p = []
avg_wait =0
avg_ta =0
pos =0
total = 0

print "Number of process? "
num = input()

print "Enter Burst Time: "
for x in range(num):
	print "for P" , (x+1)
	b_time.append(input())
	p.append(x+1)

for x in range(1, num):
	wait.append(0)
	for y in range(x):
		wait[x] = wait[x] + b_time[y]

	total = total + wait[x]

avg_wait = total / num
total = 0

for i in range(num):
	pos=i
	for j in range((i+1) , num):
		if b_time[j] < b_time[pos]:
			pos = j

	
	b_time[i] , b_time[pos] = b_time[pos] , b_time[i]
	p[i] , p[pos] = p[pos] , p[i]


wait.append(0)


print "\np \tBurst Time \tWaiting Time \tTurnAround Time"

for x in range(num):
	ta_time.append(b_time[x] + wait[x])
	total = total + ta_time[x]
	print "\nP", p[x], "\t\t", b_time[x], "\t\t", wait[x], "\t\t", ta_time[x]

avg_ta = total/num
print "\n\nAverage Waiting Time = " , avg_wait
print "\nAverage Turn Around Time = " , avg_ta


