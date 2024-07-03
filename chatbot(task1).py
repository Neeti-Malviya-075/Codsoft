import time;


now=time.ctime()
qna={
    "what is the time now":now,
    "hi":"hey",
    "hello":"hello",
    "good moring":"good moring",
    "good afternoon":"good afternoon",
    "good evening":"good evening",
    "how are you":"i am fine",
    "what is your name":"my name is NM",
    "who are you":"I am NM",
    "what are you doing":"having chat with you",
    "what is your favorite food":"sorry i am a bot i don't have food",
    "What is Artificial Intelligence":"Artificial intelligence (AI) is the ability of machines to perform tasks that are typically associated with human intelligence, such as learning and problem-solving." ,
    "How powerful is AI":"Artificial intelligence (AI) is the ability of machines to perform tasks that are typically associated with human intelligence, such as learning and problem-solving. ",
    
    "Will AI steal your jobs":"Some jobs that may fall into this category include recommending web content or applications based on user preferences and past web or app behavior. AI results can leave room for interpretation",
    "Can AI take over the world":"can't predict",
    "What are the pros of AI":" AI automates repetitive tasks",
    "What are the cons of AI":" AI needs lots of data",
    "How close are we to achieve AGI":" there are still significant roadblocks in the way before we can achieve AGI.",
    "What are the applications of AI":"Artificial Intelligence in E-Commerce",
    "Do you need to be a genius to start learning AI":"don't think so",
    "How to get started with AI":"Artificial Narrow Intelligence ,Artificial General Intelligence,Artificial Super Intelligence",
    }
while True:
    qs=input();

    if(qs=="quit"):
        break;
    else:
        print(qna[qs]);
