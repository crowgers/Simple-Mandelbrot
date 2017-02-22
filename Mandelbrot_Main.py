# Python code to compute, print and ave a png file of madnelbrot set at specified points
# Grid_size defines how large array.  Sticking with uniform grid but if variable scaling is desired split into
# grid_size_x & grid_size_y
# The tolerance is the number of times a specific point will be interated on to determine if it is in the set.
# x_min, x_max, y_min, y_max are boundary of calculation (-2,2,-2,2 encompass the set).
# Worth noting that functions use local variables and global variables carry "global tag"
import numpy as np
import matplotlib.pyplot as plt


# Plotting function creates a heatmap - Relied on by main.
def plotting(value, tolerance, x_min, x_max, y_min, y_max):
	plt.xlabel("Real Axis")
	plt.ylabel("Imaginary Axis")
	plt.title("The Mandelbrot Set. Tolerance: %s" % tolerance)
	plt.grid(True)
	plt.imshow(value, origin="0,0", interpolation="none", extent=[x_min, x_max, y_min, y_max])
	plt.savefig("MandelBrot.png", bbox_inches="tight")
	plt.show()


# Algorithm to compute if point is within set - Relied on by main
def mandel_calc(point, tolerance):
	z = 0
	for i in range(1, tolerance):
		if abs(z) > 2:
			return i
		z = z * z + point
	return 0


# Main function intialises & creates grid.  Dependent on mandel_calc & plotting.
def mandelbrot_main(x_min, x_max, y_min, y_max, grid_size, tolerance):
	real = np.linspace(x_min, x_max, grid_size)
	imag = np.linspace(y_min, y_max, grid_size)
	value = np.empty((grid_size, grid_size))
	for i in range(grid_size):
		for j in range(grid_size):
			value[j, i] = mandel_calc(real[i] + 1j * imag[j], tolerance)
	plotting(value, tolerance, x_min, x_max, y_min, y_max)
	return real

print("This code will compute the mandelbrot set for a user defined number of points between uer defined boundaries.\n")
print("The tolerance is the number of times a specific point will be interated on to determine if it is in the set.\n")
print("A plot is saved to file and then printed to screen.\n")
print("Note that -2 -> x -> 2 & -2 -> y -> 2 encompass the set.\n")

# mandelbrot_main(-2, 2, -2, 2, 1000, 100)
# mandelbrot_main(0, .5, .5, 1.0, 1000, 100)
# mandelbrot_main(.5, .6, .3, .4, 1000, 100)
# mandelbrot_main(.34, .36, .50, 5.2, 1000, 100
# mandelbrot_main(.30, .32, .56, .58, 1000, 100)
# mandelbrot_main(.36, .38, .58, .60, 1000, 50)
# Global_x_min, Global_x_max, Global_y_min, Global_y_max = [float(x) for x in raw_input("Enter x & y plotting boundaries (xmin xmax ymin ymax): ").split()]
# Global_Grid_size, Global_Tolerance = [int(x) for x in raw_input("Enter grid size and tolerance here (recommend 1000 100): ").split()]

Global_x_min = float(input("Input x_min:"))
Global_x_max = float(input("Input x_max:"))
Global_y_min = float(input("Input y_min:"))
Global_y_max = float(input("Input y_max:"))
Global_Grid_size = int(input("Input grid_size:"))
Global_Tolerance = int(input("Input tolerance:"))

print("Inputs ok. Computing set ...")
mandelbrot_main(Global_x_min, Global_x_max, Global_y_min, Global_y_max, Global_Grid_size, Global_Tolerance)
