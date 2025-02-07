import shutil

import pandas as  pd
import matplotlib.pyplot as plt 

from constant import LOSS_OPTIONS
data = pd.read_csv('Data/xy_100_scores.csv')

def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))
    
    
def check_values(start_m, end_m, start_b, end_b):
    losses = []
    for m in range(start_m,end_m):
        for b in range(start_b,end_b):
            print(m,b)
            print(loss_function(m, b, data))
            losses.append([m, b, loss_function(m, b, data)])
    sorted_data = sorted(losses, key=lambda x: x[2]) 
    return sorted_data[0]


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

def find_best_values(m, b, L, epochs): 
    for _ in range(epochs):
        m, b = gradient_descent(m, b, data, L)

    print(f"Optimized m: {m}, Optimized b: {b}")
    print(f"Final Loss: {loss_function(m, b, data)}")

import shutil

def center_text(text):
    """Centers text but keeps input aligned properly."""
    terminal_width = shutil.get_terminal_size().columns
    return text.center(terminal_width)

def set_values(temp):
    terminal_width = shutil.get_terminal_size().columns  # Get terminal width dynamically

    if temp == 'loss':
        print(center_text(LOSS_OPTIONS))  # Centered text
        print()
        print(center_text("WRITE YOUR CHOICE HERE: "), end="")  # Keep input cursor aligned
        option = input()  # Normal input without shifting cursor

        if option == '1':
            try:
                print(center_text("ENTER THE START AND THE END OF SPAN FOR m: "), end="")
                start_m, end_m = map(int, input().split())

                print(center_text("ENTER THE START AND THE END OF SPAN FOR b: "), end="")
                start_b, end_b = map(int, input().split())

                best_m, best_b, final_result = check_values(start_m, end_m, start_b, end_b)
                print()
                print(center_text(f"Optimized m: {best_m}, Optimized b: {best_b}. The loss is {final_result}"))
                return 

            except ValueError:
                print(center_text("Invalid input! Please enter two integer values separated by a space."))

        elif option == '2':
            print()
            print(center_text("PLEASE ENTER THE m VALUE: "), end="")
            m = int(input())

            print(center_text("PLEASE ENTER THE b VALUE: "), end="")
            b = int(input())

            loss = loss_function(m, b, data)
            print(center_text(f"Loss with {m}*x + {b} is {loss}"))

    else:
        print(center_text("*****WE SUGGEST YOU TO SET M AND B ZERO AT THE FIRST STEP BUT YOU SHOULD CONSIDER YOUR DATA FIRST****"))
        print()
        print(center_text("PLEASE ENTER THE M VALUE: "), end="")
        m = int(input())

        print(center_text("PLEASE ENTER THE B VALUE: "), end="")
        b = int(input())

        print(center_text("ENTER LEARNING RATE (USUALLY BETWEEN 0 AND 1 LIKE 0.01): "), end="")
        L = float(input())

        print(center_text("ENTER THE NUMBER OF ITERATIONS: "), end="")
        epochs = int(input())

        return m, b, L, epochs
