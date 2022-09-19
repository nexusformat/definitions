	String ame = "Alle meine Entchen";
	nf.makedata("string_data",NexusFile.NX_CHAR,
			1,ame.length()+2);
	nf.opendata("string_data");
	nf.putdata(ame.getBytes());