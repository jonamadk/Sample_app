from flask import Flask
import os , psutil


import time
start_time = time.time()

app = Flask('test')


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)




@app.route("/task/")
def task():
    """simple function to add cpu and memory"""
  
       
    number = 35
    list_data = [1.0] * 200000000
    data = fib(number)
   
 
   
  
# Memory usage
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss, "RAM Consumption in byte") 
    print("--- %s seconds ---" % (time.time() - start_time))
    print('The CPU usage is: ', psutil.cpu_percent(4))
    print('RAM memory % used:', psutil.virtual_memory()[2])
    print('Total memory in sys excluding swap:', psutil.virtual_memory()[0])
    print('Used Memory:', psutil.virtual_memory()[3])
    print('Free Memory:', psutil.virtual_memory()[4])
   
   
    return "Your number {} and {}".format(data,  psutil.virtual_memory()[3])


@app.route("/")
def cluster_1():
    return "welcome to test"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
