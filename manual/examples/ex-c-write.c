#include "napi.h"

 int main()
 {
    NXhandle fileID;
    NXopen ("NXfile.nxs", NXACC_CREATE, &fileID);
      NXmakegroup (fileID, "Scan", "NXentry");
      NXopengroup (fileID, "Scan", "NXentry");
        NXmakegroup (fileID, "data", "NXdata");
        NXopengroup (fileID, "data", "NXdata");
        /* somehow, we already have arrays tth and counts, each length n*/
          NXmakedata (fileID, "two_theta", NX_FLOAT32, 1, &n);
          NXopendata (fileID, "two_theta");
            NXputdata (fileID, tth);
            NXputattr (fileID, "units", "degrees", 7, NX_CHAR);
          NXclosedata (fileID);  /* two_theta */
          NXmakedata (fileID, "counts", NX_FLOAT32, 1, &n);
          NXopendata (fileID, "counts");
            NXputdata (fileID, counts);
          NXclosedata (fileID);  /* counts */
        NXclosegroup (fileID);  /* data */
      NXclosegroup (fileID);  /* Scan */
    NXclose (&fileID);
    return;
}
