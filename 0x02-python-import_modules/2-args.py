#!/usr/bin/python3
import sys
num = len(sys.argv) - 1
if __name__ == '__main__':
	if num == 0:
		print("0 arguments.")
	elif num == 1:
		print("1 argument:")
		print("1: {}".format(sys.argv))
	else:
		print("{} arguments:".format(num))
		for i in range(1, num + 1):
			print("{}: {}".format(i, sys.argv[i]))
