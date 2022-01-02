ctemp = float(input('Informe a temperatura em ⁰C: '));
ftemp = float(ctemp * 1.8 + 32);
ktemp = float(ctemp - 273.15);
print('A temperatura de {:.1f}⁰C coresponde a: \nFahrenheigt: {:.1f}⁰F  \nKelvin: {:.1f}K.'.format(ctemp,ftemp,ktemp));