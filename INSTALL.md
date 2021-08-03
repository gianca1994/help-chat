# Guide to install the help chat v0.1
### You will not need to install any libraries. 

1. First step, clone the repository: ```git clone https://github.com/gianca1994/help-chat```

2. Second step, run the server, first we enter the server folder: ```cd server```

3. Then we launch the server: ```python3 main.py (-p or --port) "port on which we want to run the server"```
   - For example: ```python3 main.py -p 5000``` or ```python main.py --port 5000```
   
4. Once the server is running, run another terminal and execute the command: ```cd client```

5. Then we launch the client ```python3 main.py (-h or --host) "server ip address" (-p or --port) "server port" (-z or --zone) "area you want to access"```
   - For example: ```python3 main.py -h 127.0.0.1 -p 5000 -z administrative``` or ```python3 main.py --host 127.0.0.1 --port 5000 --zone technique```

> Once this is done, the server is running and the client is connected, it is possible to connect multiple clients to the same server.
