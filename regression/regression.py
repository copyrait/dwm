import numpy as np 
import math
import matplotlib.pyplot as plt 
a= list()
j= list()

def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height
    # plotting the actual points as scatter plot 
    global a
    global j
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
    a.append(x)
    j.append(y_pred)
    # plotting the regression line 
    
    plt.plot(x, y_pred, color = "g") 

    error = np.subtract(y,y_pred)
    error_square = np.square(error)
    error_sum = np.sum(error_square)
    error_value = math.sqrt(error_sum) 
    print("Error: " +str(error_value))
  
    # putting labels 
    plt.xlabel('Height (in cms)') 
    plt.ylabel('Weight (in Kgs)') 
    a = np.array(a)
    j = np.array(j)
    
    
    plt.scatter(a, j, color = "r", marker = "o", s = 40) 
    return plt
    # function to show plot 
    
  
def main(): 
    # observations 
    x = np.array([172, 175, 178, 150, 157, 152, 160, 177, 180, 173]) 
    y_points = [73, 72, 63, 50, 57, 54, 53, 72, 65, 60]
    y = np.array(y_points) 
    
    # estimating coefficients 
    b = estimate_coef(x, y) 
   
    global j
    print("Estimated coefficients:\nb_0 = {} nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plt = plot_regression_line(x, y, b)
    i = 0
    # for _ in y_points:
    #      plt.plot([],[], color = "r") 
    #      i+=1
    
    plt.plot()
    plt.show() 
    
    
if __name__ == "__main__": 
    main() 