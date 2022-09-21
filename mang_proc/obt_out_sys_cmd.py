import subprocess

result = subprocess.run(["host","8.8.8.8"],capture_output=True)
print(result.returncode)

print(result.stdout)
print(result.stdout.decode().split())

result2 = subprocess.run(["rm","does_not_exist"],capture_output=True)
print(result2.returncode)

print(result.stdout)
print(result.stderr)
