# Help Chat v0.1

This is a project in which there are 3 customer service areas (technical, administrative and sales), when executing the client, you must enter 3 parameters.

1. -h or --host, followed by this parameter, will go the ip address in which it was provided by the server to which you want to connect.
2. -p or --port, followed by this parameter, will be the port on which the server you want to connect to works.
3. -z or --zone, followed by this parameter, will be the area you want to enter to receive support, it can be any of the 3 previously mentioned.

   - Example of client execution:

    ```
    python3 main.py -host 127.0.0.1 -p 5000 -z technique
    or
    python3 main.py -host 127.0.0.1 -p 5000 -z administrative
    or
    python3 main.py -host 127.0.0.1 -p 5000 -z sales
    ```
    
Once connected, you will receive the message that you are connected to the help chat, a welcome message and you will be asked if you want to register or log in, you must enter number 1 to register or number 2 to go to the login section.
> if you are not registered, you must do so. Only registered users are allowed to log in to the system.

In both cases you must enter your username and password. Once logged in, you will be stored in a waiting queue depending on the area you have chosen, as well as the role you have ("customer" or "operator").

In case there is a customer or operator in the waiting queue corresponding to the section you entered, you will be instantly sent to a private chat, where you will be able to ask the corresponding questions in case you are a customer or give the necessary help in case you are an operator.

Once the conversation is over, either of the two people can place the command "/exit" as a message and the connection will be terminated.

> The operator will return to the waiting queue of the corresponding area until a new client enters or is assigned, and the client will be disconnected from the server.
