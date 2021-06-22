# name - Aayush Gakhar
# r.no. - 2020006

import numpy as np
import matplotlib.pyplot as plt


# NO other imports are allowed

class Shape:
    """
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    """

    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None

    def translate(self, dx, dy):
        """
        Polygon and Circle class should use this function to calculate the translation
        """
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])

    def scale(self, sx, sy):
        """
        Polygon and Circle class should use this function to calculate the scaling
        """
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])

    def rotate(self, deg):
        """
        Polygon and Circle class should use this function to calculate the rotation
        """
        rad = deg * (np.pi / 180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]])

    def plot(self, x_dim, y_dim):
        """
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        """
        x_dim, y_dim = 1.2 * x_dim, 1.2 * y_dim
        plt.plot((-x_dim, x_dim), [0, 0], 'k-')
        plt.plot([0, 0], (-y_dim, y_dim), 'k-')
        plt.xlim(-x_dim, x_dim)
        plt.ylim(-y_dim, y_dim)
        plt.grid()
        plt.show()


# noinspection PyMethodOverriding,PyUnboundLocalVariable,PyUnresolvedReferences
class Polygon(Shape):
    """
    Object of class Polygon should be created when shape type is 'polygon'
    """

    def __init__(self, A):
        """
        Initializations here
        """
        # this is the __init__ func. all the varables of a class are initialized here.
        Shape.__init__(self)
        self.origA = A  # this stores original coordinates of polygon
        self.verbose = None  # this will be changed to true by main() of required
        self.A = A  # this is the coordinate matrix nX3 form

    def plot_help(self, d=False, o=False):
        """
        helper function. plots the polygon. if d==True it is dotted. if o == True it prints original polygon
        """
        if o:  # plot original figure for the plot func
            x = [i[0] for i in self.origA]  # makes list of x and y coordinates
            y = [i[1] for i in self.origA]
        else:
            x = [i[0] for i in self.A]  # makes list of x and y coordinates
            y = [i[1] for i in self.A]
        if x and y:
            lx, ly = abs(max(x, key=abs)), abs(max(y, key=abs))  # max coord value of x and y
        else:
            lx = ly = 0
        x.append(x[0])  # close the plot
        y.append(y[0])
        if d:  # dotted or not
            plt.plot(x, y, color='grey', linestyle='--')
        else:
            plt.plot(x, y, 'k-')
        return lx or 1, ly or 1  # the max x and y  coord

    def ppol(self):
        """
        helper function. prints the polygon.
        """
        x = [i[0] for i in self.A]  # makes list of x and y coordinates
        y = [i[1] for i in self.A]
        x = np.round(x, 2)  # round off x and y for specified format
        y = np.round(y, 2)
        print(*x, *y)

    def rp(self):
        """
        helper function. returns the polygon coord.
        """
        x = [i[0] for i in self.A]  # makes list of x and y coordinates
        y = [i[1] for i in self.A]
        return np.round(x, 2), np.round(y, 2)  # round off x and y for specified format

    def translate(self, dx, dy=None):
        """
        Function to translate the polygon

        This function takes 2 arguments: dx and dy

        This function returns the final coordinates
        """
        if dy is None:  # dy is not given
            dy = dx

        Shape.translate(self, dx, dy)  # this makes the T_t matrix for given dx,dy

        self.ppol()  # this prints the initial coordinates

        if self.verbose:  # verbose tells whether to plot or not
            p, q = self.plot_help(True)  # this plots the polygon if verbose is true p,q are the coordinates
            # of xlim,ylim

        self.A = np.transpose(np.dot(self.T_t, np.transpose(self.A)))

        self.ppol()  # this prints the final coordinates

        if self.verbose:  # verbose tells whether to plot or not
            u, v = self.plot_help()  # this plots the polygon if verbose is true
            Shape.plot(self, max(p, u), max(q, v))
        return self.rp()  # this returns the coordinates as list of x and y coordinates in numpy arrays

    def scale(self, sx, sy=None):
        """
        Function to scale the polygon

        This function takes 2 arguments: sx and sx

        This function returns the final coordinates
        """
        if sy is None:
            sy = sx

        Shape.scale(self, sx, sy)  # this makes the T_s matrix for given sx.sy

        self.ppol()  # this prints the initial coordinates

        if self.verbose:  # verbose tells whether to plot or not
            p, q = self.plot_help(True)  # this plots the polygon if verbose is true

        x = [i[0] for i in self.A]
        y = [i[1] for i in self.A]

        cx, cy = sum(x) / len(x), sum(y) / len(y)
        self.A = self.A - [cx, cy, 0]

        self.A = np.transpose(np.dot(self.T_s, np.transpose(self.A)))

        self.A = self.A + [cx, cy, 0]

        self.ppol()  # this prints the final coordinates

        if self.verbose:  # verbose tells whether to plot or not
            u, v = self.plot_help()  # this plots the polygon if verbose is true
            Shape.plot(self, max(p, u), max(q, v))
        return self.rp()  # this returns the coordinates as list of x and y coordinates in numpy arrays

    def rotate(self, deg, rx=0, ry=0):
        """
        Function to rotate the polygon

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates
        """
        Shape.rotate(self, deg)  # this makes the T_r matrix for given deg

        self.ppol()  # this prints the initial coordinates

        if self.verbose:  # verbose tells whether to plot or not
            p, q = self.plot_help(True)  # this plots the polygon if verbose is true

        self.A = self.A - [rx, ry, 0]

        self.A = np.transpose(np.dot(self.T_r, np.transpose(self.A)))

        self.A = self.A + [rx, ry, 0]

        self.ppol()  # this prints the final coordinates

        if self.verbose:  # verbose tells whether to plot or not
            u, v = self.plot_help()  # this plots the polygon if verbose is true
            Shape.plot(self, max(p, u), max(q, v))
        return self.rp()  # this returns the coordinates as list of x and y coordinates in numpy arrays

    def plot(self):
        """
        Function to plot the polygon

        This function should plot both the initial and the transformed polygon

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        """
        p, q = self.plot_help(True, True)  # first True for dotted second for original coord
        u, v = self.plot_help()
        Shape.plot(self, max(p, u), max(q, v))


