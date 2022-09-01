import re

def extract_pid(log_line):
	regex = r"\[(\d+)\]"
	result = re.search(regex, log_line)
	if result is None:
		return ""
	return result[1]

log = "Sep 1 07:52:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

print(extract_pid(log))

print(extract_pid("99 elephants in a [cage]"))


