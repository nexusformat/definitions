	int idata[][] = new idata[10][20];
	int iDim[] = new int[2];

	// put some data into idata.......

	// write idata
	iDim[0] = 10;
	iDim[1] = 20;
	nf.makedata("idata",NexusFile.NX_INT32,2,iDim);
	nf.opendata("idata");
	nf.putdata(idata);

	// read idata
	nf.getdata(idata);