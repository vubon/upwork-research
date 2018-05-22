import subprocess

template = 'python script.py {} {} {} {}'

args = [[1, 2, 3, 4], [5, 6, 7, 8]]

# Run commands in parallel
processes = []

for arg in args:
    command = template.format(*[str(a) for a in arg])
    process = subprocess.Popen(command, shell=True)
    processes.append(process)

# Collect statuses
output = [p.wait() for p in processes]