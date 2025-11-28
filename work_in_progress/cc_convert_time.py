from datetime import datetime

def convert_time(data):
	"""Converts column 2 and column 3 from str to time"""

	for line in data:
		try:
			time = datetime.strptime(line[1], "%H:%M:%S").time()
		except ValueError: #encounters valueerror in first line header
			pass
		else:
			line[1] = time

		try:
			time = datetime.strptime(line[2], "%H:%M:%S").time()
		except ValueError:
			pass
		else:
			line[2] = time

	return data