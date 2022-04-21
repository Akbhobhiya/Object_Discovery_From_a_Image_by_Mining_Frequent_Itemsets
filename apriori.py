from itertools import chain, combinations

def subset(itemset, num):
	return [i for i in combinations(itemset, num)]

def count_subset(itemset):
	lk = {}
	for item in itemset:
		for j in pixel:
			it = [str(i) for i in pixel[j]]
			k = 0
			s = item
			for i in item:
				if i in it:
					k += 1
			if k == len(item):
				if len(item) > 2:
					item = str(s)
					if item in lk:
						lk[item] += 1
					else:
						lk[item] = 1
					item = s
				else:
					if item in lk:
						lk[item] += 1
					else:
						lk[item] = 1			
	return lk


def ifinitem(test, item):
	k = 0
	l = len(item)
	for t in test:
		for i in range(l):
			if item[i] in t:
				k += 1
		if k == l:
			# print ("%s is repeating"%(item))
			return False

	return True

def ifinset(item, sub, l, test):
	k = 0
	for i in range(l):
		if sub[i] not in item:
			item.append(sub[i])
			return item
		else:
			k += 1
	if k == l:

		return []
	elif k == 0:
		return item




def subs(itemset, num):
	test = []
	count = len(itemset)
	for item in itemset:
		l = len(item)
		for j in range(1, count):
			new = [i for i in item]
			new1 = [i for i in itemset[j]]
			m = ifinset(new, new1, l, test)
			if m not in test:
				# print (m)
				if ifinitem(test, m) is True:
					test.append(m)
				else:
					pass
			else:
				pass
				# print ("repeating %s"%(m))

	return test

def filter_support(ck, MinSupport, count):
	L = []
	k = {}
	for i in ck:
		if (ck[i]/count)*100 >= MinSupport:
			L.append(i)
			k[i] = ck[i]
	return sorted(L), k


def Apriori_prune(Ck,MinSupport):
    L = []
    for i in Ck:
        if Ck[i] >= MinSupport:
            L.append(i)
    return sorted(L)

# file = open('example.txt', 'r')
# for line in file:
# 	for item in line.strip().split(' '):
# 		if item in C1:
# 			C1[item] += 1
# 		else:
# 			C1[item] = 1
# file.close()

def num(l):
	C1={}
	import pdb; pdb.set_trace()
	for i in l:
		for line in pixel:
			it = [str(i) for i in pixel]
			if i in it: 
				if i in C1:
					C1[i] += 1
				else:
					C1[i] = 1

def run(pix, sup):
	global pixel
	pixel = pix
	C1={}
	for line in pixel:
		for i in pixel[line]:
			if str(i) in C1:
				C1[str(i)] += 1
			else:
				C1[str(i)] = 1
	# print (C1)
	lm = 3
	# l1 = Apriori_prune(C1, sup)
	l2,c = filter_support(C1, sup, len(pixel))
	# c = num(l2)
	print (c)
	return l2
if __name__ == "__main__":
	lk = main(pixel)
	print (lk)