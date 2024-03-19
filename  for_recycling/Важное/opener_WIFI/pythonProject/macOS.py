import subprocess

def get_wifi_passwords():
    try:
        profiles = subprocess.check_output(['/usr/sbin/networksetup', '-listpreferredwirelessnetworks', 'Wi-Fi']).decode('utf-8').strip().split('\n')

        pass_wifi = ''
        for profile in profiles:
            try:
                # Using osascript to execute an AppleScript to get the Wi-Fi password
                results = subprocess.check_output(['osascript', '-e', f'do shell script "security find-generic-password -wa \\"{profile}\\""']).decode('utf-8').strip()
                pass_wifi += f"{profile} -- {results}\n"
            except subprocess.CalledProcessError as ex:
                # If the password is not found, ignore the error
                if 'The specified item could not be found in the keychain' not in ex.output.decode('utf-8'):
                    raise ex

        print(pass_wifi)
    except Exception as ex:
        print(f'Error: {ex}')

# Call the function to get Wi-Fi passwords
get_wifi_passwords()

