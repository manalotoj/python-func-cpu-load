# python-func-cpu-load
Emulate python function with high cpu load using [cpu-load-generator](https://pypi.org/project/cpu-load-generator/).

## HttpTriggerConsumeCpu Function
An http trigger that accepts the following querystring parameters:
- corenum: The index of the core to apply load against. Default is -1 which loads all cores. 
- load: The load to apply ranging from 0 to 1. Ex. 0.2, 0.5, 1. Default is .25.
- seconds: The duration in seconds to apply the load. Default is 10 seconds.  
