# DHF-Api

### Build and run

The dockerfile is used by our docker-compose.

If you want to test this api locally, you need to use the DockerfileLocal.

``` 
docker build -t dhf-api . 
docker run -p 5001:5000 dhf-api

 ```

### Docs
Interactive API documentation is available at `http://127.0.0.1:5001/docs` (this is the default port used by Uvicorn's development server).
 Note: the Docker daemon host could be different.
