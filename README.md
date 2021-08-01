# Sample App

## Description

This repo Includes following files:

- #### DockerFile
    - Build Image : docker build --tag sample_app
    - To run: docker run -p 5000:5000 -d sample_app
    - To stop: docker stop imageid

- ### Using Docker Compose
    - To run: docker compose up


# About Resources

- Memory conserved during calulation were computed through the use of fllowing library

1. memory-profiler==0.58.0
2. psutil==5.8.0


* For a single request in localhost:5000/task/

    > **Required RAM resource** = approx 1563 MB  
    > **Time taken** = approx 5 secs




* For handling 10 requests/sec

    > **Required Resource** = 10 * 5* 1563 MB


Moreover, 
    >**RAM Percent** = approx 35 
    >**CPU Percent** = approx 8 
 
Since, other applications, and IDE, browswer running resource result may be up & down the computed value.

* References:
    > process = psutil.Process(os.getpid())
    print(process.memory_info().rss, "RAM Consumption in byte") 
    
    > print("--- %s seconds ---" % (time.time() - start_time))
    
    > print('The CPU usage is: ', psutil.cpu_percent(4) 

    > print('RAM memory % used:', psutil.virtual_memory()[2])

    > print('Total memory in sys excluding swap:', psutil.virtual_memory()[0])

    > print('Used Memory:', psutil.virtual_memory()[3])

    > print('Free Memory:', psutil.virtual_memory()[4])

