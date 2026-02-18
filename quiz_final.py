from __future__ import annotations
import json
import random
import datetime
import time
import requests
import html
from dataclasses import dataclass, asdict
from typing import List, Optional
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table
from rich import box

console = Console()

QUESTIONS_FILE = "questions.json"
HIGH_SCORES_FILE = "high_scores.json"
MAX_HIGH_SCORES = 20
TRIVIA_API_URL = "https://opentdb.com/api.php"

# ---------------- DATA MODELS ----------------

@dataclass
class Question:
    prompt: str
    choices: List[str]
    answer_index: int
    category: Optional[str] = None
    difficulty: Optional[str] = "Medium"

@dataclass
class Result:
    player_name: str
    score: int
    max_score: int
    date: str
    total_time: Optional[float] = None
    category_stats: Optional[dict] = None

# ---------------- DEFAULT QUESTIONS ----------------

DEFAULT_QUESTIONS = [
    Question(
        "What is the capital of France?",
        ["Berlin", "Madrid", "Paris", "Rome"],
        2,
        "Geography",
        "Easy"
    ),
    Question(
        "Which data structure uses FIFO?",
        ["Stack", "Queue", "Tree", "Hash Table"],
        1,
        "Computer Science",
        "Medium"
    ),
]

# ---------------- STORAGE ----------------

def fetch_questions_from_api(amount=10, category=None, difficulty=None):
    """
    Fetch questions from Open Trivia Database API
    
    Categories:
    9: General Knowledge, 10: Books, 11: Film, 12: Music, 
    13: Musicals & Theatres, 14: Television, 15: Video Games,
    16: Board Games, 17: Science & Nature, 18: Computers,
    19: Mathematics, 20: Mythology, 21: Sports, 22: Geography,
    23: History, 24: Politics, 25: Art, 26: Celebrities,
    27: Animals, 28: Vehicles, 29: Comics, 30: Gadgets,
    31: Japanese Anime & Manga, 32: Cartoon & Animations
    
    Difficulty: easy, medium, hard
    """
    try:
        params = {
            'amount': amount,
            'type': 'multiple'
        }
        
        if category:
            params['category'] = category
        
        if difficulty:
            params['difficulty'] = difficulty
        
        console.print("[yellow]Fetching questions from API...[/yellow]")
        response = requests.get(TRIVIA_API_URL, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data['response_code'] != 0:
            console.print("[red]API Error: Could not fetch questions[/red]")
            return None
        
        questions = []
        for item in data['results']:
            # Decode HTML entities
            prompt = html.unescape(item['question'])
            correct = html.unescape(item['correct_answer'])
            incorrect = [html.unescape(ans) for ans in item['incorrect_answers']]
            
            # Combine choices - correct answer at the end
            all_choices = incorrect + [correct]
            answer_index = len(incorrect)  # Index of correct answer
            
            questions.append(Question(
                prompt=prompt,
                choices=all_choices,
                answer_index=answer_index,
                category=html.unescape(item['category']),
                difficulty=item['difficulty'].capitalize()
            ))
        
        console.print(f"[green]Successfully fetched {len(questions)} questions![/green]")
        time.sleep(1)
        return questions
        
    except requests.RequestException as e:
        console.print(f"[red]Network error: {e}[/red]")
        return None
    except Exception as e:
        console.print(f"[red]Error fetching questions: {e}[/red]")
        return None

def load_questions():
    try:
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Question(**q) for q in data]
    except:
        return DEFAULT_QUESTIONS

def load_high_scores():
    try:
        with open(HIGH_SCORES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Result(**r) for r in data]
    except:
        return []

def save_high_scores(results):
    results_sorted = sorted(results, key=lambda r: (-r.score, r.date))[:MAX_HIGH_SCORES]
    with open(HIGH_SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in results_sorted], f, indent=2)

# ---------------- GAME ----------------

