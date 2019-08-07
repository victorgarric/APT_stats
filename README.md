
# APT Stats  [![Generic badge](https://img.shields.io/badge/Python-2/3-blue.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Build-passing-green.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Accuracy-testing-orange.svg)](https://shields.io/)
A python package to calculate the probability of ions in Atomic Probe Tomography results and correlate with DA values.

## Global purpose 

The objective of this package is to give statistical probability of having a given ion in an Atomic Probe Tomography mass diagram based on both the abundance of each element in the material and the natural abundance. The package provide selecting and displaying tools in order to help the user.

##  Installation
### Dependencies 
* **matplotlib**
* **numpy**
* **mendeleev > 0.4**
* **tableprint**
### PIP
```
pip install apt-stats
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
                      'Al':0.9789},wt=True)
```
### Combination calculation
```python
#Setting the maxiumum multiple ions combinations and lowest acceptable probability
depth=3
low=1E-7
#Calculation
res=apt.calc(al_6061,depth,low)
#Adding charges to the calculation, considering three charges as maximum possibility
res=apt.charge_calculation(r,(1,3))
```
### Navigating through the results
```python
#Saving results
apt.save_results(res,'res.txt')
```
```python
#Global displaying
apt.disp_results(res)
```
![Console screenshot](https://github.com/victorgarric/APT_stats/blob/master/image/1.PNG?raw=true)

```python
#Display probabilities for DA=120
apt.disp_select(res,120)
```
![Console screenshot](https://github.com/victorgarric/APT_stats/blob/master/image/2.PNG?raw=true)
```python
#Graphical display arround 20<DA<30
apt.plot_results(res,(20,60))
```
![Graphical display](https://github.com/victorgarric/APT_stats/blob/master/image/3.PNG?raw=true)
## Warning !

This package is highly experimental. No warranty is given. The user should be using it as its own risk.
