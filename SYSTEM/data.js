// THE SYSTEM — Live Player Data (Synced with GitHub by THE SYSTEM)
window.SYSTEM_DATA = {
  player: "Zackkkkun",
  rank: "D-RANK · PYTHON DEVELOPER",
  level: 4,
  xp: 1600,
  xpPerLevel: 500,
  streakDays: 2,
  studyMinutes: 20,
  goalHours: 170,
  attributes: {
    PY: 12,
    DEBUG: 5,
    GIT: 6,
    ARCH: 3,
    AI: 0
  },
  activeQuest: {
    title: "Build Your Own System Engine (v0.1)",
    file: "system-app/engine.py",
    description: "Wire up parse_command() and craft_item() using Sets, Tuples, and Strings to unlock your playable RPG terminal.",
    rewardXP: 150
  },
  badges: [
    { name: "First Blood", desc: "Completed Day 01" },
    { name: "Phase 1 Clear", desc: "Conquered Python Foundations" },
    { name: "Clean History", desc: "Repaired GitHub commit history" },
    { name: "System Awakened", desc: "Initialized THE SYSTEM HUD" }
  ],
  phases: [
    {
      id: 1,
      rank: "E-RANK",
      name: "Python Foundations",
      status: "done",
      topics: ["Variables & Types", "Conditions & Loops", "Functions & Return", "Lists", "Variable Scope", "Exception Handling", "Integrated SMS Boss"]
    },
    {
      id: 2,
      rank: "D-RANK",
      name: "Python Developer",
      status: "current",
      topics: ["Dictionaries (Done)", "Sets (Done)", "Tuples & Strings (Active)", "Comprehensions", "Modules & venv", "File I/O (CSV/JSON)", "OOP", "pytest & Clean Code", "Boss: Personal Tracker"]
    },
    {
      id: 3,
      rank: "C-RANK",
      name: "SWE Workflow & SQL",
      status: "locked",
      topics: ["Git & CLI Mastery", "SQL & Joins", "CRUD & DB Design", "Boss: FastAPI + Postgres API"]
    },
    {
      id: 4,
      rank: "B-RANK",
      name: "Data & ML Foundations",
      status: "locked",
      topics: ["NumPy & pandas", "Train/Test & Metrics", "Embeddings & Similarity", "Clean UI Basics"]
    },
    {
      id: 5,
      rank: "A-RANK",
      name: "AI Engineering",
      status: "locked",
      topics: ["LLM APIs & Prompting", "Vector DBs & RAG", "Tool Calling & Agents", "AI Evals", "Boss: Deployed AI/RAG App"]
    },
    {
      id: 6,
      rank: "S-RANK",
      name: "Deploy & Job Launch",
      status: "locked",
      topics: ["Docker & Cloud Deploy", "Pythonic DSA", "System Design", "Mock Interviews & Applications"]
    }
  ]
};
