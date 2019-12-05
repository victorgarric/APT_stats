
# APT Stats  [![Generic badge](https://img.shields.io/badge/Pytehon-2/3-blue.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Build-passing-green.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Accuracy-testing-orange.svg)](https://shilds.io/)
A python package to calculate the probability of ions in Atomic Probe Tomography results and correlate with DA values.

## Global purpose 

The objective of this package is to give statistical probability of having a given ion in an Atomic Probe Tomography mass diagram based on both the abundance of each element in the material and the natural abundance. The package provide selecting and displaying tools in order to help the user.

## Lastest version

A new "impurities", keyword has been added to the material definition. This way, impurities can be introduced in the material calculation :
```python
impurities=('Ar','Ne')
```
Therefore, during calculation of the whole possibilities or for a specific mass to charge ratio, impurities can be displayed. Warning has to be made that the probability levels for impurities are normalized to 1 and are not acknowledgeable as a real probability as no probability value is imputed. 
##  Installation
### Dependencies 
* **matplotlib**
* **numpy**
* **mendeleev > 0.4**
* **tableprint**
### PIP
```
pip install APT-stats==0.0.4
```
## Usage 
### Defining the material
```python
import APT_stats as apt
#Defining a 6061 aluminum alloy using weight percentages
al_6061=apt.material({'Mg':0.0085,
                      'Si':0.0048,
                      'Fe':0.0005,
                      'Cu':0.003,
                      'Cr':0.003,
                      'Mn':0.0008,
                      'Zn':0.0005,
                      'Al':0.9789},impurities=('Ar',),wt=True)
```
### Combination calculation
```python
#Setting the maxiumum multiple ions combinations and lowest acceptable probability
depth=3
low=1E-7
#Calculation
res=apt.calc(al_6061,depth,low)
#Adding charges to the calculation, considering three charges as maximum possibility
res=apt.charge_calculation(res,(1,3))
```
### Navigating through the results
```python
#Saving results
apt.save_results(res,'res.txt')
```
```python
#Global displaying without impurities
apt.disp_results(res,imp=False)
```
![Console screenshot](https://github.com/victorgarric/APT_stats/blob/master/image/1.PNG?raw=true)

```python
#Display probabilities for DA=120
apt.disp_select(res,120)
```
![Console screenshot](https://github.com/victorgarric/APT_stats/blob/master/image/2.PNG?raw=true)
```python
#Graphical display arround 20<DA<30
apt.plot_results(res,(20,30))
```
![Graphical display](https://github.com/victorgarric/APT_stats/blob/master/image/3.PNG?raw=true)
## Warning !

This package is highly experimental. No warranty is given. The user should be using it as its own risk.
