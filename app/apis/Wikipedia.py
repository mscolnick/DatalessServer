import wikipedia
import json

class WikipediaApi:
	def __init__(self):
		pass

	def get_summary(self, topic, num_sentences=4):
	# Input: topic (string), num_sentences (int)
	# Output: string of topic
		num_sentences = int(num_sentences)
		result = {
			"summary": wikipedia.summary(topic, sentences=num_sentences).replace('"',"'"),
			"topic": topic
		}
		return json.dumps(result)

if __name__ == '__main__':
	wapi = WikipediaApi()
	print wapi.get_summary('sonny dykes', 5)