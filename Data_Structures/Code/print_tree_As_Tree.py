def __repr__(self):
	if self.root==None: return ''
	content='\n' # to hold final string
	cur_nodes=[self.root] # all nodes at current level
	cur_height=self.root.height # height of nodes at current level
	sep=' '*(2**(cur_height-1)) # variable sized separator between elements
	while True:
		cur_height+=-1 # decrement current height
		if len(cur_nodes)==0: break
		cur_row=' '
		next_row=''
		next_nodes=[]

		if all(n is None for n in cur_nodes):
			break

		for n in cur_nodes:

			if n==None:
				cur_row+='   '+sep
				next_row+='   '+sep
				next_nodes.extend([None,None])
				continue

			if n.data!=None:       
				buf=' '*int((5-len(str(n.data)))/2)
				cur_row+='%s%s%s'%(buf,str(n.data),buf)+sep
			else:
				cur_row+=' '*5+sep

			if n.left!=None:  
				next_nodes.append(n.left)
				next_row+=' /'+sep
			else:
				next_row+='  '+sep
				next_nodes.append(None)

			if n.right!=None: 
				next_nodes.append(n.right)
				next_row+='\ '+sep
			else:
				next_row+='  '+sep
				next_nodes.append(None)

		content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
		cur_nodes=next_nodes
		sep=' '*int(len(sep)/2) # cut separator size in half
	return content