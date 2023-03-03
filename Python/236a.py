usuario_id = input()

usuario_id_final = ''.join(set(usuario_id))

if len(usuario_id_final) % 2 == 0:
    print('CHAT WITH HER!')

else:
    print('IGNORE HIM!')
