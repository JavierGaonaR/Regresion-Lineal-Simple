import pandas as pd
import matplotlib.pyplot as plt

def reg_lin(path, x, y):
    data = pd.read_csv(path)

    data_x = data[x].values
    data_y = data[y].values

    mean_x = sum(data_x) / len(data_x)
    mean_y = sum(data_y) / len(data_y)

    m = sum([((data_x[i] - mean_x) * (data_y[i] - mean_y)) for i in range(len(data))]) / sum([(val - mean_x) ** 2 for val in data_x])

    b = mean_y - m * mean_x

    print('Numero de instancias:', len(data))
    print('y =', b, '+', str(m) + 'x')

    data.plot.scatter(x = x, y = y)
    
    plt.scatter(data_x, data_y)
    plt.plot(data_x, b + m * data_x, color="red") 
    plt.show()


if __name__ == "__main__":

    reg_lin('fuel.csv', 'ENGINESIZE', 'CO2EMISSIONS')
    # reg_lin('salaryData.csv', 'YearsExperience', 'Salary')
    # reg_lin('articulos_ml.csv', 'Word count', '# Shares')
