ans=set()
def combinationSum(a, sum):
	a=set(a)
	a=list(sorted(a))
	i=0
	while a:
		en=a[0]
		if en<sum:
			dfs(en,a,sum,[en])
		elif en==sum:
			ans.add(str(en))
		a.pop(0)
	astr=""
	if len(ans)==0:
		return "Empty"
	for e in sorted(ans):
		astr+="("
		for ch in e:
			astr+=ch+" "
		astr=astr[:-1]
		astr+=")"
	return astr

def dfs(csum,a,g,path):
	for n in a:
		if n<path[-1]:
			continue
		if csum+n<g:
			npath=[n]
			npath=path+npath
			dfs(csum+n,a,g,npath)
		elif csum+n==g:
			npath=[n]
			npath=path+npath
			sl=map(str, npath)
			ans.add(''.join(sl))
			#print(ans)
