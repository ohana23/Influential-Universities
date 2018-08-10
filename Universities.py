import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

with open("theta_PR.txt") as FILE:
	data = FILE.read()

data = data.splitlines()
ccMap = {}

# Count universities and map these counts to their respectives countries.
for i in range(0, 1010):
	entrySep = data[i].split("\t")
	if entrySep[5] in ccMap:
		ccMap[entrySep[5]] += 1
	else:
		ccMap[entrySep[5]] = 1

# Remove countries with less than 2 universities in the rankings. 
# This cuts number of countries from 85 to 55.
# for key in ccMap.keys():
for key in list(ccMap):
	if ccMap[key] < 4:
		del ccMap[key]

# I'm sure there's a better way to do this, but I became interested in how 
# country codes were assigned so, in order to force myself to read them, 
# I did it the hacky brute force way. Also, I was watching an episode of 
# Silicon Valley at the same time so this didn't bother me.
ccMap['Argentina'] = ccMap['AR']
del ccMap['AR']
ccMap['Austria'] = ccMap['AT']
del ccMap['AT']
ccMap['Australia'] = ccMap['AU']
del ccMap['AU']
ccMap['Belgium'] = ccMap['BE']
del ccMap['BE']
ccMap['Brazil'] = ccMap['BR']
del ccMap['BR']
ccMap['Canada'] = ccMap['CA']
del ccMap['CA']
ccMap['Switzerland'] = ccMap['CH']
del ccMap['CH']
# ccMap['Chile'] = ccMap['CL']
# del ccMap['CL']
ccMap['China'] = ccMap['CN']
del ccMap['CN']
ccMap['Colombia'] = ccMap['CO']
del ccMap['CO']
ccMap['Cyprus'] = ccMap['CY']
del ccMap['CY']
# ccMap['Czech Republic'] = ccMap['CZ']
# del ccMap['CZ']
ccMap['Germany'] = ccMap['DE']
del ccMap['DE']
ccMap['Denmark'] = ccMap['DK']
del ccMap['DK']
# ccMap['Estonia'] = ccMap['EE']
# del ccMap['EE']
ccMap['Egypt'] = ccMap['EG']
del ccMap['EG']
ccMap['Spain'] = ccMap['ES']
del ccMap['ES']
ccMap['Finland'] = ccMap['FI']
del ccMap['FI']
ccMap['France'] = ccMap['FR']
del ccMap['FR']
ccMap['Greece'] = ccMap['GR']
del ccMap['GR']
ccMap['Hungary'] = ccMap['HU']
del ccMap['HU']
ccMap['Indonesia'] = ccMap['ID']
del ccMap['ID']
# ccMap['Ireland'] = ccMap['IE']
# del ccMap['IE']
ccMap['Israel'] = ccMap['IL']
del ccMap['IL']
ccMap['India'] = ccMap['IN']
del ccMap['IN']
# ccMap['Iraq'] = ccMap['IQ']
# del ccMap['IQ']
ccMap['Iran'] = ccMap['IR']
del ccMap['IR']
ccMap['Italy'] = ccMap['IT']
del ccMap['IT']
# ccMap['Jordan'] = ccMap['JO']
# del ccMap['JO']
ccMap['Japan'] = ccMap['JP']
del ccMap['JP']
# ccMap['North Korea'] = ccMap['KP']
# del ccMap['KP']
ccMap['South Korea'] = ccMap['KR']
del ccMap['KR']
ccMap['Lebanon'] = ccMap['LB']
del ccMap['LB']
# ccMap['Latvia'] = ccMap['LV']
# del ccMap['LV']
ccMap['Mexico'] = ccMap['MX']
del ccMap['MX']
ccMap['Malaysia'] = ccMap['MY']
del ccMap['MY']
ccMap['Netherlands'] = ccMap['NL']
del ccMap['NL']
# ccMap['Norway'] = ccMap['NO']
# del ccMap['NO']
ccMap['Nepal'] = ccMap['NP']
del ccMap['NP']
# ccMap['Philippines'] = ccMap['PH']
# del ccMap['PH']
ccMap['Poland'] = ccMap['PL']
del ccMap['PL']
ccMap['Portugal'] = ccMap['PT']
del ccMap['PT']
ccMap['Romania'] = ccMap['RO']
del ccMap['RO']
ccMap['Russia'] = ccMap['RU']
del ccMap['RU']
# ccMap['Saudi Arabia'] = ccMap['SA']
# del ccMap['SA']
ccMap['Sweden'] = ccMap['SE']
del ccMap['SE']
# ccMap['Singapore'] = ccMap['SG']
# del ccMap['SG']
# ccMap['Slovakia'] = ccMap['SK']
# del ccMap['SK']
# ccMap['Syria'] = ccMap['SY']
# del ccMap['SY']
ccMap['Thailand'] = ccMap['TH']
del ccMap['TH']
ccMap['Turkey'] = ccMap['TR']
del ccMap['TR']
ccMap['Ukraine'] = ccMap['UA']
del ccMap['UA']
ccMap['United Kingdom'] = ccMap['UK']
del ccMap['UK']
ccMap['United States'] = ccMap['US']
del ccMap['US']
ccMap['Vietnam'] = ccMap['VN']
del ccMap['VN']


ordered_ccMap = OrderedDict(sorted(ccMap.items(), reverse=True))

plt.rcdefaults()
fig, ax = plt.subplots()

countries = ordered_ccMap.keys()
y_pos = np.arange(len(countries))
performance = ordered_ccMap.values()

ax.grid(color='gray', linestyle='-', linewidth=0.5)
ax.barh(y_pos, performance, align='center', linewidth=0, height=2)
ax.set_yticks(y_pos)

ax.set_yticklabels(countries)
ax.set_xlabel('Number of Influential Universities')
ax.set_title('Country University Influence')

# Align each country name to its bar graph.
plt.yticks(y_pos + 0.5, countries)

plt.show()
