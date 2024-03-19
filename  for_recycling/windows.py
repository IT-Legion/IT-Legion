import subprocess

try:
    data = subprocess.check_output('netsh wlan show profiles').decode('cp866').strip('\n')
    profile = []
    for i in data.split('\n'):
        if 'Все профили пользователей' in i:
            profile.append(i.split(':')[1][1:-1])

    pass_wifi = ''
    for i in profile:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')

        for j in results:
            if 'Содержимое ключа' in j:
                pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"

    print(pass_wifi)
except Exception as ex:
    print(f'Ошибка: {ex}')
