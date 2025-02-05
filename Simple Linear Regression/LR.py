import pandas as  pd
import matplotlib.pyplot as plt 

data = pd.read_csv('xy_100_scores.csv')

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))
    
    
def check_values(data):
    losses = []
    for m in range(1,20):
        for b in range(1,10):
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
    return (m, b)

# result = check_values(data)
# print(result)
# sorted_result = sorted(result)
# print(f"The best and lowest loss {sorted_result[0]}")
print(gradient_descent(2, 2, data, 0.001))