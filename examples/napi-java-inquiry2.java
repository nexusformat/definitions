	Hashtable h = nf.attrdir();
	Enumeration e = h.keys();
	while(e.hasMoreElements())
	{
		attname = (String)e.nextElement();
		atten = (AttributeEntry)h.get(attname);
		System.out.println("Found global attribute: " + attname +
			" type: "+ atten.type + " ,length: " + atten.length); 
	}
