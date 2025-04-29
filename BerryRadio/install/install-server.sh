echo ""
sleep 1
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

apt-get install apache2 -y
mv server/* /var/www/html 
chown -R www-data:www-data /var/www/html/
mkdir /opt/berryradio && mkdir /opt/berryradio/msic

cd /opt/berryradio
git clone https://github.com/markondej/fm_transmitter
cd fm_transmitter
apt-get install make gcc g++
make


echo " /!\ You must have previously configured the ssh of your machine. /!\"

IP=`hostname -I | cut -d' ' -f1` && echo "Your Local IP: $IP"
port=`cat /etc/sshd_config | grep port` && echo "Your SSH Port [LOCAL]: $port"
sleep 3
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
