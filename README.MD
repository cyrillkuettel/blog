# blog

## deploy
sudo ./run-prod.sh
The init-letsencrypt.sh should generally not be touched (only run once). 
It will replace the existing certificate.


## development
Quick start, just use this for a local development server. Don't use this in production.

```bash
https://github.com/cyrillkuettel/blog
cd blog/fast
uvicorn app.main:app --reload
```
