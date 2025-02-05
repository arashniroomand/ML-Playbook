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


result = check_values(data)
print(result)
sorted_result = sorted(result)
print(f"The best and lowest loss {sorted_result[0]}")