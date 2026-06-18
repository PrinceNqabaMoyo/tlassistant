===== Application Startup at 2026-06-05 09:16:25 =====

[2026-06-05 09:16:59 +0000] [1] [INFO] Starting gunicorn 21.2.0
[2026-06-05 09:16:59 +0000] [1] [INFO] Listening at: http://0.0.0.0:7860 (1)
[2026-06-05 09:16:59 +0000] [1] [INFO] Using worker: sync
[2026-06-05 09:16:59 +0000] [6] [INFO] Booting worker with pid: 6
[2026-06-05 11:18:32 +0000] [1] [INFO] Handling signal: term
[2026-06-05 11:18:32 +0000] [6] [INFO] Worker exiting (pid: 6)
Initializing AI Agents for all personas...
Warning: ChromaDB directory 'chroma_db_langchain' not found. Curriculum search will not work.
-> Student agent initialized.
-> Teacher agent initialized.
-> Admin agent initialized.
All AI Agents initialized successfully.
Loading template modules from: /code/app/utils/templates
Registered Grade 7 template module with 380 templates
Successfully loaded Grade 7 module
Loading template modules from: /code/app/utils/templates
Registered Grade 7 template module with 380 templates
Successfully loaded Grade 7 module
Loading template modules from: /code/app/utils/templates
Registered Grade 7 template module with 380 templates
Successfully loaded Grade 7 module
Redis not available, using memory cache: Error 111 connecting to localhost:6379. Connection refused.
Error sending POP notification email: [Errno 110] Connection timed out
[2026-06-05 11:18:39 +0000] [1] [INFO] Shutting down: Master
