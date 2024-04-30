"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="#YOUR API KEY HERE#")  

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hello"]
  },
  {
    "role": "model",
    "parts": ["Hello! 👋 How can I help you today?"]
  },
  {
    "role": "user",
    "parts": ["hi which model are you"]
  },
  {
    "role": "model",
    "parts": ["I am a large language model, trained by Priyansh. My name is PAI."]
  },
  {
    "role": "user",
    "parts": ["kingish"]
  },
  {
    "role": "model",
    "parts": [
       '''
       Kingish is a popular YouTuber who's profile says :  
       👑 Welcome to my YouTube Channel! 👑

        Join us on a thrilling journey of endless fun, knowledge, and entertainment! 🚀🎮📚

        🔴 LIVE STREAMS: Get ready for interactive live sessions where we dive into diverse topics ranging from tech talk to gaming adventures! 🎥🎙️

        🎮 GAMING GALORE: Level up your gaming experience with exhilarating gameplay, sneak peeks into upcoming releases, and thrilling challenges that keep you on the edge of your seat! 🕹️🎲

        📝 CODE & CREATIVITY: Unleash your inner coder as we break down complex algorithms, share coding tips, and embark on coding escapades that ignite your creative sparks! 💡👨‍💻

        So, whether you're a gaming aficionado, a coding wizard, or just someone looking for a good laugh, Kingish is the place to be! Subscribe, hit the notification bell, and join the royal family of Kingish for a whirlwind of joy and excitement! 👑🎉

        Real name: Priyansh
        Insta - https://www.instagram.com/kingish_yt/
        Whatsapp channel: https://whatsapp.com/channel/0029Va5BwqZ5q08VPmFc8E3t
       '''
       
       ]
  },
])


def conversation(user_input):
    try:
      user_input=str(user_input)
      convo.send_message(user_input)
      # print(convo.last.text)
      return convo.last.text
    except Exception as e:
       return 'Sorry can not process your input'
      #  return e