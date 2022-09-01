import re

log = "Sep 1 07:52:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result = re.search(regex, " numbers [34566777]")
print(result[1])

