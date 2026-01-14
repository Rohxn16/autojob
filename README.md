Autojob 🚀: The Sovereign AI Agent for Career Domination

"Stop being the product. Start being the priority."

⚡ The Manifesto

In the current job market, you are the prey. Big Tech platforms harvest your resume data, train their models on your experience, and then charge you for the "privilege" of seeing a job post.

Autojob flips the script. Built for the GDG Hackathon, it is a high-performance, open-source Agentic RAG system that automates the hunt while keeping your data strictly on your hardware. It’s not just a script; it’s your personal Career Chief of Staff.

✨ Features (v1.0 Beta)

Our current production-ready core includes:

Agentic Search: Autonomous keyword generation derived from semantic resume analysis.

Multi-Source Aggregation: Real-time job ingestion from TheirStack and LinkedIn.

Local RAG Engine: Instant vector-based matching against your professional history.

Privacy Guard: 100% local inference—your PII never touches a third-party server.

Technical Scoring: A "Success Probability" rank for every job found, based on Gemma 3's deep reasoning.

🔥 Why Autojob Wins

1. 🧠 Powered by Google Gemma 3

Autojob leverages Gemma 3:4B, Google's latest state-of-the-art open model. Built on the same technological foundations as Gemini 2.0, Gemma 3 provides unmatched reasoning capabilities and a massive 128K context window, allowing the agent to process entire resumes and complex job descriptions simultaneously without losing "focus."

2. 🎯 Hyper-Targeted RAG Matching

Standard keyword search is dead. Autojob uses Retrieval-Augmented Generation to understand the semantics of your experience. It understands the difference between "learning Python" and "optimizing low-latency C++ systems," matching you with roles that require your exact engineering depth.

3. 🛡️ Sovereign Privacy (Local-Only)

Your resume is your life story. Autojob processes everything via Ollama and local vector embeddings. Zero data leaves your machine. No "training food" for corporate AI—just pure, private performance powered by Google's open weights.

🧠 Technical Deep-Dive: The Agentic RAG Loop

Autojob operates in a Reasoning-Action (ReAct) loop, specifically optimized for the Gemma 3 architecture:

Ingestion & Embedding: Your PDF is shredded into semantic chunks and embedded into a local ChromaDB vector store using nomic-embed-text.

Autonomous Keyword Synthesis: Gemma 3:4B analyzes your resume to generate a high-dimensional search strategy—uncovering technical keywords and "hidden" skills within your experience.

The API Strike: The system queries the TheirStack API and LinkedIn scrapers to pull live technical data from the top recruiters in the industry.

Semantic Cross-Validation: The Agent retrieves your resume chunks (RAG) and performs a "Zero-Shot" evaluation on every job description found, scoring them for technical alignment.

Priority Ranking: Jobs are sorted by Gemma's Success Probability Score, ensuring you only see roles that are a genuine match.

🚀 The Vision: A Career OS

We are evolving Autojob into a complete Google-integrated ecosystem:

Web & Mobile Dashboards: Sleek UIs for non-technical users to harness AI power.

The HR Closer: Automated, personalized cover letters and HR mailing agents that sound exactly like you.

Skill-Gap Analysis: "You're 90% ready for this role. Learn this specific Google Cloud certification to close the gap."

🛠️ Setup & Deployment

System Requirements: A machine capable of running Ollama (8GB+ RAM recommended for Gemma 3:4B).

### 1. Clone the Beast
clone the repo and cd into it

### 2. Fire up the Local Brain
```
ollama serve
ollama pull gemma3:4b # High-performance reasoning for GDG Hackathon
```
### 3. Initialize Environment
```
cp .env.example .env # Add your TheirStack API Key
pip install -r requirements.txt
```
### 4. Launch the Agent
```python3 main.py```


🤝 Contributing

Autojob is built by hackers for hackers. Whether you're a C++ wizard, a Gemma 3 whisperer, or a UI/UX visionary, join us in reclaiming the job market.

We are currently looking for:

- Frontend Developers and UI/UX Designers to design and bring to life a beautiful, accessible interface.

- Mobile Developers for the upcoming career-tracking app.

Developed with ❤️ and ☕ for the Winter Solstice Hackathon GDGoC MSIT 2026.
