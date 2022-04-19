# MoveOn
Fitness tracking based on IOS kinematics data
# Problem statement 
Automation brings the advacement of technology reduce the efforts and has wide usecases. In todays world fitness has been given a lot of importance and many fitness tracking devices like smart watch are present into the market which uses sensors and gives status of one's activity. IOS device has sensors installed in it accelerometer and gyroscope. Using this devices the motion and location of the device is tracked.
 
# Data 
The data is available on Kaggle and it consist of accelerometer and gyroscope readings of an IOS device of a user. 
We did the primary reaserch on data to find out it's insights which are written in 'SensorsInfo.txt' in 'Documentation' folder in our words. here is the link of data which is present on Kaggle

Data link - https://www.kaggle.com/datasets/yasserh/kinematics-motion-data


# What is MoveOn 
MoveOn is a machine learning algorithm that uses the data collected from IOS devices and gives the status of motion of user. when the data is fed MoveOn predicts whether user is walking or running.

MoveOn solves binary classification problem.

The whole project is built using 'Big Data Technologies' because data contains more than 80000 rows hence it can be considered as big data. Moreover aknowledging real life scenario one IOS user will generate very big data where MoveOn model can be implemented.

# Technologies Used
* Hdfs : to store data file in distributed fashion
* Hive table : to make data structured and query it easily
* Pyspark : for implementation of machine learning algorithm
* Python : to integrate project
* T-kinter : for UI 
* PowerBI dashboard : to visualize data

Note : For hive table commands file name sql_hive.txt is uploaded and for setting hdfs files commands.sh is uploaded.

# Implementation video
* https://www.linkedin.com/posts/aykorde_project-pyspark-machinelearning-activity-6921774261321826304--DH9?utm_source=linkedin_share&utm_medium=member_desktop_web
