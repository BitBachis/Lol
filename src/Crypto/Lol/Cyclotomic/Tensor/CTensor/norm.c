#include "tensorTypes.h"

#ifdef STATS
int normrCtr = 0;
struct timespec normrTime = {0,0};
#endif

void pNormSqR (hInt_t* y, hDim_t lts, hDim_t rts, hDim_t p, hInt_t* tempSpace) {
  hDim_t blockOffset;
  hDim_t modOffset;
  hDim_t i;

  if(p==2) {
    hDim_t totm = lts*rts*(p-1);
    for (i = 0; i < totm; i++) {
      tempSpace[i] = y[i];
    }
  }
  hInt_t sum = 0;

  hDim_t tmp1 = rts*(p-1);
  for (blockOffset = 0; blockOffset < lts; ++blockOffset) {
    hDim_t tmp2 = blockOffset*tmp1;
    for (modOffset = 0; modOffset < rts; ++modOffset) {
      hDim_t tensorOffset = tmp2 + modOffset;

      for (i = 0; i < p-1; ++i) {
        sum += y[tensorOffset + i*rts];
      }
      for (i = 0; i < p-1; ++i) {
        tempSpace[tensorOffset + i*rts] = y[tensorOffset + i*rts] + sum;
      }
    }
  }
}

void ppNormSqR (void* y, PrimeExponent pe, hDim_t lts, hDim_t rts, hInt_t* tempSpace, hInt_t q) {
#ifdef DEBUG_MODE
  ASSERT (q==0);
#endif
    hDim_t p = pe.prime;
    hShort_t e = pe.exponent;
  pNormSqR ((hInt_t*)y, lts*ipow(p,e-1), rts, p, tempSpace);
}

void tensorNormSqR (hInt_t* y, hDim_t totm, PrimeExponent* peArr, hShort_t sizeOfPE) {
#ifdef STATS
    normrCtr++;
    struct timespec s1,t1;
    clock_gettime(CLOCK_REALTIME, &s1);
#endif
#ifdef DEBUG_MODE
    printf("\n\nEntered tensorNormSqR\ttotm=%" PRId32 "\tnumFacts=%" PRId16 "\n[", totm, sizeOfPE);
    hDim_t i;
    for(i = 0; i < totm; i++) {
        printf("%" PRId64 ",", y[i]);
    }
    printf("]\n[");
    for(i = 0; i < sizeOfPE; i++) {
        printf("(%" PRId32 ",%" PRId16 "),", peArr[i].prime, peArr[i].exponent);
    }
    printf("]\n");
#endif

  hInt_t* tempSpace = (hInt_t*)malloc(totm*sizeof(hInt_t));

  tensorFuserNorm (y, ppNormSqR, totm, peArr, sizeOfPE, tempSpace, 0);

  //do dot product and return in index 0
  hInt_t dotprod = 0;
  for(hDim_t i = 0; i < totm; i++) {
    dotprod += (tempSpace[i]*y[i]);
  }

  y[0] = dotprod;

  free(tempSpace);

#ifdef STATS
    clock_gettime(CLOCK_REALTIME, &t1);
    lrTime = tsAdd(normrTime, tsSubtract(t1,s1));
#endif
}