# 🎯 Quiz Game

A feature-rich, terminal-based trivia quiz application built with Python. Supports single-player and two-player modes, live question fetching from the Open Trivia Database API, offline fallback questions, negative marking, category filtering, and a persistent high-score leaderboard — all rendered beautifully in the terminal using the `rich` library.

---

## ✨ Features

- **Single Player Mode** — Answer trivia questions solo with negative marking enabled
- **Multiplayer Mode** — Two players compete head-to-head on the same question set; ties are broken by completion time
- **Live API Questions** — Fetches fresh questions from the [Open Trivia Database (OpenTDB)](https://opentdb.com/) on every session
- **Offline Fallback** — Automatically switches to a built-in question bank if the API is unavailable
- **14 Categories** — General Knowledge, Computers, Sports, Geography, History, Science & Nature, Books, Film, Music, Video Games, Mythology, Animals, Politics, and Comics
- **3 Difficulty Levels** — Easy, Medium, and Hard (or random)
- **Configurable Question Count** — Choose between 5 and 50 questions per session
- **Negative Marking** — Incorrect answers deduct 0.25 points; skipped questions score 0
- **Skip Option** — Players can skip any question without penalty
- **Category Performance Breakdown** — Visual progress bars showing accuracy per category after each game
- **Persistent High Scores** — Top 20 scores saved to `high_scores.json`, ranked by score and date
- **Rich Terminal UI** — Colourful panels, tables, and progress bars powered by the `rich` library

---

## 📁 Project Structure

```
Quiz/
├── quiz_final.py          # Main application — game engine, menus, multiplayer, scoring
├── fallback_questions.py  # Offline question bank (14 categories, multiple difficulties)
└── high_scores.json       # Auto-generated persistent leaderboard (top 20 scores)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/ankita252006/Quiz.git
   cd Quiz
   ```

2. **Install dependencies**

   ```bash
   pip install rich requests
   ```

3. **Run the game**

   ```bash
   python quiz_final.py
   ```

---

## 🎮 How to Play

### Main Menu

On launch, you are presented with four options:

```
1. Play Quiz (Single Player)
2. Multiplayer Mode
3. High Scores
4. Exit
```

### Configuring a Game

Both single-player and multiplayer sessions prompt you to configure:

| Setting | Options | Default |
|---|---|---|
| Number of questions | 5 – 50 | 10 |
| Category | 1 – 14 (or Enter for random) | Random |
| Difficulty | Easy / Medium / Hard (or Enter for random) | Random |

### Answering Questions

- Each question is displayed in a panel with four options labelled **A, B, C, D**
- Type your answer letter and press Enter
- Type `skip` to skip the question (no points lost)
- **Correct answer** → +1 point
- **Wrong answer** → −0.25 points (negative marking)
- **Skipped** → 0 points

### Multiplayer Rules

- Both players answer the **same set of questions** in turns
- The player with the **higher score wins**
- If scores are **tied**, the player who completed the quiz **faster** wins
- If both score and time are identical, it is declared a **perfect tie**

---

## 📊 Scoring & High Scores

- Final scores are displayed at the end of each game along with total time taken
- A per-category accuracy breakdown with visual progress bars is shown after every session
- Results are automatically saved to `high_scores.json` (top 20 entries, sorted by score)
- View the leaderboard at any time from the main menu → **High Scores**

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `rich` | Terminal UI — panels, tables, coloured text, progress bars |
| `requests` | HTTP requests to the OpenTDB API |

Install both with:

```bash
pip install rich requests
```

---

## 🌐 API Reference

Questions are fetched from the **Open Trivia Database**:

- **Endpoint:** `https://opentdb.com/api.php`
- **Type:** Multiple choice (4 options)
- **Fallback:** If the API is unreachable or returns an error, the app silently loads questions from `fallback_questions.py`

---

## 🗂️ Available Categories

| # | Category |
|---|---|
| 1 | General Knowledge |
| 2 | Science: Computers |
| 3 | Sports |
| 4 | Geography |
| 5 | History |
| 6 | Science & Nature |
| 7 | Entertainment: Books |
| 8 | Entertainment: Film |
| 9 | Entertainment: Music |
| 10 | Entertainment: Video Games |
| 11 | Mythology |
| 12 | Animals |
| 13 | Politics |
| 14 | Entertainment: Comics |

---

## 🛠️ Adding Fallback Questions

To expand the offline question bank, open `fallback_questions.py` and add entries to the `FALLBACK_QUESTIONS` list following this format:

```python
{
    "prompt": "Your question here?",
    "choices": ["Option A", "Option B", "Option C", "Option D"],
    "answer_index": 0,          # 0-based index of the correct answer
    "category": "General Knowledge",  # Must match an OpenTDB category name exactly
    "difficulty": "Medium"      # "Easy" | "Medium" | "Hard"
}
```

---

## 📄 License

This project is open source. Feel free to fork, modify, and share.

---

## 🙌 Acknowledgements

- [Open Trivia Database](https://opentdb.com/) — Free trivia question API
- [Rich](https://github.com/Textualize/rich) — Beautiful terminal formatting library for Python
