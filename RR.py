b_time = []
a_time = []
r = []
time = 0
r_time = 0
q_time = 0
wait_time = 0
ta_time = 0
flag = 0
count = 0



print "Number of processes ? "
num = input()
r_time = num

for x in range(num):
	print "Process P",(x+1)
	print "Arrival Time: "
	a_time.append(input())
	print "Burst Time: "
	b_time.append(input())
	r.append(burst[x])

print "Enter Quantum Time: \t"
q_time = input()

print "\n\nProcess|\tTurnaround|\tWaiting Time\n"

while r_time!=0:
	if r[count] <= q_time and r[count]>0:
		time = time + r[count]
		r[count] = 0
		flag = 1

	elif r[count]>0:
		r[count] = r[count] - q_time
		time = time + q_time

	if remaining[count]==0 and flag==1:
		remain = remain - 1
		print "P",(count+1),"\t ",time-arrival[count],"\t ",time-arrival[count]-burst[count]
		wait_time = wait_time + (time-arrival[count]-burst[count])
		turn_around_time = turn_around_time + (time-arrival[count])
		flag = 0


	if count == num-1:
		count = 0
	elif a_time[count+1] <= time:
		count = count +1
	else:
		count=0


print "\nAverage Waiting Time = " , wait_time/num
print "\nAverage Turnaround Time = " , ta_time/num

