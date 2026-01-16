docker build -t first-example .
docker images
docker run first-example
docker run -it first-example
docker ps
docker ps -a
docker start 4cb0923a2c33
docker stop 4cb0923a2c33

docker build -t workingtimoxichmain/11112025:0.0.1 .
docker push workingtimoxichmain/11112025:0.0.1
docker run --platform=linux/amd64 -it workingtimoxichmain/11112025:0.0.1;
