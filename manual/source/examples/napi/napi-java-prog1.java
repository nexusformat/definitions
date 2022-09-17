	try{
		NexusFile nf = new NexusFile(filename, NexusFile.NXACC_READ);
		nf.opengroup("entry1","NXentry");
		nf.finalize();
	}catch(NexusException ne) {
		// Something was wrong!
	}