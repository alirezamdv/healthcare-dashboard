# Smile-Api

### Build and run

``` 
docker build -t smile-engine . 
docker run -p 8000:8000 smile-engine

 ```

### Docs
Interactive API documentation is available at `http://127.0.0.1:8000/docs` (this is the default port used by Uvicorn's development server).
 Note: the Docker daemon host could be different.