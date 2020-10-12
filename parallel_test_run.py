from subprocess import Popen


processes = []

for counter in range(2):
    chrome_cmd = 'export BROWSER=chrome && python Test_Docker.py'
    firefox_cmd = 'export BROWSER=firefox && python Test_Docker.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(2):
    processes[counter].wait()