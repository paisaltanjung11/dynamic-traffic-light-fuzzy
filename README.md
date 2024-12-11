# Dynamic AI-Powered Traffic Lights for Pedestrian Crossings  

An intelligent traffic light system leveraging Artificial Intelligence (AI) to optimize pedestrian safety and crossing efficiency. Built with fuzzy logic, real-time data integration, and a user-friendly interface, this project is designed to address the challenges of traffic management in urban environments.

---

## Overview

The **Dynamic AI-Powered Traffic Lights** project aims to develop a responsive system that dynamically adjusts traffic light durations for pedestrians based on real-time conditions. By integrating fuzzy logic with APIs like TomTom Traffic and OpenCage Geocoding, the system enhances urban mobility, reduces pedestrian waiting times, and promotes adherence to traffic rules.

### Objectives:
1. **Optimize Pedestrian Crossing Durations**: Adjust traffic light timings dynamically to minimize waiting time.
2. **Enhance Safety**: Reduce accident risks by ensuring sufficient crossing times.
3. **Support Sustainable Cities**: Contribute to Sustainable Development Goal 11 by promoting efficient and pedestrian-friendly traffic systems.

---

## Features

- **Adaptive Fuzzy Logic**  
  Implements a fuzzy inference system to adjust traffic light durations based on:
  - Number of pedestrians.
  - Vehicle speed.
  - Road width.
  - Time of day.

- **Real-Time Traffic Data Integration**  
  Utilizes TomTom Traffic API to collect live traffic conditions, including vehicle speed and congestion levels.

- **Interactive User Interface**  
  Built with Streamlit to allow users to test and simulate the system:
  - Automatic mode (GPS-based).
  - Manual mode (customizable input parameters).

- **Scalable and Modular Design**  
  The system can be expanded with additional sensors and historical data for enhanced performance.

---

## Architecture

1. **Input**:
   - Pedestrian count (manual or computer vision in future development).  
   - Vehicle speed and congestion data (via TomTom API).  
   - Time of day.  
   - Road width (manual configuration).  

2. **Processing**:
   - Fuzzy logic system processes input data to determine optimal light durations.  

3. **Output**:
   - Dynamic green light durations tailored to current traffic conditions.  

4. **Interface**:
   - Displays real-time traffic conditions and recommended crossing durations.

---

## Technologies Used

- **Programming Language**: Python  
- **Libraries**:  
  - [scikit-fuzzy](https://pythonhosted.org/scikit-fuzzy/) for fuzzy logic implementation.  
  - [Streamlit](https://streamlit.io/) for the interactive web interface.  

- **APIs**:  
  - [TomTom Traffic API](https://developer.tomtom.com/) for real-time traffic data.  
  - [OpenCage Geocoding API](https://opencagedata.com/) for location-based data.  

---

## Installation

You can run this project locally on your PC or access the deployed web application.

### Option 1: Run Locally

1. **Download the repository**:
   Clone the repository or download the ZIP file from GitHub

2. **Install dependencies**:
   pip install -r requirements.txt (Alternatively, you can follow the detailed instructions in manual-install.txt.)

3. **Open the project**:
    Open the project in your preferred code editor, such as Visual Studio Code.

4. **Run the application**:
    streamlit run app.py

### Option 2: Access the Deployed Application
https://dynamic-traffic-light-using-fuzzy-approach.streamlit.app/

## Contributors  
This project is developed by a team of Computer Science students from Bina Nusantara University:

### Paisal Tanjung (Team Leader)  
### Jhansen Orlando  
### Jason Tirtadjaja  
### Justin Deryl Ferdinand  

---

As the Team Leader, I was responsible for overseeing the entire project lifecycle, ensuring its successful execution from start to finish. My contributions included designing and modeling the system architecture to ensure scalability and efficiency, as well as developing the prototype and implementing the system to translate theoretical designs into a functional application. I conducted rigorous system testing to identify and address issues, ensuring the solution met both performance and quality standards. Post-implementation, I evaluated the system and introduced refinements for continuous improvement. Additionally, I coordinated the team’s efforts to ensure all project milestones were met on schedule, provided technical and strategic guidance to foster collaboration and innovation among team members, and assisted in debugging and optimizing the system to enhance its functionality and user experience.



