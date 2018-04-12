with open ('first_lines.dat') as input_file:
	with open ('new_data.csv', 'w') as output_file:
		for count, line in enumerate(input_file):
			outLine = ','.join(line.split())
			output_file.write(outLine + '\n')

