import openai
import os
import sys

psalms = ("40", "10", "12", "23", "35", "38", "41", "88", "139", "141")


def prompts(psalm):
  return (
    f"Write a 5 to 6 sentence introduction to the spiritual and emotional elements of Psalm {psalm}, and try to connect its meaning and purpose with that of Christian faith.",
    f"Provide the full text of Psalm {psalm} using the King James Version, formatted for organizational clarity.",
    f"Create a study guide for Psalm {psalm} that covers the entire psalm with verses being grouped by relationship; precede the study guide with “Study Guide”. Write a concise, one-line header that describes the topical relationship of groups of related verses (set the text style of the header to bold). Next, write a two-part, one paragraph summary that 1) begins with a single topic sentence, which expands on the header and  summarizes the main point presented by the group of verses (set the topic sentence text style to bold), and then reference the Bible book, chapter and verses that comprise the main point (put the reference in parentheses).; and, 2) continuing in the same paragraph, a more detailed summary (5 to 6 sentences in length) that further clarifies the intent and meaning of the main point ((set the text style of the header to regular).  Include the entire psalm (all verses) in the series of main points. After each main point, present one to three questions related to the verses that focus their attention to the most significant aspect(s) of the main point (precede the questions with “Focus”). Follow each question with an answer. Following the questions and answers “Focus” section, ask one to three questions that invite and encourage the reader to reflect on the material and its applicability to their personal experiences, and to relay those experiences by and through their answers to each; precede the questions with “Reflect”. There should be no punctuation after any of these. Do not number anything, but do bullet the reflection questions.  After all the main points are written, write a summary of the main points (or psalm) overall, highlighting their overall (or collective)  meaning and purpose, and connect that meaning and purpose with that of Christian faith and/or divine attributes of God (both communicable and incommunicable), as well as His purpose for man. After each main point, present one to three questions related to the verses that focus their attention to the most significant aspect(s) of the main point (precede the questions with “Focus”). Follow each question with an answer. Following the questions and answers “Focus” section, ask one to three questions that invite and encourage the reader to reflect on the material and its applicability to their personal experiences, and to relay those experiences by and through their answers to each; precede the questions with “Reflect”. There should be no punctuation after any of these. Do not number anything, but do bullet the reflection questions.r answers to each; precede the questions with “Reflect”. There should be no punctuation after any of these. Do not number anything, but do bullet the reflection questions.",
    f"Describe all the ways Psalm {psalm} embodies or reflects God’s nature in two sections: 1. divine (incommunicable) attributes; and, 2. communicable  attributes. Include biblical references, if applicable.",
    f"Relate the person and teachings of Jesus Christ and Psalm {psalm}, particularly, as the pertain to the gospel. Include supporting Bible verses for every connection made, especially if there is a match between the words of Jesus and verses in this psalm.",
    f"List all of the psalms that are identical or highly similar to Psalm {psalm}, whether in part or in whole. Explain the similarities in as much detail as possible."
  )


def messages_arr(prompts_func, psalms_arr):
  messages_dict_arr = [{
    "role":
    "system",
    "content":
    "You are creating study material for parishoners participating in a Bible study group or class, and your task is to generate theological discourse on a variety of Psalms per the specifications provided by me."
  }]
  for psalm in psalms_arr:
    for prompt in prompts_func(psalm):
      messages_dict_arr.append({"role": "user", "content": prompt})
  return messages_dict_arr


try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
  sys.stderr.write("""
  You haven't set up your API key yet.

  If you don't have an API key yet, visit:

  https://platform.openai.com/signup

  1. Make an account or sign in
  2. Click "View API Keys" from the top right menu.
  3. Click "Create new secret key"

  Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
  """)
  exit(1)

response = openai.ChatCompletion.create(model="gpt-4",
                                        messages=messages_arr(prompts, psalms),
                                        temperature=1,
                                        top_p=1,
                                        n=3)
print(response)
