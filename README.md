
## Acknowledgements

This repo is a fork of Uber AI Labs's repo at https://github.com/uber-research/deep-neuroevolution. Please see their
README.md for further details on the repo structure and papers used during the research.

We could not have done our work without their research. This repo builds off of their work to explore the effect of
using custom, handcoded behavior characterizations (BCs) for the Atari game environment

## How to run locally

Simply run the `run_all.sh` script with the necessary arguments: `algorithm`, `path to config file`, `path to log directory`

Example:

```
./run_all.sh nsr-es configurations/frostbite_nsres.json logs_dir
```

## Our results

Our results are all in the `Experiments` folder. Note that there are several branches, each with their own BC or
similarity metric implementation, and that further results could be on those branches as well
