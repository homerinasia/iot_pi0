# iot_pi0
code to support internet connected pi thermometer

so this is probably a somewhat loosely connected project. when its all uploaded there will be four parts
a) a python script that runs on a raspberry pi that monitors an mqtt queue and when it 'see's' a particular message, it 
queries a dsXXX digital thermometer, converts the response to fahrenheit and writes the response back to the same gueue
b) a java android app that sends a message to an mqtt queue and watches for a response. this is the 'ui' to the app
c) a python script that runs under cron and every x minutes will get the temp and send it to an elastic beanstalk 
endpoint
d) elastic beanstalk flask python app that has several endpoints
  1) reads input (time/date/temp in F) and writes it to simpledb using boto
  2) allows queries against temp data in simpledb
  there is a function that checks for anomalous temps and uses cinch to text me
  
  ..... more to come
  
