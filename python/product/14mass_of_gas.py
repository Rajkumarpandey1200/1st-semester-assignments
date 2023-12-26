# To determine the volume a certain mass of gas at a given temperature 
# and pressure when the volume is known at the normal pressure
# and at the absolute temperature.

T=float(input("ENTER THE TEMPERATURE OF THE GAS IN KELVIN (K) = "))

P= float(input("ENTER THE PRESSURE OF THE GAS IN (atm)"))

n=float(input("ENTER THE NUMBER OF MOLES (mol) OF THE GAS = "))

R=0.0821

V =(n*R*T)/P

print("MOLAR VOLUME (V) OF THE GAS IN LITER (L) AT THE GIVEN TEMPERATURE AND PRESSURE IS ",V)