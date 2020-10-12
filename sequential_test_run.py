from subprocess import check_call


for counter in range(2):
    chrome_cmd = 'export BROWSER=chrome && python Test_Docker.py'
    firefox_cmd = 'export BROWSER=firefox && python Test_Docker.py'
    check_call(chrome_cmd, shell=True)
    check_call(firefox_cmd, shell=True)
