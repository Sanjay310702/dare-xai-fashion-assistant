Markdown

# 👔 Multimodal AI Fashion Outfit Recommendation System

An intelligent, enterprise-grade **Multi-Modal Conversational RAG (Retrieval-Augmented Generation) Fashion Assistant** engineered for the Dare XAI Machine Learning & AI Engineer Intern Assignment. 

This platform maps conversational natural language requests, user demographics, and style personas to surface highly compatible, pre-curated outfit configurations from a local data warehouse. Every recommendation is delivered through a high-performance web interface featuring an automated multi-image product layout grid, real-time JSON database metadata inspection, and custom styling rationales explaining the design choices.

---

## 🚀 Mapping Implementation to Assignment Requirements

This system delivers comprehensive, end-to-end compliance with all 5 core evaluation modules specified in the Dare XAI problem statement:

### 1. Dataset Analysis & Understanding (Requirement 1)
* **Implementation Asset**: Evaluated autonomously via `eda.py` and visualized permanently within the **Dataset Inventory Analytics Tab** of the live dashboard interface.
* [cite_start]**Technical Depth**: Automatically reads the columns of the database asset, calculates data dimensional profiles, isolates structural data sparsity, and tracks categorical balances across male and female design paths.

### 2. Outfit Compatibility Engine (Requirement 2)
* **Implementation Asset**: Processed through the dense multi-attribute feature text synthesis loop within `build_db.py`.
* **Technical Depth**: Instead of executing isolated single-product evaluations that risk clashing styles, the engine treats outfit coordination as a holistic graph entity. [cite_start]By packaging clothing attributes (Hero topwear, complementary bottoms, layers, footwear, and accessory tracks)  into a single semantic block, style harmony is transformed into a vector proximity mathematical problem resolved instantly via ChromaDB.

### 3. User & Context-Aware Recommendations (Requirement 3)
* **Implementation Asset**: Controlled dynamically via the interactive sidebar parameters in `app new.py`.
* **Technical Depth**: Intercepts real-time user features—including **Target Gender** (`men`, `women`, `unisex`), **User Age** (e.g., 20s styling vs mature profiles), and **Style Persona** (`Casual`, `Formal`, `Smart Casual`, `Party Wear`, `Ethnic`)—and binds them directly to the semantic vector search string to bias the retrieval search toward the proper context.

### 4. Conversational Fashion Assistant Interface (Requirement 4)
* **Implementation Asset**: Powered through the stateful chat viewport layout inside `app new.py`.
* **Technical Depth**: Utilizes specialized application session state memories (`st.session_state.messages`) to track conversational context. It automatically receives multi-item configuration rows from the database and maps them cleanly into conversational speech items.

### 5. Explainability & Stylist Logic (Requirement 5)
* **Implementation Asset**: Processed in real-time using the Google Gemini inference routing engine (`gemini-flash-latest`).
* **Technical Depth**: The LLM functions strictly as a deep reasoning framework. Anchored by the factual metadata retrieved from ChromaDB, it evaluates and explains color balance, silhouette weight, and venue appropriateness specifically tailored to the user's explicit request and demographic profile.

---

## 📊 Dataset Discoveries & Strategic Architecture Choices

During early development stages using `eda.py`, a critical structural pattern was discovered inside the provided data warehouse:
* [cite_start]**Collection Profile**: 25 highly unique, curated designer outfit rows mapped across 22 individual attribute columns.
* [cite_start]**The Sparsity Profile**: Exactly 12 rows contain explicit missing values (`NaN`) for the `second` (bottomwear) attribute.
* [cite_start]**The Structural Insight**: Cross-referencing revealed that these 12 rows belong exclusively to the 15 female design tracks [cite: 1][cite_start]—representing one-piece garments like the *Women Bodycon Midi Length Dress (Fyre Rose)* [cite: 1][cite_start], *Bodycon Midi Dress (MULVARI)* [cite: 2][cite_start], or the *Ruched Asymmetrical Midi Dress (MANGO)* [cite: 4] where separate bottomwear items do not exist.

> 🛠️ **Core Architectural Strategy**: Evaluating single items independently would incorrectly flag these records as missing data and break composition rules. To preserve designer combination synergy and bypass item-level gaps safely, this system utilizes an **Outfit-Level Vector Model**, indexing entire stylized configurations together.

---

## 🧠 High-Dimensional RAG Data Pipeline Workflow

The complete end-to-end data processing loop functions according to the following architecture:

[ Conversational Natural Language Query ]
│
▼
[ Side-Channel Profile Parameters ] ──► (Injects Gender, Age, & Style Persona State)
│
▼
[ Semantic Query Concatenation Layer ]
│
▼
[ Local Vector Dense Retrieval Match ] ──► (Sentence Transformers: all-MiniLM-L6-v2)
│
▼
[ Context-Anchored Prompt Generation ] ──► (Binds Factual Inventory Data to Prompt)
│
▼
[ Gemini Cognitive Inference Engine ]  ──► (API Stable Alias: gemini-flash-latest)
│
▼
[ Multi-Modal Frontend Presentation ]  ──► (Renders Stylist Explanation + Parallel Images)


---

## 🛠️ The System Optimization & Debug Ledger

