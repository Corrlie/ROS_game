import roslaunch

def run_node(pkg, exe):
    node = roslaunch.core.Node(pkg, exe)
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()
    process = launch.launch(node)
    return process
    
def close_node(process):
    process.stop()
