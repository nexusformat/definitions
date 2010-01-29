#include "napi.h"

 int main()
 {
   NXhandle fileID;
   NXopen ('NXfile.nxs', NXACC_CREATE, &fileID);