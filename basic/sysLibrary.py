import sys
sys.stderr.write("This is an error!\n")
sys.stderr.flush()
sys.stdout.write("This is an output text!\n")
print(sys.argv)