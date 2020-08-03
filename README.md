## bot-api -> back-end HTTP / REST
----------

![alt text](https://raw.githubusercontent.com/junqueira/telecom-fake/master/project/bot-api.jpg)

### conteiner docker
<pre>
  docker-compose up
<code>
</code>
</pre>

### config local base google firebase
<pre>
  pip install -r requirements.txt
  python bots/tests.py
<code>
  export API_KEY_FIREBASE=${API_KEY_FIREBASE}
  export AUTH_DOMAIN_FIREBASE=${AUTH_DOMAIN_FIREBASE}
  export DATA_BASE_URL_FIREBASE=${DATA_BASE_URL_FIREBASE}
  export STORAGE_BUCKET_FIREBASE=${STORAGE_BUCKET_FIREBASE}
</code>
</pre>


# Register bot_homolog

### Method - POST /bots
<pre><code>
  curl -H "Content-Type: application/json" \
  -X POST -d \
  '{"id":"36b9f842-ee97-11e8-9443-0242ac120002", "name":"Aureo"}' \
  http://201.95.65.253:8081/bots/add \
</code>

return ->
{"status": 200, "return": "success"}
</pre>
### Method - GET /bots/:id
<pre><code>
  curl -H "Content-Type: application/json" \
  -X GET http://201.95.65.253:8081/bots/36b9f842-ee97-11e8-9443-0242ac120002 \
</code>

return ->
{"id": "36b9f842-ee97-11e8-9443-0242ac120002","name": "Aureo"}
</pre>


# Exchange messages between robot with clients

### Method - POST /messages  -> bot
<pre><code>
  curl -H "Content-Type: application/json" \
  -X POST -d \
  '{"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1", \
  "timestamp": "2018-11-16T23:30:52.6917722Z", \
  "from": "36b9f842-ee97-11e8-9443-0242ac120002", \
  "to": "16edd3b3-3f75-40df-af07-2a3813a79ce9", \
  "text": "Oi! Como posso te ajudar?"}' \
  http://201.95.65.253:8081/messages/add \
</code>

return ->
{"status": 200, "return": "success"}
</pre>

### Method - POST /messages  -> client
<pre><code>
  curl -H "Content-Type: application/json" \
  -X POST -d \
  '{"id": "67ade836-ea2e-4992-a7c2-f04b696dc9ff", \
  "conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1", \
  "timestamp": "2018-11-16T23:30:57.5926721Z", \
  "from": "16edd3b3-3f75-40df-af07-2a3813a79ce9", \
  "to": "36b9f842-ee97-11e8-9443-0242ac120002", \
  "text": "Gostaria de saber meu saldo?"}' \
  http://201.95.65.253:8081/messages/add \
</code>

return ->
{"status": 200, "return": "success"}
</pre>

### Method - GET /messages/:id
<pre><code>
  curl -H "Content-Type: application/json" \
  -X GET http://201.95.65.253:8081/messages/16edd3b3-3f75-40df-af07-2a3813a79ce9 \
</code>

return -> 
'{"id": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
"timestamp": "2018-11-16T23:30:52.6917722Z",
"from": "36b9f842-ee97-11e8-9443-0242ac120002",
"to": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"text": "Oi! Como posso te ajudar?"}'
</pre>

### Method - GET /messages?conversationId=:conversationId
<pre><code>
  curl -H "Content-Type: application/json" \
  -X GET http://201.95.65.253:8081/messages/conversationId=7665ada8-3448-4acd-a1b7-d688e68fe9a1 \
</code>

return -> 
[{"id": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
"timestamp": "2018-11-16T23:30:52.6917722Z",
"from": "36b9f842-ee97-11e8-9443-0242ac120002",
"to": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"text": "Oi! Como posso te ajudar?"},
{"id": "67ade836-ea2e-4992-a7c2-f04b696dc9ff",
"conversationId": "7665ada8-3448-4acd-a1b7-d688e68fe9a1",
"timestamp": "2018-11-16T23:30:57.5926721Z",
"from": "16edd3b3-3f75-40df-af07-2a3813a79ce9",
"to": "36b9f842-ee97-11e8-9443-0242ac120002",
"text": "Gostaria de saber meu saldo?"}]
</pre>