# noinspection PyMethodOverriding,PyUnboundLocalVariable,PyUnresolvedReferences
class Circle(Shape):
    """
    Object of class Circle should be created when shape type is 'circle'
    """

    def __init__(self, x=0, y=0, radius=5.0):
        """
        Initializations here
        """
        # this is the __init__ func. all the varables of a class are initialized here.
        Shape.__init__(self)
        self.origa = x  # these are storing original values
        self.origb = y
        self.origr = radius
        self.verbose = None  # this will be changed to true by main() of required
        self.a = x  # these values will be updated by functions
        self.b = y
        self.r = radius

    def pcir(self):
        """
        helper function. prints the polygon coord.
        """
        # this prints in required format
        print(round(self.a, 2), round(self.b, 2), round(self.r, 2))

    def rc(self):
        """
        helper function. returns the polygon coord.
        """
        # this returns in required format
        return round(self.a, 2), round(self.b, 2), round(self.r, 2)

    def translate(self, dx, dy=None):
        """
        Function to translate the circle

        This function takes 2 arguments: dx and dy (dy is optional).

        This function returns the final coordinates and the radius
        """
        if dy is None:  # if dy is not given
            dy = dx

        Shape.translate(self, dx, dy)  # this makes the T_t matrix for given dx,dy

        self.pcir()  # this prints the initial coordinates

        if self.verbose:  # this plots the polygon if verbose is true
            figure, axes = plt.subplots()
            axes.add_artist(plt.Circle((self.a, self.b), self.r, fill=False, linestyle='--', color='grey'))
            p, q = abs(self.a) + self.r, abs(self.b) + self.r

        [self.a, self.b] = np.dot(self.T_t, [self.a, self.b, 1])[:2]

        self.pcir()  # this prints the final coordinates

        if self.verbose:  # this plots the polygon if verbose is true
            axes.add_artist(plt.Circle((self.a, self.b), self.r, fill=False))
            u, v = abs(self.a) + self.r, abs(self.b) + self.r
            Shape.plot(self, max(p, u) or 1, max(q, v) or 1)

        return self.rc()  # this returns the coordinates of center and radius rounded off

    def scale(self, sx):
        """
        Function to scale the circle

        This function takes 1 argument: sx

        This function returns the final coordinates and the radius
        """
        if sx < 0:
            sx = -sx
        Shape.scale(self, sx, sx)  # this makes the T_s matrix for given sx,sy

        self.pcir()  # this prints the initial coordinates

        if self.verbose:  # this plots the polygon if verbose is true
            figure, axes = plt.subplots()
            axes.add_artist(plt.Circle((self.a, self.b), self.r, fill=False, linestyle='--', color='grey'))
            p, q = abs(self.a) + self.r, abs(self.b) + self.r

        self.r = np.dot(self.T_s, [self.r, 0, 1])[0]

        self.pcir()  # this prints the final coordinates

        if self.verbose:  # this plots the polygon if verbose is true
            axes.add_artist(plt.Circle((self.a, self.b), self.r, fill=False))
            u, v = abs(self.a) + self.r, abs(self.b) + self.r
            Shape.plot(self, max(p, u) or 1, max(q, v) or 1)

        return self.rc()  # this returns the coordinates of center and radius rounded off

    def rotate(self, deg, rx=0, ry=0):
        """
        Function to rotate the circle

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)

        This function returns the final coordinates and the radius
        """
        Shape.rotate(self, deg)  # this makes the T_t matrix for given deg

        self.pcir()  # this prints the initial coordinates

        if self.verbose:  # this plots the polygon if verbose is true
            figure, axes = plt.subplots()
            axes.add_artist(plt.Circle((self.a, self.b), self.r, fill=False, linestyle='--', color='grey'))
            p, q = abs(self.a) + self.r, abs(self.b) + self.r

        [self.a, self.b] = np.dot(self.T_r, [self.a - rx, self.b - ry, 1])[:2]

        self.a, self.b = self.a + rx, self.b + ry

        self.pcir()  # this prints the final coordinates

        if self.verbose:  # this plots the polygon if verbose is true
            axes.add_artist(plt.Circle((self.a, self.b), self.r, fill=False))
            u, v = abs(self.a) + self.r, abs(self.b) + self.r
            Shape.plot(self, max(p, u) or 1, max(q, v) or 1)

        return self.rc()  # this returns the coordinates of center and radius rounded off

    def plot(self):
        """
        Function to plot the circle

        This function should plot both the initial and the transformed circle

        This function should use the parent's class plot method as well

        This function does not take any input

        This function does not return anything
        """
        figure, axes = plt.subplots()
        axes.add_artist(plt.Circle((self.a, self.b), self.r, fill=False))
        axes.add_artist(plt.Circle((self.origa, self.origb), self.origr, fill=False, linestyle='--', color='grey'))
        u, v = abs(self.origa) + self.origr, abs(self.origb) + self.origr
        p, q = abs(self.a) + self.r, abs(self.b) + self.r
        Shape.plot(self, max(p, u) or 1, max(q, v) or 1)


