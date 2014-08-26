	nf.opengroup(group,nxclass);
	h = nf.groupdir();
	e = h.keys();
	System.out.println("Found in vGroup entry:");
	while(e.hasMoreElements())
	{
		vname = (String)e.nextElement();
		vclass = (String)h.get(vname);
		System.out.println("     Item: " + vname + " class: " + vclass);
	}
