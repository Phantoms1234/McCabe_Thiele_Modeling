import numpy as np
import matplotlib.pyplot as plt

# input distillation parameters
#xf=float(input("mole fraction of light component in feed"))
#xd=float(input("mole fraction of light component in overhead liquid"))
#xb=float(input("mole fraction of light component in bottom liquid"))
#R=float(input("Reflux ratio"))
#q=float(input("heat load of feed"))
#a=float(input("average relative volatility "))


xf=0.6
xd=0.97
xb=0.03
R=2
a=2.5
q=0

#equillibrium line
x=np.linspace(0,1,101)
eq=(a*x)/(1+x*(a-1))


# 45 degree diagonal
diagonal=x

# rectifying section line
rec=(R / (R + 1)) * x + (xd / (R + 1))

# feed line and point of intersection of feed line and rectifying line (since the logic of both is connected)

if q==1:
	x_feed=[xf,xf]
	q_line=[0,1]

	# this is the intersection the point y=xb and the point of intersection of the of the feed and rectifying line
	xint=xf
	yint=(R / (R + 1)) * xf + (xd / (R + 1))

else:
	x_feed=x
	q_line=(q / (q - 1)) * x - (xf / (q - 1))
	# this is the intersection the point y=xb and the point of intersection of the of the feed and rectifying line
	xint= (xf/(q-1)+xd/(R+1))/(q/(q-1)-R/(R+1))
	yint=R/(R+1)*xint + xd/(R+1)


# stripping section line
strp=((yint-xb)/(xint-xb))*(x-xb) + xb



# stepping off numer of stages 
def stepping_off():
	stages=0
	feed_stage=1
	# defining a list to store the x and y coordinates of the stages
	x_coordinates=[xd]
	y_coordinates=[xd]
	# creating a variable to help keep track of the current x coordinate 
	x_current=x_coordinates[-1]
	y_current=y_coordinates[-1]

	while x_current>xb:
		stages=stages+1
		x_current=y_coordinates[-1]/(a-y_coordinates[-1]*(a-1))
		x_coordinates.append(x_current)
		y_coordinates.append(y_current)


		if x_current>xint:
			y_current=(R/(R+1))*x_current + (1/(R+1))*xd
			y_coordinates.append(y_current)
			x_coordinates.append(x_current)
			feed_stage=feed_stage+1


		elif x_current<xint:
			y_current=((yint-xb)/(xint-xb))*(x_current-xb) + xb
			y_coordinates.append(y_current)
			x_coordinates.append(x_current)

	return x_coordinates,y_coordinates,stages,feed_stage

x_coordinates,y_coordinates,stages,feed_stage =stepping_off()


def minimum_stages():
	min_stages=0
	x_coord=[xd]
	y_coord=[xd]

	x_current=x_coord[-1]
	y_current=y_coord[-1]

	while x_current>xb:
		min_stages+=1
		x_current=y_coord[-1]/(a-y_coord[-1]*(a-1))
		x_coord.append(x_current)
		y_coord.append(y_current)
		y_current=x_current
		y_coord.append(y_current)
		x_coord.append(x_current)

	return min_stages, x_coord,y_coord


min_stages, x_coord,y_coord=minimum_stages()





print("The minimum number of trays is", min_stages)
print("The number of trays is",stages)
print("The position of the feed tray is",feed_stage)


plt.figure(figsize=(10, 8))
plt.plot(x, eq, label='Equilibrium Line', color='blue')
plt.plot(x, diagonal, label='45-degree Diagonal', linestyle='--', color='gray')
plt.plot(x, rec, label='Rectifying Section Line', color='green')
plt.plot(x_feed, q_line, label='Feed Line', color='purple', linestyle='-.')
plt.plot(x, strp, label='Stripping Section Line', color='red')

# Plot the intersection point
plt.plot(xint, yint, 'o', color='orange', markersize=8, label='Intersection Point')

# Plot the stepping-off stages
plt.plot(x_coordinates, y_coordinates, 'o-', color='black', markersize=4, label='Stepping Off Stages')

plt.plot(x_coord, y_coord, 'o-', color='yellow', markersize=1, label='minimum stages')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x (mole fraction liquid)')
plt.ylabel('y (mole fraction vapor)')
plt.title('McCabe-Thiele Diagram')
plt.legend()
plt.grid(True)
plt.show()












