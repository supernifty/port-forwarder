port-forwarder
==============

Simple Python scripts to listen, log and forward network traffic

This script supports python 2 and 3 by making use of `future` which should be installed using `pip install future`.

Usage
-----
* Use forward-tcp.py to forward TCP traffic
* Use forward-udp.py to forward UDP traffic
* Edit the file and set listen_host, listen_port, target_host, target_port
* python forward-*.py
* Output is written to stdout

* proxy.py forwards HTTP traffic

Other Proxies
-------------
* SMTP: python -m smtpd -c DebuggingServer -n localhost:25

