b_time = []
wait = []
ta_time = []
avg_wait = 0
avg_ta = 0

print "Number of Process?"

num = input()

print "Enter Process BT \n"

for i in range(num):
	print "for P [" , (i+1) , "] = "
	b_time.append(input())


wait.append(0)

for i in range(1 ,num):
	wait.append(0)
	for y in range(i):
		wait[i] = wait[i] + b_time[y]


print "\nProcess \tBurst Time\tWaiting Time\tTurnAround Time"

for i in range(num):
	turn_around.append(b_time[i] + wait[i])
	avg_wait = avg_wait + wait[i]
	avg_ta = avg_ta + turn_around[i]
	print "\nP[",(i+1),"]\t\t",b_time[i],"\t\t",wait[i],"\t\t",turn_around[i]



avg_wait = avg_wait / num
avg_ta = avg_ta / num

print "\n Average Waiting Time : " , avg_wait
print "\n Average Turn Around Time : " , avg_ta



