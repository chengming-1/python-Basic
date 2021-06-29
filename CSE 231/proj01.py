# -*- coding: utf-8 -*-
"""
Created on Mon May 21 16:24:49 2018

@author: 73251
"""

rod_str=input('Input rods:')
rod_flt=float(rod_str)
meter_flt=rod_flt*5.0292
feet_flt=meter_flt/0.3048
mile_flt=meter_flt/1609.34
furlong_flt=rod_flt/40
MTW_flt=(5.0292*rod_flt)/(3.1*1609.34/60)

print(' You input',round(rod_flt,3),'rods.')
print('Conversions')
print('Meters:',round(meter_flt,3))
print('Feet:',round(feet_flt,3))
print('Miles:',round(mile_flt,3))
print('Furlongs:',round(furlong_flt,3))
print('Minutes to walk',round(rod_flt,3),'rods:',round(MTW_flt,3))