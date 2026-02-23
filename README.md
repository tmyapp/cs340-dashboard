# cs340-dashboard

CS-340 Dashboard Project
Grazioso Salvare Animal Rescue Analytics Dashboard
Matthew Leon
Southern New Hampshire University

Project Overview
This project involved the development of an interactive web-based analytics dashboard for Grazioso Salvare using Python, MongoDB, and the Dash framework. The purpose of the dashboard is to provide dynamic filtering, visualization, and geospatial analysis of animal shelter data in order to support data-driven rescue decisions.
The application integrates a custom CRUD Python module developed in Project One to interface with a MongoDB database. By combining MongoDB as the data model and Dash as the web framework, the dashboard dynamically updates a data table, a breed distribution chart, and a geolocation map based on user-selected rescue categories. The final product provides Grazioso Salvare with a functional, maintainable, and interactive analytical tool capable of identifying animals that meet specific rescue criteria.

Required Functionality
The dashboard successfully implements all required functionality outlined in the project specifications. The application displays animal shelter records in an interactive Dash DataTable that supports filtering, sorting, pagination, and single-row selection. Users may filter records using radio button controls corresponding to four rescue categories: Reset (All Records), Water Rescue, Mountain/Wilderness Rescue, and Disaster/Tracking.
When a rescue category is selected, the dashboard dynamically queries MongoDB using predefined criteria including animal type, breed, sex upon outcome, and age range. The filtered results automatically update the DataTable, ensuring that users see only relevant records. Additionally, the dashboard generates a dynamic histogram visualizing the distribution of animals by breed based on the currently displayed dataset.
The application also includes a geospatial component using Dash Leaflet. When a user selects a row in the DataTable, the map updates to display a marker at the corresponding latitude and longitude coordinates. The selected row is visually highlighted, ensuring clarity in user interaction. The dashboard includes Grazioso Salvare branding and creator identification, meeting all interface requirements.


Screenshot Evidence
(Screenshot 1: Full Dashboard Loaded-SNHU Link Logo)
 
(Screenshot 2: Water Rescue Filter Applied) 

(Screenshot 3: Mountain/Wilderness Filter Applied)
 
(Screenshot 4: Disaster Filter Applied)
 
(Screenshot 5: Map Marker Updating Based on Row Selection)
 
Each screenshot confirms that the filtering logic correctly modifies the dataset, updates the visualization components, and synchronizes the map display dynamically. These images provide verification that all required functionality has been implemented and tested successfully.


Tools Used and Rationale
MongoDB was selected as the database management system due to its flexible, document-oriented NoSQL architecture. The dataset is stored in JSON-like documents, which closely mirror Python dictionaries. This structural similarity simplifies serialization and deserialization of data between the database and the application layer.
MongoDB integrates seamlessly with Python through the PyMongo driver, allowing complex queries to be executed efficiently using key-value filtering. This was particularly useful for implementing rescue category filters that required conditional logic involving breed, sex, and age ranges. The custom CRUD module abstracts database operations and promotes modular, reusable code design, improving maintainability and separation of concerns.


Dash Framework as View and Controller
The Dash framework was used to construct the web application interface and manage interactivity. Dash provides a reactive callback architecture that allows components to update dynamically in response to user input. In this implementation, Dash layout components serve as the view layer, while callback functions operate as the controller layer.
Within this architecture, MongoDB functions as the model, Dash layout elements function as the view, and Dash callbacks manage application logic as the controller. This separation of responsibilities aligns with Model-View-Controller (MVC) design principles and supports organized, maintainable development.
Dash was selected because it enables rapid development of interactive dashboards using Python, integrates directly with Plotly for visualization, and supports advanced UI components such as DataTable, radio buttons, and dynamic graphs.


Additional Tools
Additional tools were used to support application functionality. Plotly Express was used to generate the dynamic histogram visualizing breed distribution. Dash DataTable provided advanced tabular features including sorting and filtering. Dash Leaflet enabled geospatial mapping of animal locations. JupyterDash facilitated development and testing within a Jupyter Notebook environment. Base64 encoding was used to embed the Grazioso Salvare logo directly within the application layout.


Steps Taken to Complete the Project
The project began with the development of a reusable CRUD Python module in Project One. After establishing a secure MongoDB connection using authentication credentials, the dataset was retrieved using the CRUD read method and converted into a Pandas DataFrame for manipulation within the application.

Because MongoDB includes an _id field of type ObjectID, which is incompatible with Dash DataTable, the _id column was removed from the DataFrame prior to rendering. The dashboard layout was then designed to include branding, a title, radio button filters, the interactive data table, a histogram visualization, and a geolocation map.

Dash callback functions were implemented to manage dynamic behavior. These callbacks were responsible for filtering data based on rescue category selection, updating the histogram visualization, highlighting the selected table row, and updating the map marker location. Each rescue category was tested individually to confirm correct filtering logic, and synchronization between the table, chart, and map was verified.


Challenges Encountered and Resolutions
One challenge encountered was the incompatibility between MongoDB’s ObjectID type and the Dash DataTable component. The _id field caused rendering errors within the table. This issue was resolved by explicitly removing the _id column from the DataFrame prior to passing data to the DataTable component.
Another challenge involved ensuring proper synchronization between dashboard components. Because multiple components depended on shared data, callback configuration required careful design to prevent conflicts. This was resolved by separating responsibilities into distinct callbacks, each managing a specific output.
A final challenge involved geolocation mapping. Latitude and longitude values required validation to prevent runtime errors when missing or improperly formatted data was encountered. This was resolved by implementing error handling using a try/except block before rendering the map marker.


Instructions for Reproducing the Project
To reproduce this project, ensure that MongoDB is installed and running locally. Confirm that the animal shelter dataset is loaded into the appropriate MongoDB collection. Install the required Python packages, including Dash, JupyterDash, Plotly, Dash Leaflet, Pandas, and PyMongo.

Open the ProjectTwoDashboard.ipynb file and verify that the database credentials in the CRUD module are correct. Run all cells in sequence. The dashboard will launch on localhost using the default port 8050. If port 8050 is unavailable, modify the run command to specify an alternate port (e.g., app.run_server(port=8051)).


Conclusion
This project demonstrates integration of MongoDB with a Python-based web dashboard using Dash. The final product satisfies all required functionality, supports dynamic filtering, and provides interactive visual analytics and geospatial visualization.
The dashboard provides Grazioso Salvare with an efficient and maintainable analytical tool to support rescue decision-making.
<img width="468" height="634" alt="image" src="https://github.com/user-attachments/assets/4a8597bd-9ad1-4638-9064-4c44a1ec067b" />
