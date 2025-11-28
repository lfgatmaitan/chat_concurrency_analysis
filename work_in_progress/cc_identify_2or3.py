def identify_count(concurrency_many, concurrency_2):
	"""Identifies if chat_id is overlapping the with the same chat multiple 
	times or with multiple chats simultaneously."""
	"""logic: if concurrency is 3, then A overlaps with B, B overlaps with C
	and C overlaps with A"""

	identified = [ [], [] ] 

	for chat_id in concurrency_many:
		count = 2 
		for concurrent_chat in concurrency_2[chat_id]:
			if concurrent_chat == chat_id:
				# concurrent chat is concurrent to itself
				continue
			for key, value in concurrency_2.items():
				if ((key == concurrent_chat) or (key == chat_id)):
					continue
				else:
					for x in value:
						if x == concurrent_chat:
							count = 3
						else:
							pass
		if count == 3:
			identified[1].append(chat_id)
		else:
			identified[0].append(chat_id)

	return(identified)