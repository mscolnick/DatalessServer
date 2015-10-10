import wikipedia
import json

class WikipediaApi:
	def __init__(self):
		pass

	def get_summary(self, topic, num_sentences=4):
	# Input: topic (string), num_sentences (int)
	# Output: string of topic
	num_sentences = int(num_sentences)
	return json.dumps({
					  "summary": wikipedia.summary(topic, sentences=num_sentences),
					  "topic": topic})

if __name__ == '__main__':
	wapi = WikipediaApi()
	print wapi.get_summary('bananas', 5)