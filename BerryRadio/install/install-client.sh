echo ""
echo "Press Enter to continue"
read touch
case $touch in
*)      echo ""
        ;;
esac
sleep 1
n=20
for x in `seq $n`
do
    for i in `seq $x`; do echo -n "#"; done
    echo -en "\r"
    sleep 0.3
done
echo ""
sleep 3

apt-get install python
apt-get install python-pip
apt-get install sshpass
apt-get install python-tk
pip install termcolor
pip install colored

mkdir /opt/berryradio
mv client/ /opt/berryradio
echo "alias berryradio='python /opt/berryradio/radio.py'" >> ~/.bashrc
bash 

echo ""
echo ""
echo "▓█████▄  ▒█████   ███▄    █ ▓█████" 
echo "▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓█   ▀"
echo "░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒███"   
echo "░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄" 
echo "░▒████▓ ░ ████▓▒░▒██░   ▓██░░▒████▒"
echo "▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░"
echo " ░ ▒  ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░"
echo " ░ ░  ░ ░ ░ ░ ▒     ░   ░ ░    ░   "
echo "   ░        ░ ░           ░    ░  ░"
echo ""
echo "[ * ]  -=  Install Done, Press a Enter to exit.  =-  [ * ]"
read touch
case $touch in
*)      echo ""
        ;;
esac
echo ""
