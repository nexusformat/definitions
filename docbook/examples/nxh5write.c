/**
 * This is an example how to write a valid NeXus file
 * using the HDF-5 API alone. Ths structure which is 
 * going to be created is:
 *
 * scan:NXentry
 *      data:NXdata
 *         counts[]
 *            @signal=1
 *         two_theta[]
 *            @units=degrees
 *
 *  WARNING: each of the HDF function below needs to be 
 *  wrapped into something like:
 *
 *  if((hdfid = H5function(...)) < 0){
 *     handle error gracefully  
 *  }  
 *  I left the error checking out in order to keep the 
 *  code clearer
 * 
 *  This also installs a link from /scan/data/two_theta to /scan/hugo
 * 
 *  Mark Koennecke, October 2011
 */
#include <hdf5.h>
#include <stdlib.h>
#include <string.h>

#define LENGTH 400
int main(int argc, char *argv[])
{
  float two_theta[LENGTH];
  int counts[LENGTH], i, rank, signal;

  /* HDF-5 handles */
  hid_t fid, fapl, gid, atts, atttype, attid;
  hid_t datatype, dataspace, dataprop, dataid;
  hsize_t dim[1], maxdim[1];


  /* create some data: nothing NeXus or HDF-5 specific */
  for(i = 0; i < LENGTH; i++){
    two_theta[i] = 10. + .1*i;
    counts[i] = (int)(1000 * ((float)random()/(float)RAND_MAX));
  }
  dim[0] = LENGTH;
  maxdim[0] = LENGTH;
  rank = 1;


 
  /*
   * open the file. The file attribute forces normal file 
   * closing behaviour down HDF-5's throat
   */
  fapl = H5Pcreate(H5P_FILE_ACCESS);
  H5Pset_fclose_degree(fapl,H5F_CLOSE_STRONG);
  fid = H5Fcreate("NXfile.h5", H5F_ACC_TRUNC, H5P_DEFAULT,fapl);  
  H5Pclose(fapl);


  /*
   * create scan:NXentry
   */
  gid = H5Gcreate(fid, (const char *)"scan",0);
  /*
   * store the NX_class attribute. Notice that you
   * have to take care to close those hids after use
   */
  atts = H5Screate(H5S_SCALAR);
  atttype = H5Tcopy(H5T_C_S1);
  H5Tset_size(atttype, strlen("NXentry"));
  attid = H5Acreate(gid,"NX_class", atttype, atts, H5P_DEFAULT);
  H5Awrite(attid, atttype, (char *)"NXentry");
  H5Sclose(atts);
  H5Tclose(atttype);
  H5Aclose(attid);

  /*
   * same thing for data:Nxdata in scan:NXentry.
   * A subroutine would be nice to have here.......
   */
  gid = H5Gcreate(fid, (const char *)"/scan/data",0);
  atts = H5Screate(H5S_SCALAR);
  atttype = H5Tcopy(H5T_C_S1);
  H5Tset_size(atttype, strlen("NXdata"));
  attid = H5Acreate(gid,"NX_class", atttype, atts, H5P_DEFAULT);
  H5Awrite(attid, atttype, (char *)"NXdata");
  H5Sclose(atts);
  H5Tclose(atttype);
  H5Aclose(attid);

  /*
   * store the counts dataset
   */
  dataspace = H5Screate_simple(rank,dim,maxdim);
  datatype = H5Tcopy(H5T_NATIVE_INT);  
  dataprop = H5Pcreate(H5P_DATASET_CREATE);
  dataid = H5Dcreate(gid,(char *)"counts",datatype,dataspace,dataprop);
  H5Dwrite(dataid, datatype, H5S_ALL, H5S_ALL, H5P_DEFAULT, counts);
  H5Sclose(dataspace);
  H5Tclose(datatype);
  H5Pclose(dataprop);  
  /*
   * set the signal=1 attribute 
   */
  atts = H5Screate(H5S_SCALAR);
  atttype = H5Tcopy(H5T_NATIVE_INT);
  H5Tset_size(atttype,1);
  attid = H5Acreate(dataid,"signal", atttype, atts, H5P_DEFAULT);
  signal = 1;
  H5Awrite(attid, atttype, &signal);
  H5Sclose(atts);
  H5Tclose(atttype);
  H5Aclose(attid);

  H5Dclose(dataid);

  /*
   * store the two_theta dataset
   */
  dataspace = H5Screate_simple(rank,dim,maxdim);
  datatype = H5Tcopy(H5T_NATIVE_FLOAT);  
  dataprop = H5Pcreate(H5P_DATASET_CREATE);
  dataid = H5Dcreate(gid,(char *)"two_theta",datatype,dataspace,dataprop);
  H5Dwrite(dataid, datatype, H5S_ALL, H5S_ALL, H5P_DEFAULT, two_theta);
  H5Sclose(dataspace);
  H5Tclose(datatype);
  H5Pclose(dataprop);  

  /*
   * set the units attribute
   */
  atttype = H5Tcopy(H5T_C_S1);
  H5Tset_size(atttype, strlen("degrees"));
  atts = H5Screate(H5S_SCALAR);
  attid = H5Acreate(dataid,"units", atttype, atts, H5P_DEFAULT);
  H5Awrite(attid, atttype, (char *)"degrees");
  H5Sclose(atts);
  H5Tclose(atttype);
  H5Aclose(attid);
 /*
   * set the target attribute for linking
   */
  atttype = H5Tcopy(H5T_C_S1);
  H5Tset_size(atttype, strlen("/scan/data/two_theta"));
  atts = H5Screate(H5S_SCALAR);
  attid = H5Acreate(dataid,"target", atttype, atts, H5P_DEFAULT);
  H5Awrite(attid, atttype, (char *)"/scan/data/two_theta");
  H5Sclose(atts);
  H5Tclose(atttype);
  H5Aclose(attid);


  H5Dclose(dataid);

  /*
   * make a link in /scan to /scan/data/two_theta, thereby 
   * renaming two_theta to hugo
   */
  H5Glink(fid,H5G_LINK_HARD,"/scan/data/two_theta","/scan/hugo");

  /*
   * close the file 
   */
  H5Fclose(fid);
}
