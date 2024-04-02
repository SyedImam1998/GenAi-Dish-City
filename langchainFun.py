from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

#Prompt Template
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

load_dotenv()


def city_selector_famous_dish(letter):
    my_secret = my_secret = os.getenv('OPENAI_API_KEY')
    llm=ChatOpenAI(api_key=my_secret,temperature=1)
    random_city_Chooser="""You are a random city selector in India who job is to give out 1 name that starts with{letter}\
    """
    city_Prompt=PromptTemplate(input_variables=["letter"],template=random_city_Chooser)
    city_LLM= LLMChain(llm=llm,prompt=city_Prompt,output_key='city')


    give_famous_dish="""
    You need to give me top 3 famous dishes of {city}\
    """
    dish_Prompt=PromptTemplate(input_variables=["city"],template=give_famous_dish)
    dish_LLM=LLMChain(llm=llm,prompt=dish_Prompt,output_key="dishes")


    ss_chain=SequentialChain(chains=[city_LLM,dish_LLM], input_variables=["letter"],
        output_variables=["city","dishes"],verbose=True)


    result= ss_chain.invoke(letter)
    return {
        'city':result['city'],
        'dishes':result['dishes']
    }