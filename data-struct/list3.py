temps = [221, 231, 340, -9999, 555, 202]

new_temps = [item / 10 if item == -9999 else 1 for item in temps]

print(new_temps)