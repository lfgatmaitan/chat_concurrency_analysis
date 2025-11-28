def count_concurrency(data):

	"""Produces a dictionary with the following:
	key is the conversation ID
	value is a list of other conversation ID's concurrent with the key"""

	concurrencies = {}
	for chat in data:
		concurrencies[chat[0]] = [] #all chats as keys, empty list as values

	for chat_1 in data:	
		convo_id_1 = chat_1[0]
		start_1 = chat_1[1]
		end_1 = chat_1[2]
	
		for chat_2 in data:
			convo_id_2 = chat_2[0]
			start_2 = chat_2[1]
			end_2 = chat_2[2]

			#logical test if chat 2 overlaps with chat 1
			if (start_1 < end_2) and (start_2 < end_1):
				concurrencies[convo_id_1].append(convo_id_2)

	return concurrencies