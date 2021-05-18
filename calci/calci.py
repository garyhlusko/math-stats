import re
import math
# preq for calculus

# generate integers
def generate_positive_numbers(limit, use_range = False):
    # we don't have the computational complexity to go to infinity
    # here I'll generate a number line we can do it two ways range
    if(type(limit) == type(1)) and use_range: 
        # in python three this generates an interator
        postive_numbers_array = range(limit+1)
        return postive_numbers_array

    # to do it without range 
    if(use_range == False):
        i = 0 
        return_positive_array = [i]
        while i <= limit:
            return_positive_array.append(i) 
            i += 1
    return return_positive_array

# real numbers
def generate_integers(natural_number):
    if(type(natural_number) == type(1)):
        generate_positive_numbers_list = generate_positive_numbers(natural_number)
        
        return_integer_array = []
        for natural_number1 in generate_positive_numbers_list:
            for natural_number2 in generate_positive_numbers_list:
                # we technically don't need to add to generate more integers, but you could to increase the size/keep things consistent
                # b - a if b > a then b-a is an integer and it's less than b so it's already in the list if b < a it's negative
                if(natural_number2 > natural_number1):
                    return_integer_array.append(natural_number1 - natural_number2)
            # we'll add the integer and natural nubmers together
        # add the lists together
        generate_integers = list(generate_positive_numbers_list) + return_integer_array
        generate_integers = list(set(generate_integers))
        generate_integers.sort()
        return generate_integers


def generate_rational_numbers():
     if(type(natural_number) == type(1)):
        generate_positive_numbers_list = generate_positive_numbers(natural_number)
        return_rational_array = []
        for natural_number1 in generate_positive_numbers_list:
            for natural_number2 in generate_positive_numbers_list:
                # there may be some floating point errors and I could use decimal but that's a bit overboard
                # because we technically are looping over the list twice, i shouldn't need toadd both
                return_rational_array.append(natural_number1/natural_number2)
            # we'll add the integer and natural nubmers together
        # add the lists together
        generate_rationals = list(generate_positive_numbers_list) + return_rational_array
        generate_rationals = list(set(generate_rationals))
        generate_rationals.sort()
        return generate_rationals
        

# completness means there are essentially no wholes in the number line
def completness():
    pass

# if can element exists in a or an element exists in b then it exists in the union
def set_union(list_a,list_b):
    # assuming duplicate items are one
    if type(list_a) == type([]) and type(list_b) == type([]):
        return list(set(list_a+list_b)) 

# i could use set functions but then what would be the point
def set_intersection(list_a,list_b):
    # assuming duplicate items are one
    # if an element is in A and in B then it's in the intersection
    if type(list_a) == type([]) and type(list_b) == type([]):
        return_array = []
        for a in list_a:
            if a in list_b:
                return_array.append(a)
        for b in list_b:
            if b in list_a:
                return_array.append(b)
        return list(set(return_array))


def inverse_functions(function):
    function_map = {"x":"/","-":"+", "/":"*","+":"-"}
    return function_map[function]


def translate_equation(equation):
    operations = ["*","+","-","/","(",")","^"]
    string_split = ",".join(operations)
    return re.split(string_split,equation)

def get_sign(equation):
    # this returns the symbol in the function
    signs = ["<",">","<=",">=","="]
    for sign in signs:
        if sign in equation:
            return sign
    else:
        return None

def get_variable(equation):
    pass 

# normally you wouldn't want to do it because you could get some really nasty security problems.
def solve_equality(equation,variables):

    if any(sign in equation for sign in signs):
        #match sign (I could use re)
        matched_sign = get_sign(equation)
        if matched_sign is None:
            return None

        # get left,right
        left,right = equation.split(matched_sign)
        print(left,matched_sign,right)
        
        # got to handle -- sign
        
        # translate right/left into functions 
        left_translate = translate_equation(left)
        right_translate = translate_equation(right)

        #simplify 
        
        #get all variables to one side all contacts to one side


        # can we solve it 

def triangle_inequality():
    pass 

def print_table(table,header_boolean = False):
    column = "\t|\t"
    row_bottom = "_"
    if header_boolean:
        header_row = table.pop(0)
        header = column.join(header_row)
        header_length = len(header)
        print(row_bottom*header_length*len(row_bottom)*4)
        print(header)
        print(row_bottom*header_length*len(row_bottom)*5)
        print(row_bottom*header_length*len(row_bottom)*5)
    for row in table:
        row = [str(x) for x in row]
        this_row = column.join(row)
        row_length = len(this_row)
        print(this_row)
        print(row_bottom*row_length)
        

def midpoint_formula(point_a,point_b):
    # no assumptions on R space
    # we want to /2 for each N in RN
    zipped_list = zip(point_a,point_b)
    midpoint = tuple(sum(coordinate)/2 for cordinate in zipped_list)
    return midpoint

