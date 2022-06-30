# Copyright (c) 2022 Intel Corporation
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

# This dockerfile builds and installs the transfer learning CLI/API for PyTorch
# The default command runs training based on environment variables specifying
# the model name, dataset information, output directory, etc.

ARG BASE_IMAGE="intel/intel-optimized-pytorch"
ARG BASE_TAG="latest"

FROM ${BASE_IMAGE}:${BASE_TAG} as builder

COPY . /workspace
WORKDIR /workspace

ENV EXCLUDE_FRAMEWORK=True

RUN python setup.py bdist_wheel --universal

FROM ${BASE_IMAGE}:${BASE_TAG}

WORKDIR /workspace
ARG TLK_VERSION=0.0.1

COPY --from=builder /workspace/dist/tlk-${TLK_VERSION}-py2.py3-none-any.whl .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir tlk-${TLK_VERSION}-py2.py3-none-any.whl[pytorch] && \
    rm tlk-${TLK_VERSION}-py2.py3-none-any.whl

ENV DATASET_DIR=/workspace/data
ENV OUTPUT_DIR=/workspace/output
ENV EPOCHS=1
ENV TORCH_HOME=/tmp/torch_cache

CMD ["sh", "-c", \
     "TORCH_HOME=${OUTPUT_DIR}/torch_cache tlk train --framework pytorch --model-name ${MODEL_NAME} --output-dir ${OUTPUT_DIR} --dataset-dir ${DATASET_DIR} --epochs ${EPOCHS} --dataset-name \"${DATASET_NAME}\" "]