docker rm -f co-dashboard
docker build -t co-dashboard .
docker run -p 8080:8080 --name co-dashboard co-dashboard
