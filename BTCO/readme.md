<!-- gcloud builds submit --tag gcr.io/<ProjectName>/<AppName>  --project=<ProjectName> -->
gcloud builds submit --tag gcr.io/btcostreamlit2/btco  --project=btcostreamlit2

<!-- gcloud run deploy --image gcr.io/<ProjectName>/<AppName> --platform managed  --project=<ProjectName> --allow-unauthenticated -->
gcloud run deploy --image gcr.io/btcostreamlit2/btco --platform managed  --project=btcostreamlit2 --allow-unauthenticated