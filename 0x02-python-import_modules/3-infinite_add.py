#!/usr/bin/python3
import sys
num = len(sys.argv) - 1
total = 0
convertedInt = 0
if __name__ == '__main__':
	for i in range(1, num + 1):
		convertedInt = int(sys.argv[i])
		total = total + convertedInt
	print("{}".format(total))
