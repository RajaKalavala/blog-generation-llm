import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLAma 2 model
def getLLamaResponse(input_text,no_words,blog_style):

    ###LLama2 Model
    llm = CTransformers(model='',model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})

    ### Prompt Template
    template="""
            Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words.
            """
    
    prompt = PromptTemplate(input_variables=["style","text","n_words"], template=template)

    ## Generate the repsonse from the llama 2 model
    response = llm(prompt.format(style=blog_style,text=input_text,n_words=no_words));
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon='',
                   layout='centered',
                   initial_sidebar_state='collapsed')


st.header("Generate Blogs ")

input_text=st.text_input("Enter the Blog Topic")

## Creating colums for additional 2 fields

col1,col2 = st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',("Data Scitentist",'Researchers','Common Pepole'),index=0)

submit=st.button('Generate')

##Final response
if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))