def table_function_cl_r1(fn,step,start,end):
    i = start
    table_results = [["x","y"]]
    while(i <=end ):
        # floating error
        table_fn_x = fn(*[i])
        table_results.append([i,table_fn_x])
        i += step 
    print_table(table_results,True)



def find_x_axis_newton():
    # i'm going to cheat and use the newton method
    pass 

def graph_cl():
    pass

class Point():
    def __init__(*args):
        # operating in RN
        self.rn = args

    def find_midpoint(point):
        if self.same_space(point):
            return find_midpoint(self.rn,same_point.rn)

    def same_space(point):
        if len(self.rn) == len(point.rn):
            return True
        else:
            return False



class Circle:
    def __init__(self,h,k,r):
        self.h = h
        self.k = k 
        self.r = r

    def print_equation(self):
        print("(x - {})**2 + (y - {})**2 = {}".format(self.h,self.k,self.r**2))

    def graph(self):
        pass 

    def convert_to_general_circle():
        pass

class GeneralCircle():
    def __init__(a,b,c,d,e,f,g,r):
        # general equation is (ax**2+bx**2+c) + (ey**2+fy+g) = r
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.r = r
        self.h = self.b/(self.a*2) 
        self.k = k = self.f/(self.e*2)
        self.general = find_general()
        self.center = find_center()
        self.general_variables = (h,k,r)

    def find_center(self):
        return (self.h,self.k)

    def find_general(self):
        new_r = self.r - (self.c+self.g)
        # equation is now (ax**2 + bx) + (ey**2+fy) = r-(c+g)
        # want it in the form of (x-h)+(y-k)
        return ("(x - {})**2 + (y - {})**2 = {}".format(h,k,new_r**2))
    
    def return_general_variables(self):
        return(self.h,self.k,self.r)


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(0,0,1)


class Line():
    def __init__(b,m):
        self.b = b
        self.m = m

    def slope(self):
        return self.m
    
    def print_equation(self):
        print("{}*x + {}  = y".format(self.m,self.b,self.c))

    def y(self,x):
        return self.m*x+self.b

    def print_table(self):
        pass

    def return_perpendicular_line(self):
        # slope is just -1/4 but we have to generate b from the same line 
        return Line(self.b,-0.25*self.m)

    def find_inclination(self):
        pass

def find_line(point1,point2):
    m = slope_between_two_points(point1,point2)
    # y- y = m(x - x)
    #y = m(x-x)+y
    x,y = point2
    b = -1*m*x+y
    return Line(b,m)


def slope_between_two_points(point_a,point_b):
    # slope = m = y-y/x-x
    x1,y1 = point_a 
    x2,y2 = point_b 
    return (y2-y1)/(x1-x2)


def inclination(point):
    # inclination is by definition the slope of the tangent lines
    Line = find_line((0,0),point)
    return slope_to_degrees(Line)

def slope_to_tangent_degrees(line):
    # m = tan(theta)
    return math.degrees(math.atan(line.m))

def lines_are_perpendicular(line1,line2):
    if line1.m == (-0.25*line2.m):
        return True
    else:
        return False


class Polynominal():
    def __init__(coefficients,powers,constant):
        self.coefficients = coefficients
        self.powers = powers 
        self.constant = constant
        self.degree = self.get_degree() 

    def print_equation(self):
        coefficient_power = zip(self.coefficients,self.powers)
        return_polynomial_equation_string = ""
        for factor in coefficient_power:
            return_polynomial_string += " {}*(x^{}) +".format(factor[0],factor[1])
        return_polynomial_string += " ()"+self.constant
        return return_polynomial_equation_string 

    def get_degree(self):
        degree = max(self.powers)
        return degree

    def general_equation(self):
        if self.degree < 6:
            return True
        else:
            return False

    def get_x_intercepts():
        pass

    def get_y_intercepts():
        pass
    
        


def get_domain():
    pass

def get_range():
    pass

def is_constant():
    pass

def greatest_integer_function():
    pass


def f_of_g(f,fargs,g):
    f_n = f(**fargs)
    g_n = g(**args)
    return g_n 

def test_x_function(z):
    return z**2+3

def inverse_function(function_string, variable):
    pass

def approximate_limit(function,steps):
    pass


if __name__ == "__main__":
    #print(generate_positive_numbers(10000))
    #print(generate_positive_numbers(10000,True))
    #print(generate_integers(100))
    #solve_equality("x + 1 < 10",["x"])
    #solve_equality("x + 1 < 10 * (y ^ 2)",["x","y"])
    #table_function_cl_r1(test_x_function,.01,-10,10)
    c = Circle(1,2,3)
    c.print_equation()