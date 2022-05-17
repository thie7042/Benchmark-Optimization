import random
import math
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
import os
from openpyxl import workbook
from openpyxl import load_workbook
import time



# ------------------------------------------------------------------------------
# TO CUSTOMIZE THIS PSO CODE TO SOLVE UNCONSTRAINED OPTIMIZATION PROBLEMS, CHANGE THE PARAMETERS IN THIS SECTION ONLY:
# THE FOLLOWING PARAMETERS MUST BE CHANGED.


def objective_function(X):
    print(X)
    #capture = [X[0], X[1], X[2], X[3]]


    f = open("C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/parameters" + str(objective_function.paramfile) + ".txt",
             "w")
    f.write(
        str(X[0]) + "," + str(X[1]) + ","+str(X[2]) + "," + str(X[3]) + ","+ str(X[4]) + "," + str(X[5]) + ","+ str(X[6]) + ","+ str(X[7]) + ","
        + str(X[8]) + ","+ str(X[9])
        + "," + "newdata")
    f.close()






    filepath = 'C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Output/' + 'abaqus_output_def'+ str(objective_function.paramfile) + '.txt'
    print(filepath)

    while True:
        time.sleep(0.5)

        try:
            file = open(filepath, 'r')
            data = file.read()
            data = data.split(' ')
            data = list(filter(None, data))
            vals = data[-9:-1]
            print("Opening File")
        except:
            print('File has not been created. Waiting for analysis. Curent Sol: ' + str(objective_function.paramfile))

            continue

        break
    print('File found!')

    vals = [float(i) for i in vals]
    print(vals)

    print("Max deflection: " , np.max(vals))
    max_def = np.max(vals)

    # This fitness function value is not correct (we want to minimize the overall weight of the structure)
    diag_l = math.sqrt(9.14**2 + 9.14**2)
    fitness =  (X[0]*9.14 + X[1]*9.14 + X[2]*diag_l + X[3]*diag_l  + X[4]*9.14 + X[5]*diag_l  + X[6]*diag_l  + X[7]*9.14 + X[8]*9.14 + X[9]*9.14) * 2770

    # I need to rethink how to handle the deflection constraint. This is a crude method to just get it working
    if max_def > 0.0508:
        fitness += 100000*max_def
        print("Bad solution: Fitness = ", fitness)
    else:
        print("Fitness =", fitness)

    #print("_____________________")
    #print(X)
    #print("_____________________")

    #A = 10
    #y = A * 2 + sum([(x ** 2 - A * np.cos(2 * math.pi * x)) for x in X])

    print("Fitness: ", fitness)



    # Writing params and fitness
    t_file = open("C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Optimization_Output/PSO/result_" + str(objective_function.paramfile) +".txt", 'w')
    t_file.write(str(X) + "," + str(max_def) + "," + str(fitness))
    t_file.close()

    objective_function.paramfile += 1
    return fitness

objective_function.paramfile = 1


bounds = [(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226),(0.0000645, 0.0226)]  # upper and lower bounds of variables
nv = 10  # number of variables
mm = -1  # if minimization problem, mm = -1; if maximization problem, mm = 1

# THE FOLLOWING PARAMETERS ARE OPTIONAL
particle_size = 50 #50  # number of particles
iterations = 15 #100  # max number of iterations
w = 0.75  # inertia constant
c1 = 1  # cognative constant
c2 = 2  # social constant
# END OF THE CUSTOMIZATION SECTION
# ------------------------------------------------------------------------------
# Visualization
"""fig = plt.figure()
ax = fig.add_subplot()
fig.show()"""


# ------------------------------------------------
# Writing the number of iterations to file
t_file = open('C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/number_of_sols.txt','w')
t_file.write(str(particle_size*iterations)+ " " +"PSO")
t_file.close()

# ------------------------------------------------
# Write termination function
t_file = open('C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/termination.txt','w')
t_file.write("False")
t_file.close()
# ------------------------------------------------



