* Pyaudio depends on portaudio, which is a C module. Conda is probably the quickest way to install pyaudio using: "conda install pyaudio -y"
* Linux can install python3-pyaudio using: "apt install python3-pyaudio -y"
* MacOS can install portaudio with Brew: "brew install portaudio"
* If you need brew, then run: ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
* Install the rest of the Python packages with: python3 -m pip install -r requirements.txt
* Install the MPEG layer 1/2/3 player using: "apt install mpg123 -y"
