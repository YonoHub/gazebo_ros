import subprocess
import os
import time


class Gazebo:
    def on_start(self):
        """This block is used to launch gazebo in noVNC
        it builds the ros workspace, source it , then run a launch file
        which run gazebo ros and load the appropriate world file.  
        """
        self.ws_path = self.get_property("ws_path")
        self.pkg_name = self.get_property("pkg_name")
        self.launch_file = self.get_property("launch_file")
        subprocess.Popen("sh /usr/local/bin/start_desktop.sh", shell=True)
        time.sleep(5)
        self.alert("Building the ROS Workspace", "INFO")
        subprocess.run(
            "cd {} && . /opt/ros/melodic/setup.sh && catkin_make".format(self.ws_path),
            shell=True,
        )
        self.alert("Starting Gazebo", "INFO")
        subprocess.Popen(
            "vglrun bash -c 'source {}devel/setup.bash && roslaunch {} {}'".format(
                os.path.join(self.ws_path, ""), self.pkg_name, self.launch_file
            ),
            shell=True,
        )
