his_name = input('Enter his name: ').lower()
her_name = input('Enter her name: ').lower()

combined_name = his_name + her_name
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('0')
v = combined_name.count('v')
e = combined_name.count('e')
love = l + o + v + e
score = int(str(true) + str(love))
print(f'Score: {score}%')