# ------------------------------------------------------------------------------
class Particle:
    def __init__(self, bounds):
        self.particle_position = []  # particle position
        self.particle_velocity = []  # particle velocity
        self.local_best_particle_position = []  # best position of the particle
        self.fitness_local_best_particle_position = initial_fitness  # initial objective function value of the best particle position
        self.fitness_particle_position = initial_fitness  # objective function value of the particle position

        for i in range(nv):
            self.particle_position.append(
                random.uniform(bounds[i][0], bounds[i][1]))  # generate random initial position
            self.particle_velocity.append(random.uniform(-1, 1))  # generate random initial velocity

    def evaluate(self, objective_function):
        self.fitness_particle_position = objective_function(self.particle_position)
        if mm == -1:
            if self.fitness_particle_position < self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position # Update the local best
                self.fitness_local_best_particle_position = self.fitness_particle_position # Update the fitness of the local best
        if mm == 1:
            if self.fitness_particle_position > self.fitness_local_best_particle_position:
                self.local_best_particle_position = self.particle_position  # Update the local best
                self.fitness_local_best_particle_position = self.fitness_particle_position # Update the fitness of the local best

    def update_velocity(self, global_best_particle_position):
        for i in range(nv):
            r1 = random.random()
            r2 = random.random()

            cognitive_velocity = c1 * r1 * (self.local_best_particle_position[i] - self.particle_position[i])
            social_velocity = c2 * r2 *(global_best_particle_position[i] - self.particle_position[i])
            self.particle_velocity[i] = w * self.particle_velocity[i] + cognitive_velocity + social_velocity

    def update_position(self, bounds):
        for i in range(nv):
            self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]

            # Check and repair to satisfy the upper bounds
            if self.particle_position[i] > bounds[i][1]:
                self.particle_position[i] = bounds[i][1]
            # Check and repair to satisfy the upper bounds
            if self.particle_position[i] < bounds[i][0]:
                self.particle_position[i] = bounds[i][0]



def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# ------------------------------------------------
if mm == -1:
    initial_fitness = float("inf") # for minimization problem
if mm == 1:
    initial_fitness = -float("inf") # for maximization problem
# ------------------------------------------------

fitness_global_best_particle_position = initial_fitness
global_best_particle_position = []
swarm_particle = []

for i in range(particle_size):
    swarm_particle.append(Particle(bounds))

A = []


for i in range(iterations):

    objective_function.gen = i

    """createFolder('C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Optimization_Output/PSO/Generation_' + str(i) +'/')"""

    for j in range(particle_size):

        objective_function.counter = j

        """filepath = "C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Optimization_Output/PSO/Generation_" + str(i) + '/Solution_' + str(j) + '.xlsx'

        #print(swarm_particle[j].particle_position[1])

        workbook = xlsxwriter.Workbook(filepath)

        # The workbook object is then used to add new
        # worksheet via the add_worksheet() method.
        worksheet = workbook.add_worksheet()

        # Use the worksheet object to write
        # data via the write() method.
        worksheet.write('A1', 'Area 1')
        worksheet.write('A2',  swarm_particle[j].particle_position[0])

        worksheet.write('B1', 'Area 2')
        worksheet.write('B2', swarm_particle[j].particle_position[1])

        worksheet.write('C1', 'Area 3')
        worksheet.write('C2', swarm_particle[j].particle_position[2])

        worksheet.write('D1', 'Area 4')
        worksheet.write('D2', swarm_particle[j].particle_position[3])

        worksheet.write('E1', 'Area 5')
        worksheet.write('E2', swarm_particle[j].particle_position[4])

        worksheet.write('F1', 'Area 6')
        worksheet.write('F2', swarm_particle[j].particle_position[5])

        worksheet.write('G1', 'Area 7')
        worksheet.write('G2', swarm_particle[j].particle_position[6])

        worksheet.write('H1', 'Area 8')
        worksheet.write('H2', swarm_particle[j].particle_position[7])

        worksheet.write('I1', 'Area 9')
        worksheet.write('I2', swarm_particle[j].particle_position[8])

        worksheet.write('J1', 'Area 10')
        worksheet.write('J2', swarm_particle[j].particle_position[9])

        workbook.close()"""

        # Write to file

        # Change parameter file - Update input parameters






        swarm_particle[j].evaluate(objective_function)

        if mm == -1:
            if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:
                global_best_particle_position = list(swarm_particle[j].particle_position)
                fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)

        if mm == 1:
            if swarm_particle[j].fitness_particle_position > fitness_global_best_particle_position:
                global_best_particle_position = list(swarm_particle[j].particle_position)
                fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)

    for j in range(particle_size):
        swarm_particle[j].update_velocity(global_best_particle_position)
        swarm_particle[j].update_position(bounds)






    A.append(fitness_global_best_particle_position) # Record the best fitness

    # Visualization
    """ax.plot(A, color = 'r')
    fig.canvas.draw()
    ax.set_xlim(left=max(0,i-iterations), right = i + 3)"""

    print("Iteration: " , i)

print("Optimal solution: ", global_best_particle_position)
print("Objective function value: ", fitness_global_best_particle_position)
#plt.show()


# ------------------------------------------------
# Write termination function
t_file = open('C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/termination.txt','w')
t_file.write("True")
t_file.close()
# ------------------------------------------------


# ------------------------------------------------
# Write optimal solution to file
filepath_f = "C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Optimization_Output/PSO/Final.txt"

t_file = open(filepath_f,'w')
t_file.write("Optimal solution: " + str(global_best_particle_position) + "Objective function value: " + str(fitness_global_best_particle_position))
t_file.close()

