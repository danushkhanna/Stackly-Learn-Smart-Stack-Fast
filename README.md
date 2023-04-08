# **Stackly: Learn Smart, Stack Fast - Smart Search Engine for CS Mastery**

<ins>https://stackly.streamlit.app/<ins/>

Stackly is a search engine created for learning any computer science tech stack or domains. It is built using Streamlit, a popular Python library for creating web apps, and course data from OSSU - Open Source Society University. Stackly helps users to learn new technologies quickly and efficiently by providing a way to search for relevant online courses and resources.

# **Features**
Stackly offers the following features:

- Search for relevant courses by topics, course name, level, or domain.
- Filter search results by different parameters to narrow down the search.
- View the course information, including course name, university, prerequisites, level, domain, and links.
- Easily access online courses and resources to learn new technologies.

# **Dependencies**

Stackly relies on the following Python packages:

- Streamlit - a Python library for building interactive web applications
- Pandas - a Python library for data manipulation and analysis
- NumPy - a Python library for numerical computing
- Google Sheets API - used to access the Google Sheet that contains the course data
- These dependencies can be installed using pip, the Python package installer. 
- Here's the command to install them:

```pip install streamlit pandas numpy google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2```

Note that you also need to have valid Google Sheets API credentials in order to access the Google Sheet that contains the course data. You can follow the instructions provided in the Google Sheets API documentation to obtain the necessary credentials.

# **How it Works?**

Stackly uses course data from Open Source Society University (OSSU), which provides a comprehensive curriculum for computer science students. The data is stored in a Google Sheet, and Stackly accesses the sheet by constructing a URL to download the CSV file using the Pandas library. The data is then loaded into a Pandas dataframe for filtering and display.

The user interface of Stackly is simple and intuitive, allowing users to search for courses by keywords such as topics, course name, level, or domain. The search functionality is implemented using a ```text_input widget```, which takes the search term as input and stores it in the ```text_search``` variable.

To filter the dataframe based on the search term, the code creates four masks using the ```str.contains``` function. These masks correspond to the four search criteria mentioned earlier, and they are combined using the ```|``` operator to create a single mask. The dataframe is then filtered using this mask, and a new dataframe called ```df_search``` is created that contains only the courses that match the search criteria.

The search results are displayed using cards, with each card providing detailed information about a specific course. The ```N_cards_per_row``` variable is set to 3, which determines how many cards will be displayed per row. The cards are created using the ```st.columns function```, which creates a layout with multiple columns that can be filled with content.

Each card displays the course name, university, prerequisites, level, domain, and links to the course. The information is formatted using the Markdown language, which allows for rich text formatting such as bold and italicized text.

Overall, Stackly is a powerful tool that provides users with an easy and intuitive way to learn computer science tech stacks and domains. It is a testament to the power of open-source software and the collaborative efforts of developers around the world.

# **Installation**
To use Stackly, you need to have Python and Streamlit installed on your machine. Follow these steps to install them:

- Install Python by downloading the installer from the official website: https://www.python.org/downloads/
- Install Streamlit by running the following command in your terminal:
- Copy code
- pip install streamlit
- Clone the Stackly repository to your local machine using the following command:
```git clone https://github.com/<your_username>/stackly.git```

# **Usage**
Once you've set up the environment and installed the required packages, you can run Stackly by following these steps:

- Open PyCharm and open the project containing the bot code.
- Make sure you are in the environment you created earlier (i.e., Stackly).
- Open a terminal in PyCharm and navigate to the directory where you've saved the bot code.
- Run the command:
```streamlit run FILENAME.py```
(replace FILENAME with the name of the file containing the Stackly.py code).

Wait for a few seconds until Stackly opens in a new tab on your default browser.

# **Data Source**
Stackly uses course data from OSSU - Open Source Society University, which is a community-driven online learning platform that offers a comprehensive computer science curriculum for free. The data is stored in a Google Sheet, which is updated regularly to include new courses and resources.

# **Team Members**

Stackly was developed by a team of two members:

- Danush Khanna (danush.s.khanna@gmail.com)
- Sanyam Jain (sanyam0605@gmail.com)

We are passionate about computer science education and wanted to create a tool that would help people learn new technologies more easily. We hope that Stackly will be useful to anyone who wants to learn and grow their skills in the field of computer science.

# **Contact Us**

If you have any questions or comments, please feel free to contact us at our GitHub repository or email.

# **Contributing**
If you want to contribute to Stackly, feel free to fork the repository and submit a pull request. You can also create an issue if you find a bug or have a suggestion for a new feature. We welcome all contributions and feedback!

# **License**
Stackly is released under the <ins>Apache License 2.0</ins>.

# **Conclusion**

With Stackly, users can easily filter courses by topics, course name, level, or domain, and get quick access to relevant information such as the university offering the course, the prerequisites required, and the links to the course materials.

And remember, with Stackly, learning computer science has never been easier! So don't be afraid to stack up your knowledge and code your way to success. Happy learning!

# **Screenshots**

<img width="1470" alt="Screenshot 2023-04-08 at 5 43 12 PM" src="https://user-images.githubusercontent.com/113158564/230720528-69d807bb-f22c-4541-ac1a-9629e2c9c803.png">
<img width="1470" alt="Screenshot 2023-04-08 at 5 43 29 PM" src="https://user-images.githubusercontent.com/113158564/230720531-b8f8cc91-b7c1-4b0a-93ae-a0c4e1bed4b2.png">
<img width="1470" alt="Screenshot 2023-04-08 at 5 43 40 PM" src="https://user-images.githubusercontent.com/113158564/230720535-71b09b3c-e7c1-401b-a199-4a30b2bbb41a.png">
<img width="1470" alt="Screenshot 2023-04-08 at 5 43 49 PM" src="https://user-images.githubusercontent.com/113158564/230720538-f57ba823-ded0-4fb7-b6cb-61d7201a1c50.png">
<img width="1470" alt="Screenshot 2023-04-08 at 5 44 31 PM" src="https://user-images.githubusercontent.com/113158564/230720540-92dc90ce-a20c-4277-a60e-af817a3c26ec.png">

