import wikipedia
import json

class WikipediaApi:
  def __init__(self):
    pass

  def get_summary(self, topic, num_sentences=4):
  # Input: topic (string), num_sentences (int)
  # Output: string of topic
    num_sentences = 4
    # num_sentences = int(num_sentences)
    try:
      summary = wikipedia.summary(topic, sentences=num_sentences)
    except Exception as e: # in case disambiguation happens
      try:
        topic = e.options[0]
        summary = wikipedia.summary(topic, sentences=num_sentences)
      except:
        return {"summary": "no such article exists", "topic": topic}

    result = {
      "summary": summary.replace('"',"'"),
      "topic": topic
    }
    return json.dumps(result)

if __name__ == '__main__':
  wapi = WikipediaApi()
  print wapi.get_summary('test', 5)
