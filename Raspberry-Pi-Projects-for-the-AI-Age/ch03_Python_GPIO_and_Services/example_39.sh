curl -fsSL https://get.docker.com -o get-docker.sh
less get-docker.sh  # read a script before you run it
sudo sh get-docker.sh
sudo usermod -aG docker $USER  # log out and in afterwards
docker run --rm hello-world
