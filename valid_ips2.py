import re

def valid_ip2(filename):
	with open(filename, 'r') as f:
		for line in f:
			pattern = r'[1|2]?[0-9][0-9]'
			matches = re.findall(pattern, line)
			ip=[]
			for match in matches:
				ip.append(str(int(match)))
			print('.'.join(ip))
		
				
valid_ip2('ip2.txt')