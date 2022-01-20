import logging

import azure.functions as func
from cpu_load_generator import load_single_core, load_all_cores, from_profile

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # variable = something if condition else something_else

    core_num = -1
    load = .25
    duration = 10

    if req.params.get('corenum') is not None: core_num = int(req.params.get('corenum'))
    if req.params.get('load') is not None: load = float(req.params.get('load'))
    if req.params.get('seconds') is not None: duration = int(req.params.get('seconds'))
    
    if core_num == -1:
        load_all_cores(duration_s=duration, target_load=load)
    else:
        load_single_core(core_num=core_num, duration_s=duration, target_load=load)
    return func.HttpResponse(
            f"HTTP triggered function applied a load of {load} to core index {core_num} over {duration} seconds.",
            status_code=200
    )