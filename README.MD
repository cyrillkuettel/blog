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
### Pycharm note:
There might be an issue where, if importing something start with `from app.core`, pycharm thinks the folder `fast` is unresolved.
It's incorrectly identifying syntax erros for absolute python imports.

1) Open the Project Structure settings.
2) In the 'Projects' pane of the Project Structure page, click the `fast` folder and mark it as Sources.
3) Click Apply, Ok.