if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    vin = int(input('verbose? 1 to plot, 0 otherwise: '))
    verbose = vin == 1  # this takes verbose as input
    T = int(input('Enter the number of test cases: '))  # this takes no of testcases as input
    for testcase in range(T):  # loop for each testcase
        PorC = int(input('Enter type of shape (polygon/circle): ')) == 0  # this takes shape as input
        if PorC:
            n = int(input('Enter the number of sides: '))
            arr = []
            for i in range(n):  # loop for each coordinate
                xc, yc = map(float, input('enter (x{}, y{}): '.format(i + 1, i + 1)).split())
                arr.append([xc, yc, 1.0])  # this takes coord as input and append to arr
            newshape = Polygon(np.array(arr))  # make a new object (polygon) specifying arr as the parameter
        else:
            a, b, r = map(float, input('Enter the coordinates of center and radius(a, b, r): ').split())
            newshape = Circle(a, b, r)
        newshape.verbose = verbose  # set verbose for the shape
        Q = int(input('Enter the number of queries: '))  # this takes no of queries as input
        print('Enter Query:\n1) R deg (rx) (ry)\n2) T dx (dy)\n3) S {}\n4) P\n'.format('sx (sy)' if PorC else 'sr'))
        for query in range(Q):  # loop for each query
            qin = input().split()  # this takes query as input
            if qin[0].lower() == 't':
                if len(qin) == 3:  # this specify dx and dy according to length of input provided
                    dx, dy = float(qin[1]), float(qin[2])
                else:
                    dx = dy = float(qin[1])
                newshape.translate(dx, dy)
            elif qin[0].lower() == 's':
                if PorC:
                    if len(qin) == 3:  # this specify sx and sy according to length of input provided
                        sx, sy = float(qin[1]), float(qin[2])
                    else:
                        sx = sy = float(qin[1])
                    newshape.scale(sx, sy)
                else:
                    sx = float(qin[1])
                    newshape.scale(sx)
            elif qin[0].lower() == 'r':
                deg = float(qin[1])
                rx = ry = 0
                if len(qin) == 3:  # this specify xc and yc according to length of input provided
                    rx = float(qin[2])
                elif len(qin) == 4:  # this specify xc and yc according to length of input provided
                    rx, ry = float(qin[2]), float(qin[3])
                newshape.rotate(deg, rx, ry)
            elif qin[0].lower() == 'p':
                newshape.plot()
            else:
                print('wrong input!')
