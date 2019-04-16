#!/usr/bin/python

#Paul Bosonetto

import os, sys



[os.rename(sys.argv[1] + x, sys.argv[1] + x.replace(" ", "_")) for x in os.listdir(sys.argv[1])]