class QuizGame:

    def __init__(self, questions, negative_marking=False, player_name=None):
        self.questions = questions
        self.score = 0
        self.negative_marking = negative_marking
        self.category_stats = {}  # Track performance by category
        self.question_times = []  # Track time for each question
        self.player_name = player_name  # Optional pre-set player name

    def ask_question(self, q, current, total):

        console.clear()

        console.print(Panel(f"Question {current}/{total}", style="bold magenta"))

        # For display, shuffle the choices
        indexed = list(enumerate(q.choices))
        random.shuffle(indexed)
        new_indices, shuffled = zip(*indexed)
        correct_index = new_indices.index(q.answer_index)

        question_panel = Panel(
            f"[bold]{q.prompt}[/bold]\n\n"
            f"[cyan]A.[/cyan] {shuffled[0]}\n"
            f"[cyan]B.[/cyan] {shuffled[1]}\n"
            f"[cyan]C.[/cyan] {shuffled[2]}\n"
            f"[cyan]D.[/cyan] {shuffled[3]}\n\n"
            f"[dim](Type 'skip' to skip this question)[/dim]",
            title=f"{q.category} | {q.difficulty}",
            box=box.ROUNDED
        )

        console.print(question_panel)

        # Track time for this question
        question_start = time.time()

        # Input validation loop
        while True:
            answer = console.input("[bold white]Your answer (A/B/C/D/skip): [/bold white]").upper()
            
            labels = ["A", "B", "C", "D"]
            
            if answer == "SKIP":
                question_time = time.time() - question_start
                self.question_times.append(question_time)
                correct_answer = shuffled[correct_index]
                console.print(f"[yellow]Skipped! (0 point)[/yellow]")
                console.print(f"[yellow]Correct answer was {labels[correct_index]}: {correct_answer}[/yellow]")
                
                # Track category stats
                if q.category not in self.category_stats:
                    self.category_stats[q.category] = {"correct": 0, "total": 0}
                self.category_stats[q.category]["total"] += 1
                
                time.sleep(2)
                return
            elif answer in labels:
                break
            else:
                console.print("[red]Invalid input! Please enter A, B, C, D, or 'skip'[/red]")

        question_time = time.time() - question_start
        self.question_times.append(question_time)

        # Track category stats
        if q.category not in self.category_stats:
            self.category_stats[q.category] = {"correct": 0, "total": 0}
        self.category_stats[q.category]["total"] += 1

        if labels.index(answer) == correct_index:
            console.print("[green]✓ Correct! (+1 point)[/green]")
            self.score += 1
            self.category_stats[q.category]["correct"] += 1
        else:
            correct_answer = shuffled[correct_index]
            if self.negative_marking:
                console.print(f"[red]Wrong! Correct answer was {labels[correct_index]}: {correct_answer} (-0.25 points)[/red]")
                self.score -= 0.25
            else:
                console.print(f"[red]Wrong! Correct answer was {labels[correct_index]}: {correct_answer}[/red]")

        time.sleep(1.5)

    def run(self):
        console.clear()
        console.print(Panel("Welcome to the Quiz Game", style="bold cyan"))

        # Use pre-set name if provided, otherwise ask for it
        if self.player_name:
            name = self.player_name
            console.print(f"[bold yellow]Player: {name}[/bold yellow]\n")
            console.input("[dim]Press Enter to start...[/dim]")
        else:
            name = console.input("[bold yellow]Enter your name: [/bold yellow]")
        
        random.shuffle(self.questions)

        total = len(self.questions)

        # Start overall timer
        start_time = time.time()

        # Create progress but don't show it during questions
        for i, q in enumerate(self.questions, 1):
            self.ask_question(q, i, total)
            
            # Show progress with time only for last 2 questions
            if i >= total - 1:
                elapsed = time.time() - start_time
                minutes = int(elapsed // 60)
                seconds = int(elapsed % 60)
                console.clear()
                console.print(f"[cyan]Progress: {i}/{total} questions completed[/cyan]")
                console.print(f"[yellow]Time elapsed: {minutes}m {seconds}s[/yellow]")
                time.sleep(1)

        # Calculate total time
        total_time = time.time() - start_time
        minutes = int(total_time // 60)
        seconds = int(total_time % 60)

        console.clear()
        
        # Format score display based on negative marking
        if self.negative_marking:
            score_text = f"[bold green]Final Score: {self.score:.2f}/{total}[/bold green]"
        else:
            score_text = f"[bold green]Final Score: {int(self.score)}/{total}[/bold green]"
        
        console.print(Panel(
            f"{score_text}\n"
            f"[bold yellow]Total Time: {minutes}m {seconds}s[/bold yellow]"
        ))
        
        # Show category progress bar
        show_category_progress(self.category_stats)

        return Result(
            player_name=name,
            score=self.score,
            max_score=total,
            date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            total_time=total_time,
            category_stats=self.category_stats
        )

# ---------------- HIGH SCORES ----------------

def show_category_progress(category_stats):
    """Display category-wise performance with progress bars"""
    if not category_stats:
        return
    
    console.print("\n[bold cyan]Category Performance:[/bold cyan]")
    
    for category, stats in category_stats.items():
        correct = stats["correct"]
        total = stats["total"]
        percentage = (correct / total * 100) if total > 0 else 0
        
        # Create visual progress bar
        bar_length = 20
        filled = int(bar_length * correct / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_length - filled)
        
        # Color based on performance
        if percentage >= 80:
            color = "green"
        elif percentage >= 50:
            color = "yellow"
        else:
            color = "red"
        
        console.print(f"[{color}]{category:20}[/{color}] [{color}]{bar}[/{color}] {correct}/{total} ({percentage:.0f}%)")
    
    console.print()

def show_high_scores():
    scores = load_high_scores()

    table = Table(title="High Scores", box=box.HEAVY_EDGE)
    table.add_column("Rank", justify="center")
    table.add_column("Name")
    table.add_column("Score")
    table.add_column("Time")
    table.add_column("Date")

    for i, r in enumerate(sorted(scores, key=lambda r: (-r.score, r.date))[:10], 1):
        time_str = "N/A"
        if r.total_time:
            minutes = int(r.total_time // 60)
            seconds = int(r.total_time % 60)
            time_str = f"{minutes}m {seconds}s"
        
        # Format score - show decimal if it's not a whole number
        if isinstance(r.score, float) and r.score % 1 != 0:
            score_str = f"{r.score:.2f}/{r.max_score}"
        else:
            score_str = f"{int(r.score)}/{r.max_score}"
        
        table.add_row(str(i), r.player_name, score_str, time_str, r.date)

    console.print(table)

# ---------------- MULTIPLAYER MODE ----------------

def multiplayer_mode(questions):
    """Two-player mode where both players answer the same questions"""
    console.clear()
    console.print(Panel("🎮 Multiplayer Mode", style="bold magenta"))
    
    # Get player names
    player1_name = console.input("[bold yellow]Player 1 name: [/bold yellow]")
    player2_name = console.input("[bold yellow]Player 2 name: [/bold yellow]")
    
    console.print(f"\n[cyan]Welcome {player1_name} and {player2_name}![/cyan]")
    console.print("[yellow]You will both answer the same questions.[/yellow]")
    console.input("\n[dim]Press Enter to start...[/dim]")
    
    # Player 1's turn
    console.clear()
    console.print(Panel(f"🎮 {player1_name}'s Turn", style="bold green"))
    
    game1 = QuizGame(list(questions), negative_marking=True, player_name=player1_name)
    result1 = game1.run()
    
    console.input("\n[dim]Press Enter to continue to Player 2...[/dim]")
    
    # Player 2's turn (same questions)
    console.clear()
    console.print(Panel(f"🎮 {player2_name}'s Turn", style="bold blue"))
    
    game2 = QuizGame(list(questions), negative_marking=True, player_name=player2_name)
    result2 = game2.run()
    
    console.input("\n[dim]Press Enter to see results...[/dim]")
    
    # Display results
    console.clear()
    console.print(Panel("🏆 Multiplayer Results", style="bold magenta"))
    
    results_table = Table(box=box.ROUNDED)
    results_table.add_column("Player", style="cyan")
    results_table.add_column("Score", style="yellow")
    results_table.add_column("Time", style="green")
    results_table.add_column("Result", style="bold")
    
    time1_str = f"{int(result1.total_time // 60)}m {int(result1.total_time % 60)}s"
    time2_str = f"{int(result2.total_time // 60)}m {int(result2.total_time % 60)}s"
    
    # Determine winner
    if result1.score > result2.score:
        winner = player1_name
        results_table.add_row(
            player1_name,
            f"{result1.score:.2f}/{result1.max_score}",
            time1_str,
            "[green]🏆 WINNER![/green]"
        )
        results_table.add_row(
            player2_name,
            f"{result2.score:.2f}/{result2.max_score}",
            time2_str,
            "[red]Lost[/red]"
        )
    elif result2.score > result1.score:
        winner = player2_name
        results_table.add_row(
            player1_name,
            f"{result1.score:.2f}/{result1.max_score}",
            time1_str,
            "[red]Lost[/red]"
        )
        results_table.add_row(
            player2_name,
            f"{result2.score:.2f}/{result2.max_score}",
            time2_str,
            "[green]🏆 WINNER![/green]"
        )
    else:
        # Tie - compare by time
        if result1.total_time < result2.total_time:
            winner = player1_name
            results_table.add_row(
                player1_name,
                f"{result1.score:.2f}/{result1.max_score}",
                time1_str,
                "[green]🏆 WINNER! (Faster)[/green]"
            )
            results_table.add_row(
                player2_name,
                f"{result2.score:.2f}/{result2.max_score}",
                time2_str,
                "[red]Lost (Slower)[/red]"
            )
        elif result2.total_time < result1.total_time:
            winner = player2_name
            results_table.add_row(
                player1_name,
                f"{result1.score:.2f}/{result1.max_score}",
                time1_str,
                "[red]Lost (Slower)[/red]"
            )
            results_table.add_row(
                player2_name,
                f"{result2.score:.2f}/{result2.max_score}",
                time2_str,
                "[green]🏆 WINNER! (Faster)[/green]"
            )
        else:
            # Perfect tie
            winner = None
            results_table.add_row(
                player1_name,
                f"{result1.score:.2f}/{result1.max_score}",
                time1_str,
                "[yellow]🤝 TIE![/yellow]"
            )
            results_table.add_row(
                player2_name,
                f"{result2.score:.2f}/{result2.max_score}",
                time2_str,
                "[yellow]🤝 TIE![/yellow]"
            )
    
    console.print(results_table)
    
    if winner:
        console.print(f"\n[bold green]🎉 Congratulations {winner}! You won![/bold green]")
    else:
        console.print(f"\n[bold yellow]🤝 Perfect tie! Both players performed equally well![/bold yellow]")
    
    # Save both results to high scores
    scores = load_high_scores()
    scores.append(result1)
    scores.append(result2)
    save_high_scores(scores)

# ---------------- MENU ----------------

def main_menu():
    
    # Define categories with proper formatting
    categories_dict = {
        1: (9, "GK"),
        2: (18, "Computers"),
        3: (21, "Sports"),
        4: (22, "Geography"),
        5: (23, "History"),
        6: (17, "Science & Nature"),
        7: (10, "Books"),
        8: (11, "Film"),
        9: (12, "Music"),
        10: (15, "Video Games"),
        11: (20, "Mythology"),
        12: (27, "Animals"),
        13: (24, "Politics"),
        14: (29, "Comics")
    }

    while True:
        console.clear()

        console.print(Panel("Main Menu", style="bold blue"))
        console.print("[bold cyan]1.[/bold cyan] Play Quiz (Single Player)")
        console.print("[bold cyan]2.[/bold cyan] Multiplayer Mode")
        console.print("[bold cyan]3.[/bold cyan] High Scores")
        console.print("[bold cyan]4.[/bold cyan] Exit")

        choice = console.input("\nChoose option: ")

        if choice == "1":
            # API Quiz options
            console.clear()
            console.print(Panel("Quiz Configuration", style="bold green"))
            
            # Ask for number of questions with validation
            while True:
                num_input = console.input("[yellow]Number of questions (5-50, default 10): [/yellow]")
                if num_input == "":
                    num_questions = 10
                    break
                try:
                    num_questions = int(num_input)
                    if 5 <= num_questions <= 50:
                        break
                    else:
                        console.print("[red]Invalid input! Please enter a number between 5 and 50.[/red]")
                except ValueError:
                    console.print("[red]Invalid input! Please enter a valid number.[/red]")
            
            # Display categories in structured format
            console.print("\n[bold cyan]Categories:[/bold cyan]")
            for i in range(1, 15, 2):
                if i+1 <= 14:
                    left = f"[cyan]{i}.[/cyan] {categories_dict[i][1]}"
                    right = f"[cyan]{i+1}.[/cyan] {categories_dict[i+1][1]}"
                    # Use proper spacing - pad left side to 35 characters
                    console.print(f"{left:<35}{right}")
                else:
                    console.print(f"[cyan]{i}.[/cyan] {categories_dict[i][1]}")
            
            console.print("[dim]Press Enter for random category[/dim]")
            
            # Category selection with validation
            while True:
                category_input = console.input("[yellow]Category number (1-14): [/yellow]")
                if category_input == "":
                    category = None
                    break
                try:
                    cat_num = int(category_input)
                    if 1 <= cat_num <= 14:
                        category = categories_dict[cat_num][0]
                        break
                    else:
                        console.print("[red]Invalid input! Please enter a number between 1 and 14.[/red]")
                except ValueError:
                    console.print("[red]Invalid input! Please enter a valid number.[/red]")
            
            # Ask for difficulty with validation
            console.print("\n[bold cyan]Difficulty:[/bold cyan]")
            console.print("[cyan]1.[/cyan] Easy")
            console.print("[cyan]2.[/cyan] Medium")
            console.print("[cyan]3.[/cyan] Hard")
            console.print("[dim]Press Enter for random difficulty[/dim]")
            
            while True:
                diff_input = console.input("[yellow]Difficulty (1-3): [/yellow]")
                if diff_input == "":
                    difficulty = None
                    break
                elif diff_input == "1":
                    difficulty = "easy"
                    break
                elif diff_input == "2":
                    difficulty = "medium"
                    break
                elif diff_input == "3":
                    difficulty = "hard"
                    break
                else:
                    console.print("[red]Invalid input! Please enter 1, 2, or 3.[/red]")
            
            # Fetch questions
            api_questions = fetch_questions_from_api(num_questions, category, difficulty)
            
            if api_questions:
                # Negative marking is enabled by default
                game = QuizGame(api_questions, negative_marking=True)
                result = game.run()
                
                scores = load_high_scores()
                scores.append(result)
                save_high_scores(scores)
            else:
                console.print("[red]Failed to fetch questions. Please try again.[/red]")
            
            console.input("\nPress Enter to return to menu...")
        elif choice == "2":
            # Multiplayer Mode
            console.clear()
            console.print(Panel("Multiplayer Quiz Configuration", style="bold green"))
            
            # Ask for number of questions with validation
            while True:
                num_input = console.input("[yellow]Number of questions (5-50, default 10): [/yellow]")
                if num_input == "":
                    num_questions = 10
                    break
                try:
                    num_questions = int(num_input)
                    if 5 <= num_questions <= 50:
                        break
                    else:
                        console.print("[red]Invalid input! Please enter a number between 5 and 50.[/red]")
                except ValueError:
                    console.print("[red]Invalid input! Please enter a valid number.[/red]")
            
            # Display categories in structured format
            console.print("\n[bold cyan]Categories:[/bold cyan]")
            for i in range(1, 15, 2):
                if i+1 <= 14:
                    left = f"[cyan]{i}.[/cyan] {categories_dict[i][1]}"
                    right = f"[cyan]{i+1}.[/cyan] {categories_dict[i+1][1]}"
                    console.print(f"{left:<35}{right}")
                else:
                    console.print(f"[cyan]{i}.[/cyan] {categories_dict[i][1]}")
            
            console.print("[dim]Press Enter for random category[/dim]")
            
            # Category selection with validation
            while True:
                category_input = console.input("[yellow]Category number (1-14): [/yellow]")
                if category_input == "":
                    category = None
                    break
                try:
                    cat_num = int(category_input)
                    if 1 <= cat_num <= 14:
                        category = categories_dict[cat_num][0]
                        break
                    else:
                        console.print("[red]Invalid input! Please enter a number between 1 and 14.[/red]")
                except ValueError:
                    console.print("[red]Invalid input! Please enter a valid number.[/red]")
            
            # Ask for difficulty with validation
            console.print("\n[bold cyan]Difficulty:[/bold cyan]")
            console.print("[cyan]1.[/cyan] Easy")
            console.print("[cyan]2.[/cyan] Medium")
            console.print("[cyan]3.[/cyan] Hard")
            console.print("[dim]Press Enter for random difficulty[/dim]")
            
            while True:
                diff_input = console.input("[yellow]Difficulty (1-3): [/yellow]")
                if diff_input == "":
                    difficulty = None
                    break
                elif diff_input == "1":
                    difficulty = "easy"
                    break
                elif diff_input == "2":
                    difficulty = "medium"
                    break
                elif diff_input == "3":
                    difficulty = "hard"
                    break
                else:
                    console.print("[red]Invalid input! Please enter 1, 2, or 3.[/red]")
            
            # Fetch questions
            api_questions = fetch_questions_from_api(num_questions, category, difficulty)
            
            if api_questions:
                multiplayer_mode(api_questions)
            else:
                console.print("[red]Failed to fetch questions. Please try again.[/red]")
            
            console.input("\nPress Enter to return to menu...")
        elif choice == "3":
            console.clear()
            show_high_scores()
            console.input("\nPress Enter to return...")
        elif choice == "4":
            console.print("[bold red]Goodbye![/bold red]")
            break
        else:
            console.print("[red]Invalid option! Please enter 1, 2, 3, or 4.[/red]")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()