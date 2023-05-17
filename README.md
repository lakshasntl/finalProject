# finalProject

Our final project aims to develop an app with the students of UMD as our main users and audience. The objective of this project is to create a student-run platform that focuses on sharing real-time alerts and information related to incidents and events within the College Park community. By collecting input from College Park bystanders, our aim is to keep the community informed and alert about its surroundings to ensure their safety. Our platform will be exclusively centered on the UMD Campus and will emphasize our commitment to keeping students secure, setting us apart from other app competitors.

The project design consists of two methods that read through the UMD Alerts Page and store the alerts into a list, separated into three sections: title, date, and description. The code is organized into six main sections:

Creating the messages: This section involves parsing the HTML pages and extracting relevant information from each alert, such as the title, date, and description.

Creating the notification: Here, a notification object is created for each new alert, which will contain the date and time.

Adding titles to the notifications: This section adds the title to the current notification object.

Classifying the notifications as three different types of alerts: The notifications are classified into three types: emergency, advisory, and safety notices. This classification helps determine the appropriate actions to take for each type of alert.

Creating an icon based on the type of alert: An icon is generated for each notification based on its classification. The icon represents the nature or severity of the alert.

Adding a sound to the notification based on the type of alert: A sound is added to each notification based on its classification. The sound serves as an additional indicator or alert signal.

When encountering problems during the development process, our team engages in problem-solving discussions. We hold Zoom meetings to identify the specific challenges someone is facing and then brainstorm potential solutions. If we encounter a roadblock and cannot find a suitable solution, we seek assistance from our TA for guidance. An example of this problem-solving approach is evident in the Classify class. When our team faced difficulties, we brainstormed for solutions and sought help from the TA, which ultimately led to resolving the issues with that class.
