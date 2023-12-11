<h1 align="center">Decision-Hub</h1>
<!-- <h5 align="center">""</h5> -->

<hr>

<img align="right" height="400px" padding="20px" src="https://media.giphy.com/media/HUplkVCPY7jTW/giphy.gif">

# Problem Statement

Develop a Rule Builder application "DecisionHub" that empowers Business Analysts to create, save,and visualize decision strategies.
Provide a no-code rule writing experience andvisual representation to test these rules in real-time and observe the calculations at each step.
# Decision Hub 

Decision Hub is an application tailored to streamline the challenges encountered by Business Analysts in creating, storing, and visualizing decision strategies. Fueled by advanced language models (LLM Powered Generative AI) and innovative methodologies, this tool offers a user-friendly,seamless, no-code rule-writing experience tailored for analysts who may not have programming expertise.

Decision Hub is a comprehensive solution with distinct sections, each catering to specific needs: 

Rule Builder for creation and visualization, Rule Management for database control, and Debugger for real-time testing. Elevate your decision-making processes with a user-centric approach that empowers analysts to navigate the complexities of rule crafting effortlessly.

### Rule Builder

Effortlessly create, save, and visualize rules, intricately linked to the rules database.
Intuitive design for a seamless rule-writing experience, ensuring accessibility for analysts with varying technical backgrounds.

### Rule Management

Centralized control to add, modify and remove rules within the rules database.
Simplifies rule governance, enabling swift adjustments to align decision strategies with evolving business requirements.

### Debugger

Real-time testing functionality, facilitating the observation of calculations.
Pinpoint and rectify errors efficiently, ensuring the reliability and accuracy of decision rules.



## Architectural Diagram

![Logo](https://private-user-images.githubusercontent.com/106394426/289374834-948fcf3c-7b4a-4b8c-ae88-4a889380c29c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDIzMDQxODMsIm5iZiI6MTcwMjMwMzg4MywicGF0aCI6Ii8xMDYzOTQ0MjYvMjg5Mzc0ODM0LTk0OGZjZjNjLTdiNGEtNGI4Yy1hZTg4LTRhODg5MzgwYzI5Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMjExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTIxMVQxNDExMjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01MGUxYTQ3MGNlYWNiYjdiYjdjMzkxYTM3YjgxYmMwZTkzYmRiZDU5YzRmMzczY2U1MmZmOGJmZTA1YTFkZmM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.zRUFlzxmaDL3FXnxxK0VUUi3KKLOrxaGJZWblbnNum8)


## Demo


## Deployment

To deploy this project run

#### Query Builder 

DataSphere-Explorer
npm install
npm install -g serve
npm run build
serve -s dist
```bash
    cd client -> npm install npm run dev
    cd server -> npm install npm start
```
#### DataSphere-Explorer
```bash
npm install
npm install -g serve
npm run build
serve -s dist
```



## Documentation

[Documentation](https://linktodocumentation)


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
