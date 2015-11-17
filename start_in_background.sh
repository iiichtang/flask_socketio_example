network_tmp=/home/ec2-user/script/network_tmp.txt
netstat -tunlp > ${network_tmp}
#store the netstat result into network_tmp
testing=$(grep ":5000" ${network_tmp})
#check if the port is been used
if [ "${testing}" != "" ]; then
        echo ${testing}
        echo "port is occupied by the other program"
        tmp=${testing#*_}
        data=${tmp%/*}
        flask=$(echo ${data} | cut -d' ' -f 7)
        echo ${flask}
        #echo ${flask_pid}
        kill ${flask}
fi

source /home/ec2-user/websocket/venv/bin/activate
nohup python /home/ec2-user/websocket/flask-socketIO/test.py >/dev/null 2>&1 &
deactivate