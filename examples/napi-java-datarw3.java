	byte bData[] = new byte[132];
	nf.opendata("string_data");
	nf.getdata(bData);
	String string_data = new String(bData);