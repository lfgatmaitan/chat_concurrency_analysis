# chat_concurrency_analysis
Classifies each chat ID into 1, 2, or 3 concurrencies based on the number of chats it overlapped with simultaneously.

#v1 11/28/2025
very rough draft but is working already
no pandas or numpy usage
input is csv file with the format [chat id, start_time, end_time]
output are lists of grouped chat ID's according to number of concurrencies
strings are printed to keep track of the logic
planning to add date and agent ID's onto the column input, right now, I am assuming all chats are made by the same person and at the same day
