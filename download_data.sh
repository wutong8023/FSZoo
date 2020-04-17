#!/bin/bash
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

set -e

mkdir data
mkdir data/embeddings


# Configure download location
DOWNLOAD_PATH="./data"

# Get externally hosted data
DATASET_PATH="$DOWNLOAD_PATH/datasets"

# Get SQuAD train
wget -O "$DATASET_PATH/filename1.json"
wget -O "$DATASET_PATH/filename2.json"