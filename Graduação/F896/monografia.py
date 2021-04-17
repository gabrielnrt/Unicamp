from numpy import sqrt, array, log, linspace, pi
from pylab import plot, scatter, show, figure, xlabel, ylabel, legend, grid, yscale, errorbar
from pandas import read_csv

hc2 = 3.89379 * (10**8)
alpha2 = 137**(-2)

# Parte 1 ------------------------------------------------------------------------------

jade = read_csv('Jadee.csv',delimiter = ';', decimal = ',')
pluto = read_csv('Pluto.csv',delimiter = ';', decimal = ',')
tasso = read_csv('Tasso.csv', delimiter = ';', decimal = ',')
markj = read_csv('MarkJ.csv',delimiter = ';', decimal = ',')

x = linspace(5,50,1000)
y = (4*pi*hc2*alpha2/3)*(x**(-2))

plot(x,y, color='navy', label='Previsão do Modelo')
scatter(jade['x'],jade['y'], color='gold', label='JADE')
scatter(pluto['x'],pluto['y'], color='red', label='PLUTO')
scatter(tasso['x'],tasso['y'], color='lime', label='TASSO')
scatter(markj['x'],markj['y'], color='violet', label='MARK-J')


yscale('log')
grid(True, linestyle='--')
legend()
xlabel('$\sqrt{s}$ (GeV)', fontsize=20)
ylabel('$\sigma$ (pb)', fontsize=20)
show()

# Parte 2 --------------------------------------------------------------------------------

barber = read_csv('barber.csv', delimiter = ';', decimal = ',')
erro = array([.3,.4,.15,.05,.04,.035,.07,.04,.045,.04,.05])

y = (10**(-3))*(4*pi*hc2*alpha2/3)*(x**(-2))

plot(x,y, color='navy', label='Previsão do Modelo')

errorbar(barber['x'], barber['y'], yerr=erro, xerr=None, fmt='o', capsize=4, color='orange', label='Barber')


yscale('log')
grid(True, linestyle='--')
legend()
xlabel('$\sqrt{s}$ (GeV)', fontsize=20)
ylabel('$\sigma$ (nb)', fontsize = 20)

show()

# Parte 3 ----------------------------------------------------------------------------------

M = 0.105               # Massa do MUON em GeV
m_tau = 1.777           # Massa do tau em Gev

# Funções
def beta(s,m):
    x = sqrt(1 - 4*(m**2)/(s**2))
    return x

def b(s,m):
    x = beta(s,m)*(3-beta(s,m)**2)
    return x

razao = read_csv('razao.csv', delimiter = ';', decimal = ',')
errox = array([0,0,0,0,0,0.02,0.04,0.04,0.04,0.08,0.02,0.1,0.23])
erroy = array([0.005,0.01,0.007,0.01,0.01,0.006,0.006,0.012,0.008,0.015,0.015,0.017,0.011])

x = linspace(3.56,5,500)
fator = 6
y = b(x,m_tau)/(fator*b(x,M))

plot(x,y, color='navy', label='Previsão do Modelo')
errorbar(razao['x'], razao['y'], yerr=erroy, xerr=errox, fmt='o', capsize=3, color='lime', label='Dados Experimentais')

grid(True, linestyle='--')
legend(loc=4)
legend()
xlabel('$\sqrt{s}$ (GeV)', fontsize=20)
ylabel('Razão R', fontsize=20)
show()
