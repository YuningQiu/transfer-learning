#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#

import argparse

from tlt.distributed.tensorflow.utils.tf_distributed_util import (
    DistributedTF,
    DistributedTrainingArguments
)


dtf = DistributedTF()
model, optimizer, loss, train_data, val_data = dtf.load_saved_objects()

if __name__ == '__main__':

    print("******Distributed Training*****")

    description = 'Distributed training with TensorFlow.'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--use_case', type=str, required=True,
                        help='Use case (image_classification|text_classification)')
    parser.add_argument('--epochs', type=int, required=False, default=1, help='Total epochs to train the model')
    parser.add_argument('--batch_size', type=int, required=False, default=128,
                        help='Global batch size to distribute data (default: 128)')
    parser.add_argument("--batch_denom", type=int, required=False, default=1,
                        help="Batch denominator to be used to divide global batch size (default: 1)")
    parser.add_argument('--shuffle', action='store_true', required=False, help="Shuffle dataset while training")
    parser.add_argument('--scaling', type=str, required=False, default='weak',
                        help='Weak or Strong scaling. For weak scaling, lr is scaled by a factor of '
                        'sqrt(batch_size/batch_denom) and uses global batch size for all the processes. For '
                        'strong scaling, lr is scaled by world size and divides global batch size by world size '
                        '(default: weak)')

    args = parser.parse_args()

    training_args = DistributedTrainingArguments(
        use_case=args.use_case,
        model=model,
        optimizer=optimizer,
        loss=loss,
        train_data=train_data,
        val_data=val_data,
        epochs=args.epochs,
        scaling=args.scaling,
        batch_size=args.batch_size,
        batch_denom=args.batch_denom,
        shuffle=args.shuffle
    )

    dtf.launch_distributed_job(training_args)
