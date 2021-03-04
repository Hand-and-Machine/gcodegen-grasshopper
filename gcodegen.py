from __future__ import print_function

import rhinoscriptsyntax as rs

print('; Generated with a Python script that has no name yet')
print('M140 S{} ; Start heating bed'.format(bed_temp))
print('M104 S{} ; Start heating hotend'.format(hotend_temp))
print('M105 ; Ask for temperature info')
print('M190 S{} ; Wait for bed to heat'.format(bed_temp))
print('M109 S{} ; Wait for hotend to heat'.format(hotend_temp))
print('G90 ; Use absolute positioning')
print()
print('; Ender 3 Custom Start G-code')
print('G92 E0 ; Reset Extruder')
print('G28 ; Home all axes')
print('G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed')
print('G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position')
print('G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line')
print('G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little')
print('G1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line')
print('G92 E0 ; Reset Extruder')
print('G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed')
print('G1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish')
print()
print('G92 E0 ; Reset extruder')
print('G1 F1500 E-6.5 ; Retract a bit')
print('G0 X110 Y110 Z0.3 ; Move to center of build plate')
print('G92 X0 Y0 Z0 ; Re-center coordinates here')

for polyline in lines:
    print()
    last = polyline[0]
    print('G0 X{} Y{} Z{} ; Move to start of polyline'.format(last.X, last.Y, last.Z))
    print('G1 E0 ; Un-retract')
    print('M83 ; Use relative extruder coordinates')
    for i, this in enumerate(polyline):
        if i == 0:
            continue
        dist = rs.Distance(last, this)
        print('G1 X{} Y{} Z{} E{}'.format(this.X, this.Y, this.Z, dist))
        last = this
    print('G1 E-6.5 ; Retract')
    print('M82 ; Use absolute extruder coordinates')
    print('G92 E-6.5 ; Mark that we retracted so that 0 is un-retracted')

print('G91 ;Relative positioning')
print('G1 E-2 F2700 ;Retract a bit')
print('G1 E-2 Z0.2 F2400 ;Retract and raise Z')
print('G1 X5 Y5 F3000 ;Wipe out')
print('G1 Z10 ;Raise Z more')
print('G90 ;Absolute positionning')
print('')
print('G1 X0 Y220 ;Present print')
print('M106 S0 ;Turn-off fan')
print('M104 S0 ;Turn-off hotend')
print('M140 S0 ;Turn-off bed')
print('')
print('M84 X Y E ;Disable all steppers but Z')
