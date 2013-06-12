import argparse
from Nsound import * 
 
parser = argparse.ArgumentParser(description='MickSynth')
parser.add_argument('-f','--freq', help='Frequency Sine name',required=True)
parser.add_argument('-t','--time', help='Time of the generated sound',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
parser.add_argument('-k','--kind',help='Tipo di onda: sine/saw/square', required=True)
parser.add_argument('-a','--harm',help='Numero intero di armoniche', required=True)
args = parser.parse_args()

## show values ##
print ("Frequenza: %s" % args.freq )
print ("Time: %s" % args.time )
print ("Output: %s" % args.output )


#definisco le vars
time = float(args.time)
freq = float(args.freq)
output = str(args.output)
kind = str(args.kind)
harm = int(args.harm)

#definisco freq
b = Buffer()

if kind == "sine":
    s = Sine(44100.0)
    b << s.generate(time,freq)
elif kind == "saw":
    s = Sawtooth(44100.0,harm)
    b << s.generate(time,freq)
elif kind == "square":
    s = Square(44100.0, harm)
    b << s.generate(time,freq)
else:
    print 'Error somefuckingwhere'

b >> output



