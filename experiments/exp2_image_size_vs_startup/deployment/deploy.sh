#!/bin/bash
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"


#small
gcloud run deploy exp2-small \
--source "$BASE_DIR/experiments/exp2_image_size_vs_startup/small_image/app" \
--region us-central1 \
--allow-unauthenticated \
--concurrency 1 \
--min-instances 0

#medium
gcloud run deploy exp2-medium \
--source "$BASE_DIR/experiments/exp2_image_size_vs_startup/medium_image/app" \
--region us-central1 \
--allow-unauthenticated \
--concurrency 1 \
--min-instances 0

#large
gcloud run deploy exp2-large \
--source "$BASE_DIR/experiments/exp2_image_size_vs_startup/large_image/app" \
--region us-central1 \
--allow-unauthenticated \
--concurrency 1 \
--min-instances 0