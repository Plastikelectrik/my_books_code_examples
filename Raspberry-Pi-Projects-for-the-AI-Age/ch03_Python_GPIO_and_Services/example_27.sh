mkdir -p ~/projects/assistant
cd ~/projects/assistant
python3 -m venv .venv  # create the environment
source .venv/bin/activate             # activate it
pip install --upgrade pip
pip install requests                  # install packages
pip freeze > requirements.txt  # save the package list
deactivate  # leave the environment
