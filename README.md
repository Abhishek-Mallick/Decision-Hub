<h1 align="center">Decision-Hub</h1>
<h5 align="center">"Empowering Analyts with AI-Driven Decision Automation"</h5>

<hr>

<img align="right" height="300px" padding="20px" src="https://decisionhub.pythonanywhere.com/static/images/server-animate.svg">

# Problem Statement

Develop a Rule Builder application "DecisionHub" that empowers Business Analysts to create, save,and visualize decision strategies.
Provide a no-code rule writing experience andvisual representation to test <br> these rules in real-time and observe the calculations at each step.

# Decision Hub 

Decision Hub is an application tailored to streamline the challenges encountered by Business Analysts in creating, storing, and visualizing decision strategies. Fueled by advanced language models (LLM Powered Generative AI) and innovative methodologies, this tool offers a user-friendly,seamless, no-code rule-writing experience tailored for analysts who may not have programming expertise.

Decision Hub is a comprehensive solution with distinct sections, each catering to specific needs: 

Rule Builder for creation and visualization, Rule Management for database control, and Debugger for real-time testing. Elevate your decision-making processes with a user-centric approach that empowers analysts to navigate the complexities of rule crafting effortlessly.

### SOLUTION 1 : ENGLISH LIKE RULE WRITING
#### TEXT TO QUERY : Natural Language Processing with Contextual Reasoning
DecisionHub utilizes customized Code Llama 2 for contextual reasoning.Users can upload databases to test queries generated from English-like rules, ensuring accuracy. The system also provides insights into the database schema, enhancing rule implementation reliability.
DecisionHub can convert plain English rules into executable database queries through natural language processing (NLP) techniques like Code Llama 2.


### SOLUTION 2 : SUPPORT FOR ADVANCED CONDITIONALS
#### Support for advanced conditionals further enhances the capabilities of the Rule Builder

DecisionHub enables business analysts to instantly prototyping and execute sophisticated data-driven decision strategies without coding through language models like Code Llama 2

* Offers intelligent query merging capabilities, allowing users to combine two queries seamlessly through Nested Rules.
* Ideal for scenarios where complex data filtering or retrieval requires the refinement of search criteria.
* Empowers users to interact with the query builder effortlessly, creating a seamless and intuitive experience.
* No-Code Query Builder & Executor - Automatically convert conditional statements, spreadsheet-style formulas into fast-executing queries


### SOLUTION 3 : AGILITY IN QUICKLY CHANGING RULES
#### DYNAMIC RULE MODIFICATION : Drag-n-drop support for rules and group of rules

* DecisionHub empowers analysts to quickly modify and test strategies by adjusting rules in real-time. The interface allows observing calculations to reduce errors and streamline adapting to evolving requirements. 

* Rule Manager provides a visual query builder for advanced search/filtering on sites and apps. Its flexibility and customization benefit projects requiring complex queries without code.

* User Friendly Interface: It provides a simple yet powerful visual interface for non-technical users to build advanced queries in a click-and-drag manner without needing to know SQL or other query languages.
* Server-Side Compatible: Queries built with Rule Manager can be converted to JSON, XML , SQL or other formats compatible with server-side frameworks like Laravel, Django, Rails etc. allowing seamless integration.

### SOLUTION 4 : DEBUGGING RULES QUICKLY
#### REAL TIME DEBUGGING  : To pinpoint and rectify logical errors in rules
* To tackle the complexity of managing thousands of rules, our application provides an easy-to-use mechanism for checking the logic of each portion of calculations rapidly.  Analysts can run rules swiftly and double click to identify potential issues or incorrect conditions within their decision  strategies.

* Interactive Debugging: The builder allows adding breakpoints to pause execution and inspect values at any point for easier debugging of queries and logic.
* Clear Error Messages: Invalid queries or values are detected immediately with clear errors displayed in the builder interface to quickly identify and fix issues.
* Trace Query Execution: Each query change is tracked to easily trace why results are unexpected, facilitating debugging of complex queries with multiple rules and conditions.



## Architectural Diagram
![Decision-Hub drawio (3)](https://github.com/Abhishek-Mallick/Decision-Hub/assets/106394426/1d760f38-0111-4c47-889c-3f63a892fba2)


## Wireframe
![archi](https://github.com/Abhishek-Mallick/Decision-Hub/assets/90705452/9ec2a192-a7c4-4305-899f-bc3e82ebaa26)


## Contribution

```

git clone https://github.com/Abhishek-Mallick/Decision-Hub

cd Decision-Hub

pip install -r requirements.txt

flask run

```



## Documentation

[Documentation](https://drive.google.com/file/d/1ioUanHQ7KLsXZGFywug9vGmdUa9GhYiE/view?usp=sharing)


# Key-Features

### 1. No-Code Rule-Writing Experience
The Rule Builder eliminates the need for analysts to delve into programming languages or navigate complex technical interfaces. Instead, it offers an intuitive, no-code rule-writing experience, allowing analysts to focus solely on expressing their business knowledge without technology hindering their progress.

By the integration of the LLM (Large Language Model), the Rule Builder transforms plain English text into sophisticated queries. These queries, execute seamlessly across diverse platforms, extracting valuable data from databases. This integration enables analysts to convert business insights into actionable rules without the hindrance of technological complexities.

### 2. Excel-Like Logic Support
Recognizing that many Business Analysts are accustomed to working with tools like Excel or calculator-like logic, our application facilitates the writing of basic arithmetic expressions with conditional or comparison operators, these are then promptly converted into rules and queries powered by the LLM model. This ensures a seamless transition for analysts familiar with these widely-used platforms.

### 3. Dynamic Rule Modification and Testing
Addressing the challenge of frequently changing business rules, DecisionHub empowers analysts to quickly modify and test their decision strategies. With a user-friendly interface, analysts can make adjustments on-the-fly and observe real-time calculations, reducing the likelihood of errors and streamlining the adaptation process for evolving business requirements.

### 4. Efficient Logic Checking for Thousands of Rules
To tackle the complexity of managing thousands of rules, our application provides an easy-to-use mechanism for checking the logic of each portion of calculations rapidly. Leveraging LLM Powered Generative AI, analysts can run rules swiftly and double-click to identify potential issues or incorrect conditions within their decision strategies.
