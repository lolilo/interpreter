# ax bx

prog = """
push ax 5
push bx 2
add
"""

"""
prog = [
    8, 1, 5,
    8, 2, 2,
    2,
    8, 1, 10,
    8, 2, 5,
    1
]
"""

# push - 8
# add - 2
# sub - 1

# ax - 1
# bx - 2

def readbytes(f):
    out_bytes = []
    byte = f.read(1)
    while byte:
	out_bytes.append(byte)
	byte = int(f.read(1))

    return out_bytes

def main():

    ax = None
    bx = None

    p = open("something.test", "rb")
    prog = readbytes(p)
    p.close()
    print prog
    
    #lines = p.split("\n")
    #while lines:
    while prog:
	cmd = prog.pop(0)

	if cmd >= 8:
	    arg1 = prog.pop(0)
	    arg2 = prog.pop(0)

	if cmd == 8:
	    if arg1 == 1:
		ax = arg2
	    elif arg1 == 2:
		bx = arg2
	elif cmd == 2:
	    arg1 = ax
	    arg2 = bx
	    val = arg1+arg2
	    ax = val
	elif cmd == 1:
	    arg1 = ax
	    arg2 = bx
	    val = arg1-arg2
	    ax = val
	
	#print "%s -- AX: %r, BX: %r"%(line, ax, bx)
	print "AX: %r, BX: %r"%(ax, bx)


if __name__ == "__main__":
    main()
