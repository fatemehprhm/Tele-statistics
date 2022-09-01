# Telegram statistics
Export statistics for telegram group

## How to run
First add 'src' to your 'PYTHONPATH' using following code in your main directory

```
export PYTHONPATH=${PATH}
```
Then add your json file to 'DATA_DIR' and change the file name to your .json file name in the following code.

```
chat_stats = chatstatistics(chat_json=DATA_DIR/'file_name.json')
```

Then run:

```
python3 src/chat-statistics/stat.py
```

to generate a wordcloud of json data in 'DATA_DIR'
