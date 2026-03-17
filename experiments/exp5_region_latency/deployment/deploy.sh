gcloud run deploy exp5-india \
  --source experiments/exp5_region_latency/app \
  --region asia-south1 \
  --allow-unauthenticated

gcloud run deploy exp5-taiwan \
  --source experiments/exp5_region_latency/app \
  --region asia-east1 \
  --allow-unauthenticated

gcloud run deploy exp5-us \
  --source experiments/exp5_region_latency/app \
  --region us-central1 \
  --allow-unauthenticated