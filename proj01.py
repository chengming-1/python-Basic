    ###########################################################
    #  Computer Project #1
    #
    #  Algorithm
    # input te rod 
    #   convert rod from string to float
    #       convert the rod to other measurement by divied coefficient
    #   output the measurement by different cofficient
    ###########################################################

rod_str=input('Input rods:')
rod_float=float(rod_str)
meter_float=rod_float*5.0292
feet_float=meter_float/0.3048
mile_float=meter_float/1609.34
furlong_float=rod_float/40
MTW_float=(5.0292*rod_float)/(3.1*1609.34/60)

print(' You input',round(rod_float,3),'rods.')
print('Conversions')
print('Meters:',round(meter_float,3))
print('Feet:',round(feet_float,3))
print('Miles:',round(mile_float,3))
print('Furlongs:',round(furlong_float,3))
print('Minutes to walk',round(rod_float,3),'rods:',round(MTW_float,3))