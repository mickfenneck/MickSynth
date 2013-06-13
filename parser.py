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
try:
    time = float(args.time)
    freq = float(args.freq)
    output = str(args.output)
    kind = str(args.kind)
    harm = int(args.harm)
except ValueError:
    print 'errore nell inserimento di qualche dato'

#definisco freq
b = Buffer()

if kind == "sine":
    s = Sine(44100.0)
elif kind == "saw":
    s = Sawtooth(44100.0,harm)
elif kind == "square":
    s = Square(44100.0, harm)
else:
    print 'Error somefuckingwhere'
    
b << s.generate(time,freq)
b >> output




