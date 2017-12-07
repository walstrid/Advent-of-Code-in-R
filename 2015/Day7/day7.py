#! /usr/bin/python

## Part 1
data=open("./day7_data","r")
datal=data.readlines()
data.close()
wire={}
while "a" not in wire:
	for line in datal:
		line=line.split()
		if "NOT" in line:
			try:
				wire[line[3]]=65535-wire[line[1]]
			except KeyError:
				try:
					wire[line[3]]=65535-int(line[1])
				except ValueError:
					None
		elif "OR" in line:
			try:
				wire[line[4]]=wire[line[0]] | wire[line[2]]
			except KeyError:
				try:
					wire[line[4]]=int(line[0]) | wire[line[2]]
				except ValueError:
					try:
						wire[line[4]]=wire[line[0]] | int(line[2])
					except:
						None
				except KeyError:
					try:
						wire[line[4]]=int(line[0]) | int(line[2])
					except ValueError:
						None
		elif "AND" in line:
			try:
				wire[line[4]]=wire[line[0]] & wire[line[2]]
			except KeyError:
				try:
					wire[line[4]]=int(line[0]) & wire[line[2]]
				except ValueError:
					try:
						wire[line[4]]=wire[line[0]] & int(line[2])
					except:
						None
				except KeyError:
					try:
						wire[line[4]]=int(line[0]) & int(line[2])
					except ValueError:
						None	
		elif "RSHIFT" in line:
			try:
				wire[line[4]]=wire[line[0]] >> int(line[2])
			except KeyError:
				None
		elif "LSHIFT" in line:
			try:
				wire[line[4]]=wire[line[0]] << int(line[2])
			except KeyError:
				None
		else:
			try:
				wire[line[2]]=int(line[0])
			except ValueError:
				try:
					wire[line[2]]=wire[line[0]]
				except KeyError:
					None
print wire["a"]

## Part 2
for i in range(0,len(datal)):
	if "-> b\n" in datal[i]:
		datal[i]="3176 -> b"
wire={}
while "a" not in wire:
	for line in datal:
		line=line.split()
		if "NOT" in line:
			try:
				wire[line[3]]=65535-wire[line[1]]
			except KeyError:
				try:
					wire[line[3]]=65535-int(line[1])
				except ValueError:
					None
		elif "OR" in line:
			try:
				wire[line[4]]=wire[line[0]] | wire[line[2]]
			except KeyError:
				try:
					wire[line[4]]=int(line[0]) | wire[line[2]]
				except ValueError:
					try:
						wire[line[4]]=wire[line[0]] | int(line[2])
					except:
						None
				except KeyError:
					try:
						wire[line[4]]=int(line[0]) | int(line[2])
					except ValueError:
						None
		elif "AND" in line:
			try:
				wire[line[4]]=wire[line[0]] & wire[line[2]]
			except KeyError:
				try:
					wire[line[4]]=int(line[0]) & wire[line[2]]
				except ValueError:
					try:
						wire[line[4]]=wire[line[0]] & int(line[2])
					except:
						None
				except KeyError:
					try:
						wire[line[4]]=int(line[0]) & int(line[2])
					except ValueError:
						None	
		elif "RSHIFT" in line:
			try:
				wire[line[4]]=wire[line[0]] >> int(line[2])
			except KeyError:
				None
		elif "LSHIFT" in line:
			try:
				wire[line[4]]=wire[line[0]] << int(line[2])
			except KeyError:
				None
		else:
			try:
				wire[line[2]]=int(line[0])
			except ValueError:
				try:
					wire[line[2]]=wire[line[0]]
				except KeyError:
					None
print wire["a"]
