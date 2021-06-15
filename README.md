<h1>Extract-job-postings-from-Indeed-using-selenium-and-python</h1>
Searching for the job posting during post-pandemic might be tedious as there are might job postings but half of them might be from
the staffing agency which leads to scam email or calls. To save time for differentiating its better to automate the process of extracting from the website and then start applying on the geniune companies. We can check the companies profile on the linkedin to clarify its authenticity. 
<h2>Automate Webscraping process for extracting jobs from Indeed website from page 1 to page 6.</h2>
<ul>
<li>The script starts with calling chrome driver to open Google chrome and visit Indeed website.
  There, the script enters the username and password to login into the Indeed account. Followed 
  by Entering the Job Title to be searched for job posting.</li>
  
  <li>The script then extracts all job title, job description and location from page 1 and goes to
  page 2 from extracting the rest. This process continues till it reaches the page 6</li>
  
  <li>The script stores the job titles and details in the list data types. This list data type then get converted
  into Dataframe using pandas library and then it get exported to csv ot html tables format, which-so-ever you want</li>
  </ul>
  <h2>Demonstration</h2>
  


![selenium](https://user-images.githubusercontent.com/57468338/122059950-22b81580-cdbb-11eb-8785-5ea29e6ff286.gif)



  
  
  
  <h2>Output</h2>
  
  ![image](https://user-images.githubusercontent.com/57468338/122058788-fc45aa80-cdb9-11eb-8425-fb61dbebdff6.png)



  
  <h2>Future Work  </h2>
  <p>Further work will be storing the job posting into a database like connecting the script with postgre to insert daily postings with links and 
  using them for applying or carrying out analysis.
  Analyis might include differentiating the job posting from staffing agency to actual companies because every 3rd job posting in the Indeed are
  from staffing agency rather than from actual companies.
  </p>
  
  
  
