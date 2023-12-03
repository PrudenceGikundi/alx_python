#!/usr/bin/python3
def myarguments():
   import sys
   arguments = sys.argv[1:]
   num_arguments = len(arguments)
   output = ""
   if num_arguments == 0:
        output += "0 argument{}.\n".format('s' if num_arguments != 1 else '')
   else:
        output += "{} argument{}:\n".format(num_arguments, 's' if num_arguments != 1 else '')

        # Construct string for each argument with its position
        for i, arg in enumerate(arguments, 1):
            output += "{}: {}\n".format(i, arg)

   return output.strip()

