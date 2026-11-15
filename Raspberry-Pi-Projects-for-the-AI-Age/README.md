# Code examples — Raspberry Pi Projects for the AI Age

Every numbered example from the book, organized by chapter.
Each file is named after its number in the book (Example 01 -> example_01.*).

## How to use

1. Create and activate a Python virtual environment (see Appendix A).
2. Install the libraries: `pip install numpy matplotlib opencv-python scikit-learn pyserial pytest flask pybullet joblib`.
3. Run desktop examples with `python3 example_NN.py` from inside their chapter folder.
4. Arduino examples (`.ino`): open them in the Arduino IDE (each sketch must be inside a folder with the same name; the IDE offers to create it).
5. MicroPython examples: copy them to the ESP32 with Thonny and save them as `main.py` to run at startup.
6. ROS 2 examples: place them in a ROS 2 package as described in the book.

## Files that other examples import

Some later examples import earlier ones by module name. Those files are included a second time under the required name (for example `rover.py`). Keep them in the same folder as the program that imports them.

## Safety and license

Examples are provided as is, without warranty, for learning. Read the safety notes in the book before running anything that moves hardware. The code is released under the MIT License (see the LICENSE file in the root of this repository). Third-party libraries keep their own licenses (see the appendix on third-party software).

## List of examples

