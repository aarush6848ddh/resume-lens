from langchain_core.prompts import ChatPromptTemplate

def build_prompt():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that compares a resume to a job description and provides feedback. You will return a score from 0 to 100 indicating how well the resume matches the job description, along with specific feedback on strengths and areas for improvement. Also a list of matching skills between the resume and job description and missing skills that are in the job description but not in the resume."),
        ("human", "Here is the resume text:\n{resume}\n\nAnd here is the job description:\n{job_description}\n\nPlease provide feedback on how well the resume matches the job description and suggest improvements.\n\n{format_instructions}")
    ])
    return prompt
