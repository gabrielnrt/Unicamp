from numpy import sqrt, array, log, linspace, pi
from pylab import plot, scatter, show, figure, xlabel, ylabel, legend, grid, yscale, errorbar
from pandas import read_csv, read_excel

hc2 = 3.89379 * (10**8)
alpha2 = 137**(-2)

# Parte 1 ------------------------------------------------------------------------------

planilha = read_excel('Parte1.xlsx', sheet_name = None)

x = linspace(5,50,1000)
y = (4*pi*hc2*alpha2/3)*(x**(-2))

plot(x,y, color='navy', label='Previsão do Modelo')

scatter(planilha['Jade']['x'],planilha['Jade']['y'], color='gold', label='JADE')
scatter(planilha['Pluto']['x'],planilha['Pluto']['y'], color='red', label='PLUTO')
scatter(planilha['Tasso']['x'],planilha['Tasso']['y'], color='lime', label='TASSO')
scatter(planilha['MarkJ']['x'],planilha['MarkJ']['y'], color='violet', label='MARK-J')


yscale('log')
grid(True, linestyle='--')
legend()
xlabel('$\sqrt{s}$ (GeV)', fontsize=20)
ylabel('$\sigma$ (pb)', fontsize=20)
show()

# Parte 2 --------------------------------------------------------------------------------

barber = read_csv('barber.csv')


y = (10**(-3))*(4*pi*hc2*alpha2/3)*(x**(-2))

plot(x,y, color='navy', label='Previsão do Modelo')

errorbar(barber['x'], barber['y'], yerr=barber['Erro y'], xerr=None, fmt='o', capsize=4, color='orange', label='Barber')


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

# razao = read_csv('razao.csv', delimiter = '\t', decimal = ',')
razao = read_csv('razao.csv')


x = linspace(3.56,5,500)
fator = 6
y = b(x,m_tau)/(fator*b(x,M))

plot(x,y, color='navy', label='Previsão do Modelo')
errorbar(razao['x'], razao['y'], yerr=razao['Erro y'], xerr=razao['Erro x'], fmt='o', capsize=3, color='lime', label='Dados Experimentais')

grid(True, linestyle='--')
legend(loc=4)
legend()
xlabel('$\sqrt{s}$ (GeV)', fontsize=20)
ylabel('Razão R', fontsize=20)
show()
