import pandas as  pd
import matplotlib.pyplot as plt 

data = pd.read_csv('Data/xy_100_scores.csv')

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))
    
    
def check_values(data):
    losses = []
    for m in range(0,20):
        for b in range(0,10):
            print(m,b)
            print(loss_function(m, b, data))
            losses.append(loss_function(m, b, data))
    return losses


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - L * m_gradient
    b = b_now - L * b_gradient
    return m, b

# result = sorted(check_values(data))
# print(f'best result {result[0]}')

def find_best_values(m, b, L, epochs): 
    for _ in range(epochs):
        m, b = gradient_descent(m, b, data, L)

    print(f"Optimized m: {m}, Optimized b: {b}")
    print(f"Final Loss: {loss_function(m, b, data)}")
def set_values(temp):
    if temp == 'loss':
        print(" DO YOU WANT TO CHECK THE LOSS IN SPAN OF NUMBERS OR JUST TEST SPECIFIC NUMBER:()")
    else:
        print("*****WE SUGGEST YOU TO SET M AND B ZERO AT THE FIRST STEP BUT YOU SHOULD CONISDER YOUR DATA FIRST****")
        print()
        m = int(input("                                 PLEASE ENTER THE M VALUE: "))
        b = int(input("                                 PLEASE ENTER THE M VALUE:  "))
        L = float(input("                    ENTER LEARNING RATE:(USUALLY BETWEEN 0 AND 1 LIKE 0.01): "))
        epochs = int(input("                          ENTER THE NUMBER OF ITERATIONS:  "))
        return m, b, L, epochs