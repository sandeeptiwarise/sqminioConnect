## MinIO Python Client and Dockerized MinIO Cloud Storage

# Working
1. Connectivity for non default user with its access_key and secret key
2. Bucket Creation 
3. Object addition and removal
3. Bucket Destruction

# TODO
1. Mapping AWS Cognito (Openid) with the user
2. Placing user policy in, to decide do's and dont's by the user mapped with AWS Cognito ID

## Making Container Up and Running With MiniIO Cloud Storage
sudo su
docker --version
systemctl start docker
systemctl enable docker
docker pull minio/minio

docker run -t -d -p 9000:9000 --name sqminiotest \
> -e "MINIO_ACCESS_KEY=sqtestkey" \
> -e "MINIO_SECRET_KEY=sqtestsecret" \
> -v /home/dev/mdata:/data \
> minio/minio server /data 

272ada2e7e49afe6cee7a53bff12a11edb2dc5e726f5a7fc8fa1d4272adf3269

docker ps -a

CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                      PORTS                    NAMES
272ada2e7e49   minio/minio                     "/usr/bin/docker-ent…"   28 seconds ago   Up 27 seconds               0.0.0.0:9000->9000/tcp   sqminiotest

CONTAINER WITH MINIO STORAGE SERVER IS ONLINE NOW 

sudo docker container stop container_id
sudo docker container prune

## INSTALLATION OF MINIO PYTHON CLIENT

mkdir sqminioConnect

cd sqminioConnect/

python3 -m venv venv

. venv/bin/activate

pip3 install minio

pip3 freeze

pip3 freeze > requirements.txt

code .


# sudo chmod -R 757 /home/dev/mdata
# (venv).....# sudo chmod -R 757 /home/s..../MinIOProject/
