import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def charge_vs_force_on_charge():
    charge_1 = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]
    force_on_charge_2 = [-280.861, -224.689, -168.517, -112.344, -56.172, 0, 56.172, 112.344, 168.517, 224.689, 280.861]
    slope, intercept, r_value, p_value, std_err = linregress(charge_1, force_on_charge_2)
    print(slope)

    mn = np.min(charge_1)
    mx = np.max(charge_1)
    x1 = np.linspace(mn, mx, 500)
    y1 = slope * x1 + intercept

    fig = plt.figure()
    plt.plot(charge_1, force_on_charge_2, 'ob')
    plt.plot(x1, y1, '-r')
    fig.suptitle('Charge 1 vs. Force on Charge 2', fontsize=20)
    plt.xlabel('Charge 1 (µC)', fontsize=16)
    plt.ylabel('Force on Charge 2 (N)', fontsize=16)
    plt.savefig('charge1_vs_F_charge2.png')

def force_vs_distance():
    q1 = 5
    q2 = 5
    r_arr = np.array([2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5])
    F_arr = [561.722, 359.502, 249.654, 183.419, 140.430, 110.597, 89.876, 74.277, 62.414, 53.181]
    k_arr = []
    for i in range(len(F_arr)):
        k_arr.append(F_arr[i] / (q1 * q2))

    log_k_arr = []
    log_r_arr = []
    for j in range(len(k_arr)):
        log_k_arr.append(math.log(k_arr[j]))
        log_r_arr.append(math.log(r_arr[j]))

    slope, intercept, r_value, p_value, std_err = linregress(log_r_arr, log_k_arr)
    mn = np.min(log_r_arr)
    mx = np.max(log_r_arr)
    x1 = np.linspace(mn, mx, 500)
    y1 = slope * x1 + intercept

    fig = plt.figure()
    plt.plot(log_r_arr, log_k_arr, 'ob')
    plt.plot(x1, y1, '-r')
    fig.suptitle('log(k_12) vs. log(r)', fontsize=20)
    plt.xlabel('log(r)', fontsize=18)
    plt.ylabel('log(k_12)', fontsize=16)
    plt.savefig('force_vs_distance.png')

    print("A = " + str(math.exp(intercept)))
    print("B = " + str(slope))




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    charge_vs_force_on_charge()
    force_vs_distance()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
