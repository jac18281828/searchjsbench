# SearchJS Benchmark

## Benchmarking JavaScript

### Method

Timing is performed using Node.JS with the NanoTimer package.   The data set is BlockNative transaction data in formatted JSON form.   1000 confirmed transactions are included which include 2815 total events.  Filter sets are applied to each event individually and iterated for a minimum of 1000 searches. The total nanoseconds are tallied and the mean is determined.

### Hardware

Timing is performed on MacBook Pro running Docker from a Debian stable-slim base image.

#### using i7 2019 MacBook Pro (Unscientific)
#### Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz


### Caveat 

This is a 'best effort' benchmark.   The goal of this work is to produce a ballpark estimate of search performance for the package (SearchJS)[https://github.com/deitch/searchjs] for simple searches.   No effort has been made to compare wildly different hardware platforms and architectures or to be accurate to the nanosecond.

## Results

### Single Search

Search for a single low cardinality field.  All timings in nanoseconds.

```json
{
        "name": "firstfield",
        "filter": {"status":"confirmed"}
}
```

![865 ns](plot/output/singledist.jpg)

### Single Address Matching

Search for a unique matching, single address field.

```json
    {
        "name": "to1",
        "filter": {
            "to": [
                "0xC1bfcCd4c29813eDe019D00D2179Eea838a67703"
            ]
        }
    }
```

![957 ns](plot/output/lowcardinalitymatch.jpg)

### Double Address Matching

Search for two unique matching addresses.  Note the uptick in timing for multiple matching.   

```json
    {
        "name": "to2",
        "filter": {
            "to": [
                "0xC1bfcCd4c29813eDe019D00D2179Eea838a67703",
                "0x9724f51e3aFB6B2ae0A5D86fd3b88c73283BC38F"
            ]
        }
    }
```

![1977 ns](plot/output/lowcardinalitymatch2.jpg)

### Multiple Address Matching

Search for ten unique matching individual addresses.   This search is significantly more expensive.

```json
    {
        "name": "to10",
        "filter": {
            "to": [
                "0xC1bfcCd4c29813eDe019D00D2179Eea838a67703",
                "0x9724f51e3aFB6B2ae0A5D86fd3b88c73283BC38F",
                "0x91B305F0890Fd0534B66D8d479da6529C35A3eeC",
                "0xD4c64f0Fe38ecdaF0Baefd7859E18185a73b9aa3",
                "0xe66B31678d6C16E9ebf358268a790B763C133750",
                "0xDef1C0ded9bec7F1a1670819833240f027b25EfF",
                "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",
                "0x4A137FD5e7a256eF08A7De531A17D0BE0cc7B6b6",
                "0x94C43145d2AE2F99a65aC6efCCa9bD73b6DA8637",
                "0x4da08a1Bff50BE96bdeD5C7019227164b49C2bFc"
            ]
        }
    }
```

![3060 ns](plot/output/lowcardinalitymatch10.jpg)
