


fil=open("text.txt", "r")
content=fil.read()
mod = content.replace('a', '1').replace('z', '2').replace('e', '3').replace(
    'r', '7').replace('t', '6').replace('y', '5').replace('u', '4').replace(
    'c', '8').replace('g', '9').replace('o', '0').replace('i', '-').replace(
    'x', '@').replace('f', '>').replace('p', 'ç').replace('h', '_').replace(
    'w', 'à').replace('d', '€').replace('m', '^').replace('j', ':').replace(
    'v', '\'').replace('s', '&').replace('l', '=').replace('k', ',').replace(
    'b', 'ù').replace('O', '²').replace('P', '+').replace('C', '?').replace(
    'n', '%').replace('I', ')').replace('M', '}').replace('X', '!').replace(
    'ù', '.').replace('U', '(').replace('L', '¨').replace('W', '§').replace(
    'é', '`').replace('Y', '°').replace('K', '^').replace('Q', '*').replace(
    'ç', 'A').replace('T', ']').replace('J', 'é').replace('S', 'µ').replace(
    'A', 'B').replace('R', '[').replace('H', '#').replace('D', '£').replace(
    'Z', 'C').replace('E', '|').replace('G', '{').replace('F', '$').replace(
    'V', 'D').replace('B', '/').replace('N', '>').replace('q', '¤')
file = open("text.txt", "w")
file.write(mod)
file.close()

