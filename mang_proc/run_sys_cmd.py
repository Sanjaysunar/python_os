import subprocess

subprocess.run(["date"])
subprocess.run(["sleep","5"])

result= subprocess.run(["ls","this_file_does_not_exist"])
print(result.returncode)