This section documents the chronological development hurdles encountered during the project assembly and the explicit technical fixes engineered to resolve them:

* **Operating System Script Execution Restrictions**:
  * *Hurdle*: Attempting to activate the isolated virtual workspace (`.\venv\Scripts\activate`) failed with a Windows PowerShell `UnauthorizedAccess` exception.
  * *Resolution*: Modified security boundaries for the current active workspace terminal using an un-restricted user-scoped policy override command: `Set-ExecutionPolicy Unrestricted -Scope CurrentUser`.
* **Workspace Path Bleeding & File Ingestion Pollution**:
  * *Hurdle*: The file-scanning loop in `eda.py` picked up unrelated configuration files (e.g., VS Code internal environment tables like `codicon.csv`), skewing structural analytics metrics.
  * *Resolution*: Upgraded discovery pathing from a broad relative directory scan to an absolute script-level directory locator (`os.path.dirname(os.path.abspath(__file__))`) while explicitly blacklisting workspace management folders (`venv` and `.git`).
* **Clean-Slate Sandbox Dependency Disconnects**:
  * *Hurdle*: Executing scripts inside the workspace returned severe `ModuleNotFoundError: No module named 'pandas'` errors because initial library commands were written to the computer's global system environment before environment activation.
  * *Resolution*: Activated the sandbox environment first and re-installed dependencies within the isolated shell to cleanly map bindings.
* **API Version Deprecation (404) & Quota Rate Limits (429)**:
  * *Hurdle*: Target backend configurations using legacy models (`models/gemini-1.5-flash`) returned `404 Not Found` messages due to endpoint updates. Rapid back-to-back local testing also triggered severe `429 Rate Limit` exceptions (capping free-tier requests to 5 per minute).
  * *Resolution*: Refactored the core inference router to utilize the stable, auto-routing live service alias **`gemini-flash-latest`**. This bypassed version blocks and stabilized response times under heavy testing constraints.

---

## 📁 Repository Directory Profile

The completed project repository features a clean, professional file architecture:
```text
ML-TASK/
├── app new.py              # Full-stack Streamlit dashboard controller (UI & RAG logic)
├── build_db.py             # Database compilation engine & ChromaDB vector indexer
├── eda.py                  # Exploratory Data Analysis & quality check script
├── outfits.csv             # Raw curated data file containing outfit configurations
└── chroma_db/              # Local persistent vector storage folder (auto-generated)

1. eda.py (Exploratory Data Analysis File)

    Purpose: Performs a thorough check on data warehouse health, category layouts, and value completeness.

    Core Logic: Uses os.walk to scan directories while skipping virtual environments. It loads outfits.csv to evaluate matrix shapes, maps column properties, counts missing values, and prints top value frequencies across attributes like gender and occasion.  

2. build_db.py (Vector Database Compiler File)

    Purpose: Converts flat dataset rows into mathematical multi-dimensional coordinates.

    Core Logic: Replaces null entries with empty strings  using .fillna(""). It combines disjointed columns—including gender, wear_type, occasion, theme, palette , item breakdowns (hero, second, layer, footwear, accessory_1) , and the original stylist_rationale —into a single textual paragraph. These dense descriptions are converted into vector embeddings and written to local storage using an automated Upsert Mechanism that matches incoming files by outfit_id  to prevent duplicate rows.  

3. app new.py (Full-Stack UI & RAG Controller File)

    Purpose: The interactive center managing sidebar parameter states, session chat records, real-time RAG lookups, and visual column graphics.

    Core Logic:

        Integrates custom CSS styling to render a professional dark-themed workspace with gradient banners.

        Implements a stateful architecture using st.session_state.messages to preserve the user's chat history across updates.

        Coordinates image file arrays by splitting the semicolon-separated values found in image_files  via .split(';'). It validates asset existence locally using os.path.exists() and aligns components horizontally using dynamic column blocks (st.columns).  

💻 Local Deployment & System Verification Guide

Follow these exact operational steps to deploy, run, and review the entire application pipeline on a local operating system:
Step 1: Initialize Workspace & Environment Isolation

Open a terminal window on your machine and run these setup commands:
PowerShell

# Navigate into the project directory root
cd C:\Users\sanjay\ML-TASK

# Adjust system script execution policies
Set-ExecutionPolicy Unrestricted -Scope CurrentUser

# Execute the virtual environment boot script
.\venv\Scripts\activate

(Your prompt terminal line will now display a (venv) tag at the very front, confirming the isolated sandbox is active).
Step 2: Install Project Dependencies

Run the package installer tool to configure the required engineering libraries:
PowerShell

pip install pandas streamlit google-generativeai chromadb transformers torch pillow

Step 3: Build the Semantic Vector Database Store

Compile the local dataset and generate the vector embedding files:
PowerShell

python build_db.py

Expected Terminal Output Confirmation:
Plaintext

Loaded 25 outfits. Initializing Vector Database...
Successfully indexed 25 fashion outfits into ChromaDB vector space!

Step 4: Launch the Interactive AI Dashboard

Boot up the full frontend application and connect the RAG backend loop:
PowerShell

streamlit run "app new.py"

Your local browser will automatically open an interactive tab at http://localhost:8501, displaying the completed multi-modal RAG assistant dashboard and analytics tracking center.