| Folder | File | Title | Type |
|---|---|---|---|
| appendix_A_GPIO_and_Electronics_Reference | example_161.py | Calculating a series resistor for an LED | desktop (runs without hardware) |
| appendix_A_GPIO_and_Electronics_Reference | example_162.py | Checking a voltage divider | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_163.py | A fan curve with hysteresis | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_164.py | fan.py: controlling the fan with PWM | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_165.sh | Checking the I2C bus | command / config |
| appendix_H_Bonus_Mini_Projects | example_166.py | Daily climate summary from logged readings | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_167.py | Mapping security states to LED colors | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_168.py | Analyzing latency and packet loss | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_169.py | Generating the kiosk page from a notes file | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_170.ini | ~/.config/autostart/kiosk.desktop (Exec is one line) | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_171.py | Night light logic: time window and timeout | desktop (runs without hardware) |
| appendix_H_Bonus_Mini_Projects | example_172.py | Calibrated soil moisture and a one-time reminder | desktop (runs without hardware) |
| appendix_I_Templates_and_Worksheets | example_173.toml | settings.toml: a configuration file template | desktop (runs without hardware) |
| appendix_I_Templates_and_Worksheets | example_174.py | main.py: a robust skeleton for a long-running program | desktop (runs without hardware) |
| appendix_I_Templates_and_Worksheets | example_175.ini | /etc/systemd/system/my-project.service | desktop (runs without hardware) |
| appendix_I_Templates_and_Worksheets | example_176.yaml | docker-compose.yml: template for a home service | desktop (runs without hardware) |
| appendix_I_Templates_and_Worksheets | example_177.sh | backup.sh: template for a dated backup with rotation | command / config |
| appendix_I_Templates_and_Worksheets | example_178.md | build_log.md: a build log template | desktop (runs without hardware) |
| ch01_The_Raspberry_Pi_Today | example_01.sh | Updating Raspberry Pi OS | command / config |
| ch01_The_Raspberry_Pi_Today | example_02.sh | Checking and updating the bootloader firmware | command / config |
| ch01_The_Raspberry_Pi_Today | example_03.sh | Quick health check | command / config |
| ch02_Linux_Essentials_for_Makers | example_04.sh | A typical prompt | command / config |
| ch02_Linux_Essentials_for_Makers | example_05.sh | Navigating the file system | command / config |
| ch02_Linux_Essentials_for_Makers | example_06.sh | Creating, copying, moving and deleting | command / config |
| ch02_Linux_Essentials_for_Makers | example_07.sh | Looking inside files | command / config |
| ch02_Linux_Essentials_for_Makers | example_08.sh | Editing a file with nano | command / config |
| ch02_Linux_Essentials_for_Makers | example_09.sh | Running a command as administrator | command / config |
| ch02_Linux_Essentials_for_Makers | example_10.sh | Permissions in a file listing | command / config |
| ch02_Linux_Essentials_for_Makers | example_11.sh | Changing permissions and ownership | command / config |
| ch02_Linux_Essentials_for_Makers | example_12.sh | Showing your groups | command / config |
| ch02_Linux_Essentials_for_Makers | example_13.sh | Managing software packages | command / config |
| ch02_Linux_Essentials_for_Makers | example_14.sh | System monitoring commands | command / config |
| ch02_Linux_Essentials_for_Makers | example_15.sh | Network commands | command / config |
| ch02_Linux_Essentials_for_Makers | example_16.sh | Setting a static IP address with NetworkManager | command / config |
| ch02_Linux_Essentials_for_Makers | example_17.sh | Connecting with SSH | command / config |
| ch02_Linux_Essentials_for_Makers | example_18.sh | Creating and installing an SSH key (on your own computer) | command / config |
| ch02_Linux_Essentials_for_Makers | example_19.sh | Copying files over SSH | command / config |
| ch02_Linux_Essentials_for_Makers | example_20.sh | Controlling services with systemctl | command / config |
| ch02_Linux_Essentials_for_Makers | example_21.sh | Example crontab entries | command / config |
| ch02_Linux_Essentials_for_Makers | example_22.sh | Editing the boot configuration | command / config |
| ch02_Linux_Essentials_for_Makers | example_23.sh | Backing up config.txt | command / config |
| ch02_Linux_Essentials_for_Makers | example_24.sh | A simple system report script (report.sh) | command / config |
| ch02_Linux_Essentials_for_Makers | example_25.sh | Finding help | command / config |
| ch03_Python_GPIO_and_Services | example_26.sh | Checking the Python version | command / config |
| ch03_Python_GPIO_and_Services | example_27.sh | Creating and using a virtual environment | command / config |
| ch03_Python_GPIO_and_Services | example_28.py | Decoding the throttled status of a Raspberry Pi | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_29.py | Reading the real value on the Raspberry Pi | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_30.py | Reading the processor temperature from Linux | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_31.py | Blinking an LED and reacting to a button | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_32.py | A button with debouncing and a hold action | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_33.py | Testing debounce logic without hardware | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_34.py | Reading settings from a TOML configuration file | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_35.py | Logging with levels and time stamps | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_36.py | health_monitor.py: a long-running monitoring program | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_37.ini | /etc/systemd/system/health.service | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_38.sh | Enabling and checking your own service | command / config |
| ch03_Python_GPIO_and_Services | example_39.sh | Installing Docker Engine (official script) | command / config |
| ch03_Python_GPIO_and_Services | example_40.yaml | docker-compose.yml: a simple service in a container | desktop (runs without hardware) |
| ch03_Python_GPIO_and_Services | example_41.sh | Starting, checking and stopping containers | command / config |
| ch03_Python_GPIO_and_Services | example_42.sh | Basic Git workflow | command / config |
| ch04_Planning_Tools_and_Safety | example_43.py | A power budget calculator | desktop (runs without hardware) |
| ch04_Planning_Tools_and_Safety | example_44.sh | backup_config.sh: archive important files with a date | command / config |
| ch04_Planning_Tools_and_Safety | example_45.sh | Creating an image file of a card (on a Linux PC) | command / config |
| ch04_Planning_Tools_and_Safety | example_46.py | buildlog.py: append time-stamped notes to a log | desktop (runs without hardware) |
| ch05_Project_1_The_Mini_PC_Hardware_and_Operating_Syste | example_47.sh | Checking that the NVMe SSD is detected | command / config |
| ch05_Project_1_The_Mini_PC_Hardware_and_Operating_Syste | example_48.sh | Choosing NVMe as the boot device | command / config |
| ch05_Project_1_The_Mini_PC_Hardware_and_Operating_Syste | example_49.sh | Showing the bootloader configuration | command / config |
| ch05_Project_1_The_Mini_PC_Hardware_and_Operating_Syste | example_50.py | Decoding the Raspberry Pi 5 BOOT_ORDER value | desktop (runs without hardware) |
| ch05_Project_1_The_Mini_PC_Hardware_and_Operating_Syste | example_51.py | A simple storage speed test | desktop (runs without hardware) |
| ch05_Project_1_The_Mini_PC_Hardware_and_Operating_Syste | example_52.ini | Enabling PCIe Gen 3 (not officially certified) | desktop (runs without hardware) |
| ch05_Project_1_The_Mini_PC_Hardware_and_Operating_Syste | example_53.sh | Confirming that the root file system is on NVMe | command / config |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_54.sh | install_apps.sh: install the mini PC software set | command / config |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_55.sh | Installing Samba | command / config |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_56.ini | A private Samba share in /etc/samba/smb.conf | desktop (runs without hardware) |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_57.sh | Setting a Samba password and restarting | command / config |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_58.sh | Installing and checking the printing system | command / config |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_59.sh | Checking swap and memory | command / config |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_60.py | sysdash.py: a text dashboard for system health | desktop (runs without hardware) |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_61.sh | Enabling automatic security updates | command / config |
| ch06_Project_1_The_Mini_PC_Software_Tuning_and_Maintena | example_62.sh | Reading the board's power sensors | command / config |
| ch07_Project_2_The_Arcade_Console_How_Emulation_Works | example_63.py | A minimal CHIP-8 emulator core | desktop (runs without hardware) |
| ch07_Project_2_The_Arcade_Console_How_Emulation_Works | example_64.py | An input lag budget calculator | desktop (runs without hardware) |
| ch07_Project_2_The_Arcade_Console_How_Emulation_Works | example_65.sh | Installing open-source games on Raspberry Pi OS | command / config |
| ch08_Project_2A_The_Console_in_a_Case | example_66.py | Sorting homebrew games into system folders | desktop (runs without hardware) |
| ch08_Project_2A_The_Console_in_a_Case | example_67.sh | backup_saves.sh: back up Batocera saves over the network | command / config |
| ch09_Project_2B_The_Bartop_Arcade_Cabinet | example_68.py | Planning arcade GPIO pins and generating gpio-key lines | desktop (runs without hardware) |
| ch09_Project_2B_The_Bartop_Arcade_Cabinet | example_69.ini | One gpio-key overlay line in /boot/firmware/config.txt | desktop (runs without hardware) |
| ch09_Project_2B_The_Bartop_Arcade_Cabinet | example_70.sh | Testing the GPIO keys with evtest | command / config |
| ch09_Project_2B_The_Bartop_Arcade_Cabinet | example_71.py | arcade_mapper.py: GPIO buttons to a virtual keyboard | desktop (runs without hardware) |
| ch09_Project_2B_The_Bartop_Arcade_Cabinet | example_72.sh | Installing python-evdev and allowing uinput access | command / config |
| ch10_Project_3_The_Touchscreen_Media_Center_How_Media_W | example_73.py | Bitrate, file size and network headroom | desktop (runs without hardware) |
| ch11_Project_3_Building_the_Media_Center | example_74.sh | Editing the boot configuration on LibreELEC | command / config |
| ch11_Project_3_Building_the_Media_Center | example_75.ini | Touch Display 2 overlay with rotation (choose your size) | desktop (runs without hardware) |
| ch11_Project_3_Building_the_Media_Center | example_76.sh | Finishing the configuration change | command / config |
| ch11_Project_3_Building_the_Media_Center | example_77.py | Checking media file names before scanning | desktop (runs without hardware) |
| ch11_Project_3_Building_the_Media_Center | example_78.py | kodi_rpc.py: a small JSON-RPC client for Kodi | desktop (runs without hardware) |
| ch11_Project_3_Building_the_Media_Center | example_79.py | A sleep timer that fades out and stops playback | desktop (runs without hardware) |
| ch12_Project_4_The_Voice_Assistant_How_It_Works | example_80.py | An energy-based voice activity detector | desktop (runs without hardware) |
| ch12_Project_4_The_Voice_Assistant_How_It_Works | example_81.py | A latency budget for the voice assistant | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_82.sh | Installing system packages for audio | command / config |
| ch13_Project_4_Building_the_Voice_Assistant | example_83.sh | Listing audio devices | command / config |
| ch13_Project_4_Building_the_Voice_Assistant | example_84.sh | Recording and playing a test sample | command / config |
| ch13_Project_4_Building_the_Voice_Assistant | example_85.sh | Creating the voice assistant environment | command / config |
| ch13_Project_4_Building_the_Voice_Assistant | example_86.sh | Downloading the wake word models and a Piper voice | command / config |
| ch13_Project_4_Building_the_Voice_Assistant | example_87.py | audio.py: microphone and speaker helpers | hardware / ROS 2 |
| ch13_Project_4_Building_the_Voice_Assistant | example_88.py | wake_test.py: testing the wake word detector | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_89.py | record_command(): recording until the speaker stops | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_90.py | stt.py: speech-to-text with faster-whisper | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_91.py | intents.py: a rule-based intent parser with tests | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_92.py | skills.py: a background timer and a notes file | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_93.py | Switching a smart plug with MQTT | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_94.py | tts.py: speaking with Piper | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_95.py | The assistant's state machine, tested with events | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_96.py | assistant.py: the complete voice assistant | desktop (runs without hardware) |
| ch13_Project_4_Building_the_Voice_Assistant | example_97.ini | /etc/systemd/system/assistant.service | desktop (runs without hardware) |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_98.sh | Installing Ollama with the official script | command / config |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_99.sh | Downloading and testing a small model | command / config |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_100.py | llm.py: calling the local model through Ollama | desktop (runs without hardware) |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_101.py | The system prompt of the assistant | desktop (runs without hardware) |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_102.py | The tool prompt: the model must choose a tool | desktop (runs without hardware) |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_103.py | Validating the model's tool calls | desktop (runs without hardware) |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_104.py | brain.py: rules first, then the language model | desktop (runs without hardware) |
| ch14_Project_4_Giving_the_Assistant_an_AI_Brain | example_105.py | Turning a token stream into sentences for speech | desktop (runs without hardware) |
| ch15_Project_5_The_AI_Chatbot_Concepts | example_106.py | Estimating context use and waiting time | desktop (runs without hardware) |
| ch15_Project_5_The_AI_Chatbot_Concepts | example_107.py | How temperature changes the probabilities | desktop (runs without hardware) |
| ch15_Project_5_The_AI_Chatbot_Concepts | example_108.py | Retrieval with TF-IDF and cosine similarity | desktop (runs without hardware) |
| ch15_Project_5_The_AI_Chatbot_Concepts | example_109.py | Building a RAG prompt with sources | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_110.sh | Downloading the chat and embedding models | command / config |
| ch16_Project_5_Building_the_Chatbot_Server | example_111.sh | Creating the chatbot project | command / config |
| ch16_Project_5_Building_the_Chatbot_Server | example_112.py | index_docs.py: building the embedding index | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_113.py | retrieve.py: top-k retrieval with a minimum score | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_114.py | app.py: the chatbot web application | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_115.py | Speech routes in app.py | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_116.html | static/index.html: the chat page (simplified) | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_117.sh | Creating a self-signed certificate | command / config |
| ch16_Project_5_Building_the_Chatbot_Server | example_118.py | A simple password check for all routes | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_119.ini | /etc/systemd/system/chatbot.service | desktop (runs without hardware) |
| ch16_Project_5_Building_the_Chatbot_Server | example_120.py | Scoring chatbot answers against expected facts | desktop (runs without hardware) |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_121.sh | Updating and enabling automatic security updates | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_122.ini | /etc/ssh/sshd_config.d/10-hardening.conf | desktop (runs without hardware) |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_123.sh | Testing and applying the SSH configuration | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_124.sh | A basic firewall with ufw | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_125.sh | Showing SSH log messages | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_126.py | Analyzing SSH log messages | desktop (runs without hardware) |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_127.sh | Installing the CrowdSec engine and firewall bouncer | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_128.sh | Testing a manual CrowdSec decision | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_129.sh | Listing listening network services | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_130.sh | Disabling an unneeded service | command / config |
| ch17_Project_6_The_Security_Suite_Foundations_and_Harde | example_131.sh | Running a Lynis security audit | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_132.sh | Installing Pi-hole with the official installer | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_133.sh | Setting the Pi-hole admin password | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_134.sh | Opening the firewall for Pi-hole (home network only) | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_135.sh | Testing DNS through Pi-hole | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_136.sh | Installing Unbound | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_137.yaml | /etc/unbound/unbound.conf.d/pi-hole.conf | desktop (runs without hardware) |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_138.sh | Testing Unbound | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_139.py | pihole_stats.py: reading statistics through the API | desktop (runs without hardware) |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_140.sh | Installing WireGuard and creating the server keys | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_141.ini | /etc/wireguard/wg0.conf (server) | desktop (runs without hardware) |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_142.sh | /etc/wireguard/nat.sh: masquerading for VPN clients | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_143.sh | Forwarding and firewall rules for WireGuard | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_144.py | Generating WireGuard client configurations | desktop (runs without hardware) |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_145.sh | Starting WireGuard | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_146.sh | Showing a client configuration as a QR code | command / config |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_147.py | Detecting unknown devices from the neighbor table | desktop (runs without hardware) |
| ch18_Project_6_Network_Protection_DNS_Filtering_VPN_and | example_148.py | notify.py: sending a notification through ntfy | desktop (runs without hardware) |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_149.py | Motion detection by frame differencing | desktop (runs without hardware) |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_150.yaml | mediamtx.yml (excerpt): publishing the Pi camera | desktop (runs without hardware) |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_151.sh | Checking the Hailo device | command / config |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_152.yaml | ~/frigate/docker-compose.yml | desktop (runs without hardware) |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_153.yaml | ~/frigate/config/config.yml (minimal example) | desktop (runs without hardware) |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_154.sh | Starting Frigate | command / config |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_155.sh | Installing the Mosquitto MQTT broker | command / config |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_156.py | An alert policy for Frigate events | desktop (runs without hardware) |
| ch19_Project_6_Smart_Cameras_and_the_Security_Dashboard | example_157.py | Combining health checks into an overall status | desktop (runs without hardware) |
| ch20_Bringing_It_All_Together | example_158.py | Connecting a camera alert to the media center | desktop (runs without hardware) |
| ch20_Bringing_It_All_Together | example_159.py | Planning services per board by memory | desktop (runs without hardware) |
| ch20_Bringing_It_All_Together | example_160.py | A maintenance reminder | desktop (runs without hardware) |
