{-|
Module      : BenchLolCPPMain
Description : Main driver for lol benchmarks with CPP.
Copyright   : (c) Eric Crockett, 2011-2017
                  Chris Peikert, 2011-2017
License     : GPL-3
Maintainer  : ecrockett0@email.com
Stability   : experimental
Portability : POSIX

Main driver for lol benchmarks with CPP.
-}

{-# LANGUAGE DataKinds             #-}
{-# LANGUAGE DuplicateRecordFields #-}
{-# LANGUAGE NoStarIsType          #-}
{-# LANGUAGE TypeOperators         #-}

module BenchLolCPPMain where

import Crypto.Lol.Benchmarks
import Crypto.Lol.Cyclotomic.Tensor.CPP
import Crypto.Lol.Factored
import Crypto.Random.DRBG

import Data.Proxy

-- choose which layers of Lol to benchmark
ls :: [String]
ls = [
  "Tensor",
  "Cyc",
  "CycRep"
  ]

-- choose which operations to benchmark
bs :: [String]
bs = [
  "zipWith (*)",
  "crt",
  "crtInv",
  "l",
  "lInv",
  "*g Pow",
  "*g Dec",
  "*g CRT",
  "divG Pow",
  "divG Dec",
  "divG CRT",
  "lift",
  "error",
  "twacePow",
  "twaceDec",
  "twaceCRT",
  "embedPow",
  "embedDec",
  "embedCRT"
  ]

main :: IO ()
main = diagnosticMain

diagnosticMain :: IO ()
diagnosticMain = do
  let opts = defaultDiagnosticOpts{levels=ls, benches=bs}
      b1 = bgroup "Single Index"
           [oneIdxBenches (Proxy::Proxy '(F64*F9*F25, Zq 14401)) (Proxy::Proxy CT) (Proxy::Proxy HashDRBG)]
      b2 = bgroup "Twace-Embed"
           [twoIdxBenches (Proxy::Proxy '(F64*F9*F25, F64*F9*F25, Zq 14401)) (Proxy::Proxy CT)]
  mapM_ (prettyBenchesDiagnostic opts) [b1,b2]
