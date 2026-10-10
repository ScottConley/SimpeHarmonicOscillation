#imports
import numpy as np
import matplotlib.pyplot as plt

#params
k = 1.0
m = 10.0

#we need to work with time steps since oscillation occurs over time
dt = 0.01 #time step, delta t
T_MAX = 20 #time max

#to make things easier, we'll consolidate our number of steps here.
#remember that arrays/computers generally start counting from 0
n_steps = int(T_MAX/dt) + 1 #This will give us 1000 "time steps" + 1 so we can access the last element of the array


#arrays
#create "buckets" that can collect information over time
#we are concerned with v(t) and x(t), that is, velocity and position over time.

#we'll start with time. In numpy we need a "linear array" since time moves linearly
t_array = np.linspace(0, T_MAX, n_steps)

#now we need two "empty buckets" to store velocity and position at each point of time
#numpy provides a style of array that gives us an "empty bucket" which we can fill with our data points
#remember that we still need to have the same number of elements in these arrays that we have "time steps"
#zeros is going to give us a "bucket" filled with n_steps number of "zeros". literally 1001 0s.
#this will be useful for us later because at time step 0, our amplitude will be 1.
#this is where we'll set out initial conditions. x = 1.0 (fully stretched spring) and v = 0.0 (starting from rest)

x_array = np.zeros(n_steps)
v_array = np.zeros(n_steps)

#we'll go ahead and set the initial conditions
#if we set them inside the upcoming for loop, we'll end up going back to our initial conditions
#every time the loop iterates - the spring will go back to full stretch at every iteration

#note that even though we know the v_array will start at 0.0, we'll still set it here
#this will make the physics more visible and prevents confusion later

#We'll also set it here so that the loop has starting conditions at time = 0
x_array[0] = 1.0
v_array[0] = 0.0

#time loop
#i is going to be a variable which handles the step count for us
#a for loop will start the count at 0, but the for loop will write to the index of i+1 when it executes
#so in order to access the last n_step, we'll need to subtract 1

#essentially, at i = 0, the loop writes 1, which is the first new time step
#time step = 0 was already set by the initial conditions

#Here's the physics "recipe" we'll be using per step:
#1. Where is the mass? -> x_array[i]
#2. What's the force that acts on it? F = -kx (Hooke's Law)
#3. How hard is the force pulling on it? -> F = ma; ma = -kx; a = -(k/m) * x
#4. Update the velocity and then the position

#note, we'll be using Euler's method of Simple Harmonic Motion
#They are simple differential equations meant to model harmonic motion over time
#They look like this:
#v_new = v_old - (k/m) * x * dt
#x_new = x_old + (k/m) * x * dt

#note that we've set -(k/m) * x = a
#our formulas in the loop will then look like...
#v_new = v_old + a * dt
#x_new = x_old + v_new * dt

for i in range(n_steps - 1):
    a = -(k/m) * x_array[i] #F = ma; ma = -kx; a = -(k/m) * x
    v_array[i+1] = v_array[i] + a * dt # v_new = v_old + a * dt
    x_array[i+1] = x_array[i] + v_array[i+1] * dt #x_new uses the updated velocity

#TODO: add verification method
#TODO: upgrade to velocity verlet oscillation mathematical model for animation upgrade

#plots

#These are simply nice colors that I like which are easy on the eyes

colors = {
    "axes.facecolor": "#1e1e2e",
    "figure.facecolor": "#1e1e2e",
    "text.color": "#cdd6f4",
    "axes.labelcolor": "#cdd6f4",
    "lines.color": "#89b4fa",
    "xtick.color": "#cdd6f4",
    "ytick.color": "#cdd6f4",
}
for key, value in colors.items():
    plt.rcParams[key] = value

#here, we're using matplotlib to make the graphs.
#most software/data people will simply grab a template from the internet and paste it into their code
#don't worry too much about what we're doing here, just now that we're setting up graphs.

#this first block is going to set a single graph to show velocity and position together

plt.figure(figsize=(10,6))

plt.plot(t_array, x_array, label="Position with respect to time x(t)", linewidth=2)
plt.plot(t_array, v_array, label="Velocity with respect to time v(t)", linewidth=2)
plt.axhline(0, color="grey", linestyle="--", linewidth=0.8)

plt.title("Simple Harmonic Oscillation")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

plt.legend()
plt.grid(True, alpha=0.3)

#this next block is going to set up a pair of graphs to show velocity and position separately

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 7))

ax1.plot(t_array, x_array, color='#89b4fa', linewidth=2)
ax1.set_ylabel('Position x (m)')
ax1.set_title('Simple Harmonic Oscillator')
ax1.grid(True, alpha=0.3)
ax1.axhline(0, color='gray', linestyle='--', linewidth=0.8)

ax2.plot(t_array, v_array, color='#fab387', linewidth=2)
ax2.set_ylabel('Velocity v (m/s)')
ax2.set_xlabel('Time (s)')
ax2.grid(True, alpha=0.3)
ax2.axhline(0, color='gray', linestyle='--', linewidth=0.8)

plt.tight_layout()

plt.show()