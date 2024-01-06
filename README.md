# YouTube Data Analysis Redash Chat Add-on

## Business Objective

Our company aimed to enhance data analysis capabilities, particularly focusing on comprehensive YouTube data exploration. The goal was to develop a Redash chat add-on facilitating natural language queries for extracting insights from multiple Redash dashboards and connected databases. This initiative aimed to empower team members to derive actionable insights from our BI platforms.

## Project Design

### Data Collection and Storage

- Created a comprehensive schema for YouTube data storage.
- Utilized Python scripts to persist all required data efficiently.

### Redash Chat Add-on Integration

- Integrated a chatbot into the Redash interface, enabling seamless communication.
- Leveraged Redash API for query and visualization generation programmatically.

### Large Language Model Integration

- Developed an LLM using OpenAI GPT-3.5 Turbo for translating natural language to SQL queries.
- Integrated the LLM with the chatbot for accepting user inputs and generating appropriate SQL queries.

## Tech Stack Used

- Python for data persistence and backend development.
- Redash for dashboard visualization and querying.
- OpenAI GPT-3.5 Turbo for natural language understanding and SQL query generation.

## Methodologies Followed

- Agile development methodology for iterative progress.
- Test-driven development (TDD) for ensuring code robustness.
- Continuous Integration/Continuous Deployment (CI/CD) for efficient code package testing and deployment.

## Results Obtained

- Successfully integrated a chatbot allowing natural language queries within Redash.
- Implemented an LLM capable of translating natural language to SQL queries.
- Enabled users to extract insights and generate visualizations seamlessly through the Redash interface.

## Lessons Learned

- The importance of robust data schema design for efficient querying and visualization.
- The significance of fine-tuning language models for accurate interpretation of user queries.
- Continuous iteration and feedback gathering are crucial for improving user experience.

# Chatbot Generating SQL Query Example

In this example, we showcase the functionality of our chatbot integrated with Redash, where a user input in natural language triggers the generation of an SQL query.

![Chatbot Generating SQL Query](screenshots/Screenshot%20from%202024-01-06%2017-59-26.png "Chatbot Example")

The image above demonstrates the chatbot interface. A user input in natural language prompts the chatbot to interpret the query and generate the corresponding SQL. This seamless interaction empowers users to retrieve data through conversational queries.

## Documentation

For a detailed process walkthrough, please refer to the attached PDF document or follow this [link](https://drive.google.com/file/d/1QbxxN_a9mIDLAU385HkLzWsDE5iv_J5o/view?usp=sharing) to access the published blog detailing our approach, challenges faced, and results obtained.
